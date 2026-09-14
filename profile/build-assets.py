# -*- coding: utf-8 -*-
"""Generates the animated SVG furniture for the A-Theme profile README.

Everything is hand-rolled SVG: no third-party image service sits in the
critical path, so the profile cannot be broken by someone else's rate limit.
Animation is CSS keyframes + SMIL, both of which GitHub renders inside <img>.

Rule learned the hard way: never put a CSS `transform` animation on an element
that also carries a `transform` attribute -- the CSS property wins and the
element jumps to the origin. Position with an outer <g>, animate an inner one.
"""
import os, random

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
CY, RD, PU, GR, OC = "#00c2ff", "#ff3c50", "#9d4edd", "#5be27a", "#d8924a"
BG, PANEL, EDGE = "#0b1420", "#101c2c", "#1d2e44"
TX, MU, DIM = "#eaf1fa", "#a8bdd4", "#7d95ae"
# Theme counts shown on the cards and the system map. Refresh from:
#   Tinfoil-Themes: len(themes.json["themes"])
#   RomM-Themes:    manifest.json["count"]  (the validator keeps it current)
TINFOIL_COUNT = 173
ROMM_COUNT = 101

MONO = "ui-monospace, 'SFMono-Regular', 'Fira Code', Consolas, monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def adv(text, size):
    """Monospace advance width."""
    return len(text) * size * 0.6


def write(name, body):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        f.write(body)
    print(f"  {name:26s} {len(body):>6d} bytes")


# --------------------------------------------------------------- shared defs
def grid_def(idx="grid", colour=CY, step=44, op=0.07):
    return (f'<pattern id="{idx}" width="{step}" height="{step}" patternUnits="userSpaceOnUse">'
            f'<path d="M{step} 0H0V{step}" fill="none" stroke="{colour}" '
            f'stroke-opacity="{op}" stroke-width="1"/></pattern>')


