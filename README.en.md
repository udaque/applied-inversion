# Applied Inversion

A browser-based image **inversion** tool. Upload a photo, pick the center and radius of an inversion circle, and watch the planar inversion of the image render in real time.

> **Inversion** — Given a point *O* and a radius *r* in the plane, every point *P* (≠ *O*) is mapped to the point *Q* that lies on the ray *OP* and satisfies *OP · OQ = r²*.

🇰🇷 한국어 README는 [README.md](./README.md)를 참고하세요.

---

## ✨ Features

- 🖼 **Image upload** — drop or pick any local file (JPG, PNG, WEBP, …)
- 🎯 **Inversion circle controls**
  - **Click / tap** the canvas to jump the center to that location
  - **Drag the center dot** to reposition
  - **Drag the dashed edge** to resize the radius
  - **Type numeric values** for center X/Y (as % of width/height) and radius (in pixels) — fully two-way bound
- ⚡ **Real-time preview** — the inverted result re-renders on the right as soon as anything changes
- 🎨 **Undefined-region fill** — pixels near the center map outside the original image and have no source data. Choose how they look:
  - black / white / custom color / transparent
- 💾 **Save** — export as PNG (default), JPEG, or WEBP

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

### 3. GitHub Pages
Go to the repo's **Settings → Pages** and deploy the desired branch to publish it at a public URL.

---

## 📐 The math

Given the inversion center *O = (cx, cy)* and radius *r*, the source coordinate for an output pixel *Q = (x, y)* is:

```
d² = (x - cx)² + (y - cy)²
P  = O + (Q - O) · (r² / d²)
```

- If *d²* is essentially zero (too close to the center), the source point lies at infinity → undefined region.
- If *P* lands outside the original image bounds, it's likewise treated as undefined.
- Otherwise, the pixel at *P* is sampled (nearest-neighbor).

Points on the circle (*d = r*) are fixed; the inside and outside of the circle are swapped.

---

## 🛠 Tips

- **Fine tuning**: get close with the mouse, then nudge values precisely via the X% / Y% / radius inputs.
- **Save formats**:
  - For transparency, use **PNG** or **WEBP**. JPEG has no alpha channel, so the result is automatically composited onto a white background.
- **Performance**: for responsiveness the working canvas is capped at the longer side ≤ 900 px (`MAX_DIM = 900`), with the image scaled proportionally.

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
