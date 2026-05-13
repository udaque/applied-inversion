# Applied Inversion

A browser-based image **inversion** tool. Upload a photo, pick the center and radius of an inversion circle, and watch the planar inversion render in real time. Compose multiple circles for a full Möbius transformation, and use the built-in visualizations to see the group structure and even Apollonian-style fractals that fall out of it.

> **Inversion** — Given a point *O* and a radius *r* in the plane, every point *P* (≠ *O*) is mapped to the point *Q* on the ray *OP* that satisfies *OP · OQ = r²*.

🇰🇷 한국어 README는 [README.md](./README.md)를 참고하세요.

**Version 0.3** — see [CHANGELOG.md](./CHANGELOG.md) for per-version changes.

---

## ✨ Features at a glance

### Core
- 🖼 **Image upload** — file picker, click/tap the empty drop area, drag-and-drop anywhere on the page, or Ctrl/⌘+V from clipboard
- 🎯 **Inversion circle controls** — click/tap, drag, or type numbers. Drag inside the active circle pans it, drag the dashed edge resizes (cursor rotates with angle)
- 🔁 **Multiple inversion circles** — compose σ_N ∘ … ∘ σ_1, with an active indicator and number labels
- ⚡ **Real-time result** rendered in a Web Worker so the main thread stays responsive
- 🔍 **Zoom & pan on the result canvas** — wheel/pinch, drag, double-click/double-tap to reset, automatic hi-res re-render once the view settles

### Advanced options (organized into three sections)
**Image**
- Strength slider — linear blend between the original and the full inversion
- Fill — black / white / custom / transparent / **edge clamp** (default)
- Sampling — Nearest / **Bilinear** (default)

**Visualization**
- Grid overlay — the source's straight grid drawn on the result through the full composed transformation
- Group exploration — with exactly two circles, classifies the composition as Elliptic / Parabolic / Hyperbolic, draws fixed points, axis, and seed orbits

**I/O**
- Presets — save up to five named configurations to `localStorage`, with JSON export / import for backup or sharing
- Save format — PNG / JPEG / WEBP
- Save at original resolution — re-render from the full source instead of the on-screen preview

### Save / share
- 💾 PNG / JPEG / WEBP export; mobile routes through the Web Share sheet to the Photos library
- 📤 Share buttons — Bluesky · X · Threads · Instagram · device share · copy link
- 🌐 **URL hash** — the full configuration is encoded in `#…`, so the URL is a shareable composition link
- 💽 **Refresh recovery** — last image in IndexedDB, settings mirrored to localStorage

### Other
- 🌏 Korean / English language toggle
- ⏪ Undo / Redo (Ctrl/⌘ Z, Ctrl/⌘ ⇧ Z)
- 📱 Installable PWA (offline-capable)
- ⓘ Info modals on every option and beside the page title explain the math and the meaning of each visual element

---

## 🚀 Getting started

It's a single static HTML file — no build step.

### 1. Open directly
Clone the repo and open `index.html` in your browser.

### 2. Local server (recommended)
```bash
git clone https://github.com/udaque/applied-inversion.git
cd applied-inversion
python3 -m http.server 8000
# or: npx serve .
```
Then visit `http://localhost:8000/`.

> Web Share, image clipboard, and "save to Photos" only work on **HTTPS or localhost**.

### 3. GitHub Pages
Repo **Settings → Pages**, pick a branch, and the public URL appears in a minute.

---

## 📐 The math

Given center *O = (cx, cy)* and radius *r*, the source coordinate for an output pixel *Q = (x, y)* is

```
d² = (x - cx)² + (y - cy)²
P  = O + (Q - O) · (r² / d²)
```

- *d² ≈ 0* (close to the center): source goes to infinity → undefined region
- *P* outside the image: also undefined (or clamped to the edge)
- Otherwise: sample at *P* via Bilinear or Nearest

Composing N circles applies N inversions in sequence; for N = 2 the result is a general Möbius transformation, classified as Elliptic / Parabolic / Hyperbolic by how the two circles intersect (or don't).

**Inverse of a grid line**: A horizontal line `y = b` with `b ≠ cy` maps to the circle through the inversion center with center `(cx, cy + r²/(2(b-cy)))` and radius `r²/(2|b-cy|)`. Lines through the center map to themselves.

Detailed math is available behind the ⓘ next to the page title and beside each advanced option.

---

## 🛠 Tips

- **Fine tuning**: use the mouse/touch to get close, then dial in X% / Y% / radius numerically
- **Save formats**: PNG or WEBP preserves alpha; JPEG composites onto white. iOS Photos library only accepts PNG / JPEG / HEIC (WEBP will go through Files instead).
- **Presets**: storing a preset captures the composition (% positions), not the pixels, so the same composition applies to any image
- **Share links**: copying the URL lets a recipient open the same composition; they upload their own image

---

## 📂 Structure

```
applied-inversion/
├── index.html             # the whole app
├── sw.js                  # service worker (PWA)
├── manifest.webmanifest
├── icons/                 # PWA icons + generate.py
├── CHANGELOG.md           # per-version changes
├── README.md              # Korean
└── README.en.md           # English (this file)
```

No dependencies — no package manager, no build tooling, no external scripts.

---

## 👤 Author

[udaque](https://bsky.app/profile/udaqueness.blog)

---

## 📜 License

MIT