def build_hero():
    # ============================================================ hero.svg
    W, H = 1200, 300
    stars = []
    for i in range(46):
        x = round(random.uniform(8, W - 8), 1)
        y = round(random.uniform(8, H - 8), 1)
        r = round(random.uniform(0.7, 1.9), 2)
        dur = round(random.uniform(2.4, 6.0), 2)
        beg = round(random.uniform(0, 6.0), 2)
        o = round(random.uniform(0.25, 0.85), 2)
        stars.append(
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#cfe6ff" opacity="{o}">'
            f'<animate attributeName="opacity" values="{o};0.05;{o}" dur="{dur}s" '
            f'begin="{beg}s" repeatCount="indefinite"/></circle>'
        )
    stars = "\n    ".join(stars)

    word = "ARAMAKI"
    letters = []
    x0, step = 92, 104
    for i, ch in enumerate(word):
        letters.append(
            f'<text class="ltr" style="animation-delay:{0.08*i:.2f}s" '
            f'x="{x0 + i*step}" y="158" text-anchor="middle">{ch}</text>'
        )
    letters = "\n    ".join(letters)

    chips = [
        ("native C on a console that says no", CY),
        ("JS on the Switch via nx.js", PU),
        ("k-means palettes, on-device", RD),
        ("PWAs that install for real", GR),
    ]
    cx = 66
    chip_svg = []
    for i, (label, col) in enumerate(chips):
        w = int(len(label) * 7.6) + 46
        chip_svg.append(
            f'<g transform="translate({cx},236)"><g class="chip" style="animation-delay:{0.9 + 0.16*i:.2f}s">'
            f'<rect width="{w}" height="30" rx="15" fill="{col}" fill-opacity="0.10" stroke="{col}" stroke-opacity="0.55"/>'
            f'<circle cx="17" cy="15" r="3.6" fill="{col}">'
            f'<animate attributeName="opacity" values="1;0.25;1" dur="{2.2 + 0.35*i:.2f}s" repeatCount="indefinite"/></circle>'
            f'<text class="chip-t" x="29" y="19.5" fill="{col}">{label}</text></g></g>'
        )
        cx += w + 14
    chip_svg = "\n    ".join(chip_svg)

    hero = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
      viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img"
      aria-labelledby="heroTitle heroDesc">
      <title id="heroTitle">Aramaki</title>
      <desc id="heroDesc">Animated banner: the name ARAMAKI over a drifting starfield, with tags for native C Switch homebrew, JavaScript on the Switch via nx.js, on-device k-means palettes, and installable web apps.</desc>

      <defs>
        <linearGradient id="sky" x1="0" y1="0" x2="0.35" y2="1">
          <stop offset="0" stop-color="#0e1c2e"/>
          <stop offset="0.55" stop-color="#0b1420"/>
          <stop offset="1" stop-color="#070e17"/>
        </linearGradient>

        <linearGradient id="ink" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="{CY}"/>
          <stop offset="0.3" stop-color="{PU}"/>
          <stop offset="0.62" stop-color="{RD}"/>
          <stop offset="1" stop-color="{CY}"/>
          <animateTransform attributeName="gradientTransform" type="translate"
            values="-0.55 0; 0.55 0; -0.55 0" dur="11s" repeatCount="indefinite"/>
        </linearGradient>

        <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="{CY}" stop-opacity="0"/>
          <stop offset="0.5" stop-color="{PU}" stop-opacity="0.9"/>
          <stop offset="1" stop-color="{RD}" stop-opacity="0"/>
        </linearGradient>

        <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">
          <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
          <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.30"/>
          <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
        </linearGradient>

        <radialGradient id="halo" cx="0.5" cy="0.5" r="0.5">
          <stop offset="0" stop-color="{CY}" stop-opacity="0.30"/>
          <stop offset="1" stop-color="{CY}" stop-opacity="0"/>
        </radialGradient>

        <pattern id="grid" width="44" height="44" patternUnits="userSpaceOnUse">
          <path d="M44 0H0V44" fill="none" stroke="{CY}" stroke-opacity="0.07" stroke-width="1"/>
        </pattern>

        <filter id="soft" x="-30%" y="-30%" width="160%" height="160%">
          <feGaussianBlur stdDeviation="5"/>
        </filter>

        <clipPath id="frame"><rect width="{W}" height="{H}" rx="16"/></clipPath>
      </defs>

      <style>
        .ltr {{
          font: 800 92px ui-monospace, 'SFMono-Regular', 'Fira Code', Consolas, monospace;
          fill: url(#ink); letter-spacing: 2px;
          opacity: 0; animation: rise 0.9s cubic-bezier(.2,.8,.2,1) forwards;
        }}
        .tag {{
          font: 500 19px ui-monospace, 'Fira Code', Consolas, monospace; fill: {MU};
          opacity: 0; animation: fade 1s ease-out 0.75s forwards;
        }}
        .chip {{ opacity: 0; animation: rise 0.7s cubic-bezier(.2,.8,.2,1) forwards; }}
        .chip-t {{ font: 500 12.5px ui-monospace, 'Fira Code', Consolas, monospace; }}
        @keyframes rise {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: translateY(0); }} }}
        @keyframes fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
      </style>

      <g clip-path="url(#frame)">
        <rect width="{W}" height="{H}" fill="url(#sky)"/>

        <!-- grid drifting up-left, one tile per cycle so the loop is seamless -->
        <g opacity="0.9">
          <rect x="-44" y="-44" width="{W+88}" height="{H+88}" fill="url(#grid)">
            <animateTransform attributeName="transform" type="translate"
              values="0 0; -44 -44" dur="16s" repeatCount="indefinite"/>
          </rect>
        </g>

        {stars}

        <ellipse cx="150" cy="120" rx="320" ry="150" fill="url(#halo)"/>
        <ellipse cx="1040" cy="240" rx="300" ry="150" fill="url(#halo)" opacity="0.5"/>

        <!-- wordmark, with a glow pass behind it -->
        <g filter="url(#soft)" opacity="0.32">
        {letters}
        </g>
        {letters}

        <!-- light sweeping across the wordmark -->
        <rect x="-300" y="0" width="260" height="{H}" fill="url(#sweep)" opacity="0.40">
          <animate attributeName="x" values="-300;{W}" dur="6.5s" begin="1.6s" repeatCount="indefinite"/>
        </rect>

        <path d="M40 186 H760" stroke="url(#rule)" stroke-width="2" fill="none">
          <animate attributeName="opacity" values="0.45;1;0.45" dur="4s" repeatCount="indefinite"/>
        </path>

        <text class="tag" x="42" y="214">tinkerer &#183; modder &#183; reverse engineer &#183; breaker of things</text>

        {chip_svg}

        <!-- scanline -->
        <rect x="0" y="0" width="{W}" height="2" fill="{CY}" opacity="0.16">
          <animate attributeName="y" values="-4;{H}" dur="7s" repeatCount="indefinite"/>
        </rect>

        <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="16" fill="none"
          stroke="{CY}" stroke-opacity="0.22"/>
      </g>
    </svg>
    '''
    return hero


# ============================================================== now.svg
def build_now():
    W, H = 1200, 232
    lines = [
        ("$", "now", CY, None),
        ("→", "Switch-Theme-Installer", RD, "k-means palette extraction, running on the console itself, in C"),
        ("→", "switch-rom-forwarder", PU, "HOME-menu forwarders built on-device — no PC in the loop"),
        ("→", "Theme-App 2.1.0", CY, "two editors, one brand, desktop build cut by CI"),
        ("→", "dinner-by-derek", OC, "a supper club that runs off a phone. no Switch in sight"),
    ]
    CYCLE = 22.0          # whole loop
    TYPE = 1.5            # seconds to type one line
    START = 1.0           # first line starts here
    GAP = 1.9             # between line starts

    rows, clips = [], []
    y = 92
    for i, (sigil, label, col, rest) in enumerate(lines):
        t0 = START + i * GAP
        a, b = t0 / CYCLE, (t0 + TYPE) / CYCLE
        full = 1140
        clips.append(
            f'<clipPath id="t{i}"><rect x="30" y="{y-20}" height="30" width="0">'
            f'<animate attributeName="width" dur="{CYCLE}s" repeatCount="indefinite" '
            f'calcMode="linear" keyTimes="0;{a:.4f};{b:.4f};0.965;1" '
            f'values="0;0;{full};{full};0"/></rect></clipPath>'
        )
        x = 34
        row = [f'<text class="sig" x="{x}" y="{y}" fill="{col}">{esc(sigil)}</text>']
        x += 26
        row.append(f'<text class="lbl" x="{x}" y="{y}" fill="{col}">{esc(label)}</text>')
        if rest:
            x += adv(label, 16) + 20
            row.append(f'<text class="rest" x="{x:.0f}" y="{y}">{esc(rest)}</text>')
        rows.append(f'<g clip-path="url(#t{i})">' + "".join(row) + "</g>")
        y += 32

    # cursor parks at the end of each line as it finishes
    cur_keytimes, cur_x, cur_y = ["0"], ["34"], ["72"]
    for i, (sigil, label, col, rest) in enumerate(lines):
        t0 = START + i * GAP
        lw = 34 + 26 + adv(label, 16) + ((20 + adv(rest, 13.5)) if rest else 0)
        ly = 92 + i * 32
        cur_keytimes += [f"{t0/CYCLE:.4f}", f"{(t0+TYPE)/CYCLE:.4f}"]
        cur_x += [f"{34}", f"{lw:.0f}"]
        cur_y += [f"{ly-15}", f"{ly-15}"]
    cur_keytimes.append("1"); cur_x.append(f"{lw:.0f}"); cur_y.append(f"{ly-15}")
    cursor = (
        f'<rect width="10" height="19" fill="{CY}" opacity="0.9">'
        f'<animate attributeName="x" dur="{CYCLE}s" repeatCount="indefinite" '
        f'keyTimes="{";".join(cur_keytimes)}" values="{";".join(cur_x)}"/>'
        f'<animate attributeName="y" dur="{CYCLE}s" repeatCount="indefinite" '
        f'calcMode="discrete" keyTimes="{";".join(cur_keytimes)}" values="{";".join(cur_y)}"/>'
        f'<animate attributeName="opacity" values="0.95;0.05;0.95" dur="1.1s" repeatCount="indefinite"/>'
        f'</rect>'
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
  width="{W}" height="{H}" role="img" aria-labelledby="nowTitle nowDesc">
  <title id="nowTitle">Now building</title>
  <desc id="nowDesc">A terminal panel that types out four current projects: Switch-Theme-Installer (k-means palette extraction on the console, in C), switch-rom-forwarder (HOME menu forwarders built on-device), Theme-App 2.1.0 (two editors, desktop build cut by CI), and dinner-by-derek (a supper club that runs off a phone).</desc>
  <defs>
    {grid_def("gnow", CY, 40, 0.05)}
    <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{CY}"/><stop offset="0.5" stop-color="{PU}"/>
      <stop offset="1" stop-color="{RD}"/>
    </linearGradient>
    <clipPath id="nowframe"><rect width="{W}" height="{H}" rx="14"/></clipPath>
    {"".join(clips)}
  </defs>
  <style>
    .sig  {{ font: 700 16px {MONO}; }}
    .lbl  {{ font: 700 16px {MONO}; }}
    .rest {{ font: 400 13.5px {MONO}; fill: {MU}; }}
    .hd   {{ font: 600 12.5px {MONO}; fill: {DIM}; }}
  </style>
  <g clip-path="url(#nowframe)">
    <rect width="{W}" height="{H}" fill="{PANEL}"/>
    <rect width="{W}" height="{H}" fill="url(#gnow)"/>
    <rect width="{W}" height="34" fill="#0a1220"/>
    <circle cx="22" cy="17" r="5" fill="{RD}" opacity="0.85"/>
    <circle cx="40" cy="17" r="5" fill="{OC}" opacity="0.85"/>
    <circle cx="58" cy="17" r="5" fill="{GR}" opacity="0.85"/>
    <text class="hd" x="80" y="21">aramaki@workbench: ~/what-im-on-right-now</text>
    <rect y="34" width="{W}" height="2" fill="url(#bar)" opacity="0.7"/>
    {"".join(rows)}
    {cursor}
    <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none"
      stroke="{EDGE}" stroke-width="1"/>
  </g>
</svg>
'''


