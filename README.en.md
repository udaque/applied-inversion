# Applied Inversion

A browser-based image **inversion** tool. Upload a photo, pick the center and radius of an inversion circle, and watch the planar inversion of the image render in real time.

> **Inversion** — Given a point *O* and a radius *r* in the plane, every point *P* (≠ *O*) is mapped to the point *Q* on the ray *OP* that satisfies *OP · OQ = r²*.

🇰🇷 한국어 README는 [README.md](./README.md)를 참고하세요.

---

## ✨ Features

### Core
- 🖼 **Image upload** — pick a file or click/tap the empty drop area
- 🎯 **Inversion-circle controls**
  - Click/tap the canvas to jump the center
  - Drag the center to reposition, drag the dashed edge to resize
  - Type center X/Y (% of width/height) and radius (px) by hand
- ⚡ **Live result** — Web Worker + OffscreenCanvas keep the main thread responsive
- 🔍 **Zoom & pan on the result canvas**
  - Desktop: wheel zoom around the cursor, drag to pan, double-click to reset
  - Mobile: pinch zoom, one-finger drag, double-tap to reset

### Advanced options
- 🎨 **Undefined-region fill** — black / white / custom color / transparent / **edge clamp** (sample the nearest in-bounds source pixel)
- 🪡 **Sampling** — Nearest (fast) or **Bilinear** (smooth, default)
- 💾 **Save at original resolution** — the preview is capped at 900px for speed, but exports re-render at the full source resolution
- 📐 **Grid overlay** — draws a fixed white Cartesian grid on the source and its inverse image (circles through the inversion center) on the result. The grid pitch is configurable.

### Save / share
- 💾 **Save** as PNG / JPEG / WEBP
  - On mobile, the Web Share API routes the image to "Save to Photos / 사진에 저장"
- 📤 **Share to Bluesky / X / Threads / Instagram / device / clipboard link**
  - Bluesky, X, and Threads open their compose view in a new tab (or app, via universal links) with the post text prefilled; the rendered image is copied to the clipboard in the background so you can paste it
  - On mobile with Web Share, the OS share sheet opens directly
  - An "Include current settings" toggle decides whether the URL contains the configuration hash

### Persistence
- 🌐 **URL hash** — every setting (center as %, radius as % of the shorter side, sampling, fill mode, grid, zoom & pan, language) is encoded in `#…`. Copy the URL to share the exact composition.
- 💽 **Refresh recovery** — the last image is stored in IndexedDB and the settings mirror to localStorage. Reload and it all comes back.
- 🌏 **Korean / English toggle** — header selector, remembered in localStorage

---

## 🚀 Getting started

No build, no install — it's a single static HTML file.

### 1. Open the file directly
Clone the repo and open `index.html` in your browser.

### 2. Local server (recommended)
```bash
git clone https://github.com/udaque/applied-inversion.git
cd applied-inversion
python3 -m http.server 8000
# or: npx serve .
```
Then visit `http://localhost:8000/`.

> Web Share, image clipboard, and "save to photos" only work over **HTTPS or localhost**.

### 3. GitHub Pages
In the repo's **Settings → Pages**, deploy the desired branch for a public URL.

---

## 📐 The math

Given the inversion center *O = (cx, cy)* and radius *r*, the source coordinate for an output pixel *Q = (x, y)* is

```
d² = (x - cx)² + (y - cy)²
P  = O + (Q - O) · (r² / d²)
```

- If *d²* is essentially zero, the source point lies at infinity → undefined region.
- If *P* lands outside the original image bounds, it's likewise undefined (or clamped to the nearest edge pixel).
- Otherwise, the pixel at *P* is sampled with bilinear or nearest-neighbor.

Points on the circle (*d = r*) are fixed; the inside and outside of the circle are swapped.

**Inverse of a grid line**: a horizontal line `y = b` with `b ≠ cy` becomes a circle through the inversion center — center `(cx, cy + r²/(2(b - cy)))`, radius `r²/(2|b - cy|)`. Lines passing through the center map to themselves.

---

## 🛠 Tips

- **Fine tuning**: drag with the mouse to get close, then nudge the X% / Y% / radius inputs for precision.
- **Save formats**:
  - For transparency, use PNG or WEBP. JPEG has no alpha channel, so it's composited on a white background automatically.
  - iOS only accepts PNG / JPEG / HEIC into the Photos library; WEBP shares will fall through to a Files save.
- **Performance**: the working preview is capped at 900px on the longer side (`MAX_DIM = 900`); save and share re-render at the original resolution.
- **Sharing**: Bluesky / X / Threads open with the text prefilled, so you only need to paste the image (Ctrl/⌘ V).

---

## 📂 Structure

```
applied-inversion/
├── index.html      # single-page HTML + CSS + JS
├── README.md       # Korean
└── README.en.md    # English (this file)
```

Zero dependencies — no external libraries, no package manager, no build step.

---

## 📜 License

MIT
