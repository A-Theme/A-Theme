// build-snake.js
//
// A from-scratch snake-pathfinding + SVG animation generator, built
// specifically because Platane/snk (the tool used for the other snake
// on this profile) has NO capability to target a specific past year --
// confirmed by checking its full documented option list, which only
// ever reads "whatever GitHub's live rolling contribution graph
// currently says." This file exists so the year-cycling snake can show
// a genuine, specific calendar year instead.
//
// Algorithm: boustrophedon ("lawnmower") traversal -- the snake moves
// down column 0, right to column 1, up column 1, right to column 2,
// down column 2, and so on. This guarantees every cell in the grid is
// visited exactly once, the path never crosses itself, and the logic is
// simple enough to verify correctness directly (unlike trying to
// reverse-engineer Platane/snk's own internal solver, which isn't
// published anywhere I could inspect).
//
// Verified for real before being committed here:
//  - Path visits every cell exactly once, zero gaps, zero duplicates
//    (tested against both a full 52-week grid and a realistic grid with
//    partial first/last weeks, which real GitHub data always has unless
//    the year happens to start on a Sunday)
//  - The "eating" color-flash animation for each contribution day fires
//    at the exact same timestamp the snake head's own animation places
//    it at that cell -- checked programmatically against every sample,
//    zero mismatches
//  - Explicitly uses each day's `weekday` field for row placement rather
//    than array index, since real GitHub API responses have partial
//    weeks at the start/end of a year range and array position would
//    silently misalign rows without this

const LEVEL_MAP = { NONE: 0, FIRST_QUARTILE: 1, SECOND_QUARTILE: 2, THIRD_QUARTILE: 3, FOURTH_QUARTILE: 4 };

function buildSnakeSVG(weeks, year, opts = {}) {
  const CELL = 16;
  const CELL_SIZE = 12;
  const RADIUS = 2;
  const bodyLength = opts.bodyLength || 4;
  const msPerStep = opts.msPerStep || 120;
  const numWeeks = weeks.length;
  const numRows = 7;

  const cells = [];
  weeks.forEach((week, col) => {
    week.contributionDays.forEach((day) => {
      const row = day.weekday; // explicit field, not array index -- see header note
      cells.push({
        col, row,
        count: day.contributionCount,
        level: LEVEL_MAP[day.contributionLevel] ?? (day.contributionCount > 0 ? 1 : 0),
        date: day.date,
      });
    });
  });

  const path = [];
  for (let col = 0; col < numWeeks; col++) {
    const colCells = cells
      .filter(c => c.col === col)
      .sort((a, b) => (col % 2 === 0 ? a.row - b.row : b.row - a.row));
    path.push(...colCells);
  }

  const totalSteps = path.length;
  if (totalSteps === 0) throw new Error('empty contribution grid, nothing to build a path from');

  const totalDurationMs = totalSteps * msPerStep;

  const contributionSteps = path
    .map((cell, i) => ({ ...cell, stepIndex: i }))
    .filter(c => c.count > 0);

  let css = `:root{--cb:#1b1f230a;--cs:#00c2ff;--ce:#161b22;--c0:#161b22;--c1:#0e4429;--c2:#006d32;--c3:#26a641;--c4:#39d353}`;
  css += `.c{shape-rendering:geometricPrecision;fill:var(--ce);stroke-width:1px;stroke:var(--cb);width:${CELL_SIZE}px;height:${CELL_SIZE}px;}`;

  contributionSteps.forEach((c, idx) => {
    const pctStart = (c.stepIndex / totalSteps * 100).toFixed(3);
    const pctEnd = ((c.stepIndex + 1) / totalSteps * 100).toFixed(3);
    css += `@keyframes cc${idx}{${pctStart}%{fill:var(--c${c.level})}${pctEnd}%,100%{fill:var(--ce)}}`;
    css += `.cc${idx}{animation:cc${idx} ${totalDurationMs}ms linear infinite;}`;
  });

  let snakeCss = '';
  let snakeRects = '';
  for (let seg = 0; seg < bodyLength; seg++) {
    let kf = `@keyframes s${seg}{`;
    for (let i = 0; i <= totalSteps; i++) {
      const srcIdx = ((i - seg) % totalSteps + totalSteps) % totalSteps;
      const cell = path[srcIdx];
      const x = cell.col * CELL;
      const y = cell.row * CELL;
      const pct = (i / totalSteps * 100).toFixed(3);
      kf += `${pct}%{transform:translate(${x}px,${y}px)}`;
    }
    kf += `}`;
    snakeCss += kf;
    snakeCss += `.s${seg}{animation:s${seg} ${totalDurationMs}ms linear infinite;}`;
    const size = 14 - seg * 0.6;
    const off = (16 - size) / 2;
    snakeRects += `<rect class="s${seg}" x="${off.toFixed(1)}" y="${off.toFixed(1)}" width="${size.toFixed(1)}" height="${size.toFixed(1)}" rx="4" fill="var(--cs)"/>`;
  }

  let gridRects = '';
  cells.forEach(c => {
    const x = c.col * CELL + 2;
    const y = c.row * CELL + 2;
    const stepEntry = c.count > 0 ? contributionSteps.find(cs => cs.col === c.col && cs.row === c.row) : null;
    const cls = stepEntry ? `c cc${contributionSteps.indexOf(stepEntry)}` : 'c';
    gridRects += `<rect class="${cls}" x="${x}" y="${y}" rx="${RADIUS}" ry="${RADIUS}"/>`;
  });

  const width = numWeeks * CELL + 20;
  const height = numRows * CELL + 34;
  const totalContribs = cells.reduce((s, c) => s + c.count, 0);

  const svg =
    `<svg viewBox="0 0 ${width} ${height}" width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">` +
    `<style>${css}${snakeCss}</style>` +
    `<g transform="translate(10,4)">${gridRects}<g>${snakeRects}</g></g>` +
    `<text x="10" y="${numRows * CELL + 28}" font-family="monospace,'Fira Code'" font-size="14" fill="#00c2ff">${year} \u00b7 ${totalContribs} contributions</text>` +
    `</svg>`;

  return { svg, totalSteps, totalContribs, totalDurationMs };
}

module.exports = { buildSnakeSVG };
