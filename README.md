<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff3c50,50:9d4edd,100:00c2ff&height=220&section=header&text=ARAMAKI&fontSize=80&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=tinkerer%20%C2%B7%20modder%20%C2%B7%20breaker%20of%20things&descAlignY=58&descSize=20" width="100%"/>

<img src="https://raw.githubusercontent.com/A-Theme/Theme-App/main/assets/logo.png" width="90" height="90" alt="A-Theme logo"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=00C2FF&center=true&vCenter=true&width=680&lines=If+it+has+a+config+file%2C+I'm+opening+it.;Breaking+things+to+understand+them+since+forever.;Currently%3A+reverse-engineering+Tinfoil's+theme+format.;Currently%3A+writing+native+C+for+a+console+that+says+no.;Give+me+read+access+and+ten+minutes.)](https://git.io/typing-svg)

<p>
  <img src="https://komarev.com/ghpvc/?username=Aramaki&label=Profile+Views&color=00c2ff&style=for-the-badge" alt="profile views"/>
  <img src="https://img.shields.io/github/followers/Aramaki?label=Followers&style=for-the-badge&color=ff3c50" alt="followers"/>
  <img src="https://img.shields.io/badge/status-tinkering-9d4edd?style=for-the-badge" alt="status"/>
</p>

</div>

---

## 👋 About Me

I'm a **tinkerer** — the kind of person who sees a settings file, a locked-down console, or a UI I didn't design and thinks *"okay, but what if I opened this up."* Coding, modding, hacking, reverse-engineering, reflashing, rebuilding — if it can be taken apart and understood, I'm interested. I don't stick to one platform or one language; I go wherever the interesting problem is.

Lately that's meant living inside **Tinfoil's theme format** — figuring out exactly how `theme.json` works down to the hex digit, then building real tools around it across every surface I could think of: browser, desktop, mobile, and eventually the Nintendo Switch itself, natively, in C.

```
whoami
> Aramaki — builder of tools nobody asked for but everyone ends up using
interests
> coding · modding · hacking · homebrew · reverse engineering · "let's see what's inside"
currently
> teaching a Switch homebrew app to generate color palettes from an image, on-device
```

---

## 🎨 What I've Been Building — The A-Theme Project

A full pipeline for creating, browsing, and installing Tinfoil themes — three tools, one shared theme database, built from scratch across three very different platforms.

<div align="center">

[![Theme-App](https://github-readme-stats.vercel.app/api/pin/?username=A-Theme&repo=Theme-App&theme=radical&hide_border=true&bg_color=0b1420)](https://github.com/A-Theme/Theme-App)
[![Switch-Theme-Installer](https://github-readme-stats.vercel.app/api/pin/?username=A-Theme&repo=Switch-Theme-Installer&theme=radical&hide_border=true&bg_color=0b1420)](https://github.com/A-Theme/Switch-Theme-Installer)

[![Tinfoil-Themes](https://github-readme-stats.vercel.app/api/pin/?username=A-Theme&repo=Tinfoil-Themes&theme=radical&hide_border=true&bg_color=0b1420)](https://github.com/A-Theme/Tinfoil-Themes)

</div>

### 🖥️ [Theme-App](https://github.com/A-Theme/Theme-App) — the visual editor
A full theme.json GUI editor that runs as a browser app, an installable mobile PWA, *and* a Windows desktop app — all from one codebase. The newest stuff:

- **Browse the entire live theme database from inside the app** and load one with a click — it downloads and unzips the theme's archive **entirely client-side** (real embedded JSZip, no server involved) and wires up every bundled logo/background/audio file automatically
- **Palette generation via real k-means color clustering**, extracted straight from your background image — not a gimmick, actual dominant-color math
- **A live, pixel-accurate mockup preview** of the real Tinfoil layout, where every visible piece is hoverable and clickable — hover a selection tile, it tells you exactly which JSON field controls it; click it, and the form scrolls straight to that field and highlights it
- Full alpha/transparency support with a visual slider and diagram, because hex color formats are not intuitive and I got tired of explaining them

### 🎮 [Switch-Theme-Installer](https://github.com/A-Theme/Switch-Theme-Installer) — native homebrew, on the console itself
This is the one I'm most proud of. A native C application (`.nro`) that runs *directly on a Nintendo Switch* — no PC required:

- Reads the theme database live over Switch's own networking stack, browsable with a controller
- Real device rendering via SDL2 — an actual on-screen preview of a theme's colors and layout before you commit to installing it
- **Runs the same k-means palette extraction as the browser app, but on-device** — reads raw pixels out of a decoded image on the Switch itself and rewrites the theme's JSON in place, byte-for-byte, no serializer needed
- Built the hard way: real devkitA64/libnx toolchain, zip extraction via `zziplib`, JSON parsing via a hand-verified `jsmn` integration, iterated through multiple real hardware test-and-fix cycles until it actually ran clean

### 🌈 [Tinfoil-Themes](https://github.com/A-Theme/Tinfoil-Themes) — the database itself
150+ community and original themes, serving as the shared backbone every other tool in this project reads from.

---

## 🛠️ Tech I Reach For

<div align="center">

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![C](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)
![Electron](https://img.shields.io/badge/Electron-191970?style=for-the-badge&logo=electron&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

![Nintendo Switch Homebrew](https://img.shields.io/badge/Switch%20Homebrew-devkitA64%20%2F%20libnx-e60012?style=for-the-badge&logo=nintendoswitch&logoColor=white)
![SDL2](https://img.shields.io/badge/SDL2-Graphics-1a1a2e?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![PWA](https://img.shields.io/badge/PWA-Installable-5A0FC8?style=for-the-badge&logo=pwa&logoColor=white)

</div>

---

## 📊 The Numbers

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=Aramaki&show_icons=true&theme=radical&hide_border=true&bg_color=0b1420&title_color=00c2ff&icon_color=ff3c50&text_color=eaf1fa" height="165"/>
<img src="https://github-readme-streak-stats.herokuapp.com/?user=Aramaki&theme=radical&hide_border=true&background=0b1420&stroke=00c2ff&ring=ff3c50&fire=ff3c50&currStreakLabel=00c2ff" height="165"/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Aramaki&layout=compact&theme=radical&hide_border=true&bg_color=0b1420&title_color=00c2ff&text_color=eaf1fa" height="165"/>

</div>

<div align="center">
<img src="https://github-profile-trophy.vercel.app/?username=Aramaki&theme=radical&no-frame=true&no-bg=true&margin-w=8&row=1" />
</div>

---

## 🐍 Contribution Snake

<!-- To make this animate for real: add the platane/snk GitHub Action to this
     repo (github.com/Platane/snk), configure it with github_user_name: Aramaki
     so it tracks your personal contribution graph, and it'll generate and
     commit the SVGs below to this repo's `output` branch automatically. -->
<div align="center">
<img src="https://raw.githubusercontent.com/A-Theme/A-Theme/output/github-contribution-grid-snake-dark.svg" width="100%"/>
</div>

---

## 💬 Find Me

<div align="center">

[![Discord](https://img.shields.io/badge/Discord-A--Theme%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/xW7TMkgkH)
[![Website](https://img.shields.io/badge/Web-a--theme.ca-ff3c50?style=for-the-badge&logo=googlechrome&logoColor=white)](https://a-theme.ca)
[![GitHub Org](https://img.shields.io/badge/GitHub-A--Theme-00c2ff?style=for-the-badge&logo=github&logoColor=white)](https://github.com/A-Theme)

</div>

<div align="center">

*Got a config file? A locked bootloader? A UI that's begging to be re-themed? Talk to me.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00c2ff,50:9d4edd,100:ff3c50&height=120&section=footer" width="100%"/>

</div>