# ============================================================ pipeline.svg
def build_pipeline():
    W, H = 1200, 478

    def box(x, y, w, h, col, title, sub, note=None):
        g = [f'<g transform="translate({x},{y})">']
        g.append(f'<rect width="{w}" height="{h}" rx="10" fill="{PANEL}" stroke="{col}" stroke-opacity="0.55"/>')
        g.append(f'<rect width="4" height="{h}" rx="2" fill="{col}" opacity="0.85"/>')
        g.append(f'<circle cx="{w-16}" cy="16" r="4" fill="{col}">'
                 f'<animate attributeName="opacity" values="1;0.2;1" dur="3s" repeatCount="indefinite"/></circle>')
        g.append(f'<text class="bt" x="18" y="27" fill="{col}">{esc(title)}</text>')
        g.append(f'<text class="bs" x="18" y="48">{esc(sub)}</text>')
        if note:
            g.append(f'<text class="bn" x="18" y="68">{esc(note)}</text>')
        g.append("</g>")
        return "".join(g)

    def wire(idx, d, col, dots=3, dur=3.4, label=None, lx=0, ly=0):
        out = [f'<path id="w{idx}" d="{d}" fill="none" stroke="{col}" stroke-opacity="0.38" '
               f'stroke-width="1.6" stroke-dasharray="5 5"/>']
        for k in range(dots):
            out.append(
                f'<circle r="3.4" fill="{col}">'
                f'<animateMotion dur="{dur}s" begin="{k*dur/dots:.2f}s" repeatCount="indefinite" '
                f'keyPoints="0;1" keyTimes="0;1" calcMode="linear">'
                f'<mpath xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#w{idx}"/>'
                f'</animateMotion>'
                f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.12;0.88;1" '
                f'dur="{dur}s" begin="{k*dur/dots:.2f}s" repeatCount="indefinite"/></circle>')
        if label:
            out.append(f'<text class="wl" x="{lx}" y="{ly}">{esc(label)}</text>')
        return "".join(out)

    parts = []
    # ---- tier 1: the editors
    parts.append(box(400, 40, 400, 78, CY, "Theme-App  ·  the editors",
                     "browser  ·  installable PWA  ·  Windows desktop",
                     "two editors, one launcher, one codebase"))
    # ---- tier 2: the databases
    parts.append(box(120, 210, 380, 78, GR, "Tinfoil-Themes",
                     f"themes.json  ·  {TINFOIL_COUNT} entries",
                     "served from GitHub Pages"))
    parts.append(box(700, 210, 380, 78, PU, "RomM-Themes",
                     f"manifest.json  ·  {ROMM_COUNT} themes  ·  19 roles",
                     "every submission validated in CI"))
    # ---- tier 3: the consoles
    parts.append(box(120, 372, 380, 62, RD, "Switch-Theme-Installer",
                     ".nro  ·  C  ·  devkitA64 / libnx / SDL2"))
    parts.append(box(700, 372, 380, 62, PU, "RomM Switch client",
                     "SDL2 homebrew  ·  reads a folder on the SD card"))

    # ---- wires: editors -> databases
    parts.append(wire(1, "M540 118 C 440 160, 330 160, 310 210", CY, 3, 3.2,
                      "exports settings.json", 392, 202))
    parts.append(wire(2, "M660 118 C 760 160, 870 160, 890 210", CY, 3, 3.2,
                      "exports a theme.json or a .zip pack", 596, 202))
    # ---- wires: databases -> editors (the catalog read, going back up)
    parts.append(wire(3, "M250 210 C 200 150, 300 128, 420 118", GR, 2, 4.2,
                      "browse the live catalog, in-app", 96, 126))
    parts.append(wire(4, "M950 210 C 1000 150, 900 128, 780 118", PU, 2, 4.2,
                      "opens a published theme, assets and all", 866, 126))
    # ---- wires: databases -> consoles
    parts.append(wire(5, "M310 288 L 310 372", GR, 2, 2.6,
                      "read live over the console's own network stack", 330, 330))
    parts.append(wire(6, "M890 288 L 890 372", PU, 2, 2.6,
                      "the same manifest the console reads", 700, 330))

    legend = (
        f'<g transform="translate(40,{H-14})">'
        f'<circle cx="0" cy="-4" r="3.4" fill="{CY}"/>'
        f'<text class="lg" x="12" y="0">data actually moving — every arrow here is a shipped code path</text>'
        f'</g>'
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
  width="{W}" height="{H}" role="img" aria-labelledby="pipeTitle pipeDesc">
  <title id="pipeTitle">How the A-Theme project fits together</title>
  <desc id="pipeDesc">A system map. Theme-App (browser, PWA and Windows desktop) exports themes into two databases: Tinfoil-Themes (themes.json, {TINFOIL_COUNT} entries, served from GitHub Pages) and RomM-Themes (manifest.json, {ROMM_COUNT} themes, 19 colour roles, validated in CI). Both databases are browsable from inside the editors, and both are read on the console itself: Tinfoil-Themes by Switch-Theme-Installer, a C homebrew .nro, and RomM-Themes by the RomM Switch client.</desc>
  <defs>
    {grid_def("gpipe", CY, 40, 0.045)}
    <clipPath id="pipeframe"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  </defs>
  <style>
    .bt {{ font: 700 15px {MONO}; }}
    .bs {{ font: 400 12.5px {MONO}; fill: {MU}; }}
    .bn {{ font: 400 11.5px {MONO}; fill: {DIM}; }}
    .wl {{ font: 400 11px {MONO}; fill: {DIM}; }}
    .lg {{ font: 400 11.5px {MONO}; fill: {DIM}; }}
    .tier {{ font: 700 11px {MONO}; fill: {DIM}; letter-spacing: 2px; }}
  </style>
  <g clip-path="url(#pipeframe)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <rect width="{W}" height="{H}" fill="url(#gpipe)"/>
    <text class="tier" x="40" y="84">AUTHOR</text>
    <text class="tier" x="40" y="196">PUBLISH</text>
    <text class="tier" x="40" y="358">CONSOLE</text>
    {"".join(parts)}
    {legend}
    <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none"
      stroke="{EDGE}"/>
  </g>
</svg>
'''


# =============================================================== cards
def build_card(fname, accent, title, status, desc, tags, glyph_kind):
    W, H = 580, 186
    tagsvg, tx = [], 22
    for label, col in tags:
        w = max(42, int(adv(label, 11)) + 26)
        tagsvg.append(
            f'<g transform="translate({tx},{H-42})">'
            f'<rect width="{w}" height="24" rx="12" fill="{col}" fill-opacity="0.11" '
            f'stroke="{col}" stroke-opacity="0.45"/>'
            f'<text class="tg" x="{w/2:.0f}" y="16" fill="{col}" text-anchor="middle">{esc(label)}</text></g>')
        tx += w + 9

    sw = int(adv(status, 11)) + 24

    # the glyph lives in the header strip, immediately left of the status pill,
    # so it can never collide with a description line
    gx = W - sw - 18 - (46 if glyph_kind == "wave" else 42)
    glyph = (f'<g transform="translate({gx},25)">'
             + (wave_glyph(accent) if glyph_kind == "wave" else dots_glyph(accent))
             + '</g>')

    # guard: a description line wider than the card is a layout bug, not a typo
    for line in desc:
        assert adv(line, 12.5) <= W - 44, f"{fname}: line too wide ({len(line)} chars): {line}"
    title_end = 22 + adv(title, 19)
    assert title_end < gx, f"{fname}: title runs into the header glyph"
    lines = "".join(
        f'<text class="cd" x="22" y="{96 + i*20}">{esc(l)}</text>' for i, l in enumerate(desc))

    body = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
  width="{W}" height="{H}" role="img" aria-labelledby="ct cd">
  <title id="ct">{esc(title)}</title>
  <desc id="cd">{esc(title)} — {esc(status)}. {esc(" ".join(desc))} Built with: {esc(", ".join(t for t, _ in tags))}.</desc>
  <defs>
    {grid_def("gc", accent, 34, 0.05)}
    <linearGradient id="edge" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{accent}" stop-opacity="0.15"/>
      <stop offset="0.5" stop-color="{accent}" stop-opacity="1"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0.15"/>
    </linearGradient>
    <linearGradient id="gloss" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0"/>
      <stop offset="0.5" stop-color="#ffffff" stop-opacity="0.055"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="cf"><rect width="{W}" height="{H}" rx="12"/></clipPath>
  </defs>
  <style>
    .ch {{ font: 700 19px {MONO}; fill: {accent}; }}
    .cs {{ font: 700 11px {MONO}; fill: {accent}; }}
    .cd {{ font: 400 12.5px {MONO}; fill: {MU}; }}
    .tg {{ font: 600 11px {MONO}; }}
    .in {{ opacity: 0; animation: cin .8s cubic-bezier(.2,.8,.2,1) forwards; }}
    @keyframes cin {{ from {{ opacity: 0 }} to {{ opacity: 1 }} }}
  </style>
  <g clip-path="url(#cf)">
    <rect width="{W}" height="{H}" fill="{PANEL}"/>
    <rect width="{W}" height="{H}" fill="url(#gc)"/>

    <!-- left edge, breathing -->
    <rect width="4" height="{H}" fill="url(#edge)">
      <animate attributeName="opacity" values="0.55;1;0.55" dur="4.5s" repeatCount="indefinite"/>
    </rect>

    <!-- slow gloss sweep -->
    <rect x="-240" y="0" width="240" height="{H}" fill="url(#gloss)">
      <animate attributeName="x" values="-240;{W}" dur="9s" begin="2s" repeatCount="indefinite"/>
    </rect>

    <g class="in">
      {glyph}
      <text class="ch" x="22" y="46">{esc(title)}</text>
      <g transform="translate({W - sw - 18},26)">
        <rect width="{sw}" height="22" rx="11" fill="{accent}" fill-opacity="0.14"
          stroke="{accent}" stroke-opacity="0.5"/>
        <text class="cs" x="{sw/2:.0f}" y="15" text-anchor="middle">{esc(status)}</text>
      </g>
      <path d="M22 60 H {W-22}" stroke="{accent}" stroke-opacity="0.18" stroke-width="1"/>
      {lines}
      {"".join(tagsvg)}
    </g>
    <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none"
      stroke="{accent}" stroke-opacity="0.28"/>
  </g>
</svg>
'''
    write(fname, body)


def dots_glyph(col, cx=0, cy=0):
    """A small 3x3 matrix that ripples -- reads as 'a grid of themes'."""
    out = []
    for r in range(3):
        for c in range(3):
            i = r * 3 + c
            out.append(
                f'<rect x="{cx + c*9}" y="{cy + r*9}" width="6" height="6" rx="1.5" fill="{col}">'
                f'<animate attributeName="opacity" values="0.25;1;0.25" dur="2.8s" '
                f'begin="{i*0.16:.2f}s" repeatCount="indefinite"/></rect>')
    return "".join(out)


def wave_glyph(col, cx=0, cy=0):
    bars = []
    for i in range(5):
        h = [10, 18, 24, 16, 8][i]
        bars.append(
            f'<rect x="{cx + i*7}" y="{cy + 24 - h}" width="4" height="{h}" rx="2" fill="{col}">'
            f'<animate attributeName="height" values="{h};{max(4, h//2)};{h}" dur="{1.6 + i*0.2:.1f}s" '
            f'repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{cy+24-h};{cy+24-max(4, h//2)};{cy+24-h}" '
            f'dur="{1.6 + i*0.2:.1f}s" repeatCount="indefinite"/></rect>')
    return "".join(bars)


print("writing profile assets:")
write("hero.svg", build_hero())
write("now.svg", build_now())
write("pipeline.svg", build_pipeline())

CARDS = [
    ("card-theme-app.svg", CY, "Theme-App", "v2.1.0",
     ["Two visual editors — Tinfoil's settings.json and the RomM client's",
      "theme.json — in a browser, as an installable PWA, and as a Windows",
      "desktop build the release workflow cuts on every tag."],
     [("HTML/JS", CY), ("Electron", PU), ("PWA", GR), ("no build step", DIM)],
     "dots"),

    ("card-installer.svg", RD, "Switch-Theme-Installer", "native C",
     ["A .nro that runs on the console itself. Browses the live database over",
      "the Switch's own network stack, previews a theme with SDL2, and runs",
      "k-means palette extraction on-device, rewriting the JSON in place."],
     [("C", RD), ("devkitA64 / libnx", CY), ("SDL2", PU), ("zziplib · jsmn", DIM)],
     "wave"),

    ("card-forwarder.svg", PU, "switch-rom-forwarder", "new · early",
     ["HOME-menu forwarders for retro games, generated on the console with no",
      "PC in the loop. CRC32 against No-Intro DATs to recover real titles,",
      "libretro box art, and a diff of every source before it touches a thing."],
     [("nx.js", PU), ("JavaScript", CY), ("NSP", RD), ("no devkitPro", DIM)],
     "wave"),

    ("card-romm-themes.svg", GR, "RomM-Themes", f"{ROMM_COUNT} themes",
     ["Themes for the RomM Switch client: 19 semantic colour roles,",
      "backgrounds with free drift/pan/zoom motion, sprite-sheet animation,",
      "a replacement font, mascot art, music \u2014 and CI validates every one."],
     [("JSON", GR), ("19 roles", CY), ("CI-validated", PU), ("contrast-checked", DIM)],
     "dots"),

    ("card-tinfoil-themes.svg", CY, "Tinfoil-Themes", f"{TINFOIL_COUNT} entries",
     ["The database everything else reads — community and original Tinfoil",
      "themes, served straight off GitHub Pages and browsable from inside",
      "the editor and from the console, without leaving either one."],
     [("JSON", CY), ("GitHub Pages", GR), ("170+ themes", PU), ("secret-scanned", DIM)],
     f'<g transform="translate(516,120)">{dots_glyph(CY)}</g>'),

    ("card-dinner.svg", OC, "dinner-by-derek", "new · not a Switch",
     ["An installable ordering app for a supper club: no app store, no",
      "accounts, no online payment — a site that installs to a home screen.",
      "One-file SQLite, measured WCAG contrast, print cards at 300 DPI."],
     [("Node 20", GR), ("Express 5", OC), ("SQLite", CY), ("PWA", PU)],
     "dots"),
]
for c in CARDS:
    build_card(*c)


# ============================================================== footer.svg
def build_footer():
    W, H = 1200, 152
    waves = []
    for i, (col, op, dur, amp, yb) in enumerate([
            (CY, 0.55, 9, 20, 96), (PU, 0.45, 11, 26, 110), (RD, 0.35, 13, 16, 124)]):
        d = (f"M-1200 {yb} "
             f"C -1000 {yb-amp}, -800 {yb+amp}, -600 {yb} "
             f"C -400 {yb-amp}, -200 {yb+amp}, 0 {yb} "
             f"C 200 {yb-amp}, 400 {yb+amp}, 600 {yb} "
             f"C 800 {yb-amp}, 1000 {yb+amp}, 1200 {yb} "
             f"C 1400 {yb-amp}, 1600 {yb+amp}, 1800 {yb} "
             f"C 2000 {yb-amp}, 2200 {yb+amp}, 2400 {yb}")
        waves.append(
            f'<g><path d="{d}" fill="none" stroke="{col}" stroke-opacity="{op}" stroke-width="2"/>'
            f'<animateTransform attributeName="transform" type="translate" '
            f'values="0 0; 1200 0" dur="{dur}s" repeatCount="indefinite"/></g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
  width="{W}" height="{H}" role="img" aria-labelledby="ftTitle ftDesc">
  <title id="ftTitle">Got a config file? Talk to me.</title>
  <desc id="ftDesc">Animated footer: three coloured waves rolling under the line "got a config file, a locked bootloader, or a UI begging to be re-themed?".</desc>
  <defs><clipPath id="ff"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>
  <style>
    .f1 {{ font: 700 22px {MONO}; fill: {TX}; }}
    .f2 {{ font: 400 13.5px {MONO}; fill: {DIM}; }}
  </style>
  <g clip-path="url(#ff)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    {"".join(waves)}
    <text class="f1" x="{W//2}" y="48" text-anchor="middle">got a config file?</text>
    <text class="f2" x="{W//2}" y="74" text-anchor="middle">a locked bootloader, or a UI that is begging to be re-themed? talk to me.</text>
    <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="none" stroke="{EDGE}"/>
  </g>
</svg>
'''

write("footer.svg", build_footer())
print("done")
