# Changelog

All notable changes to **Applied Inversion** are recorded here.
Newest first.

---

## [0.3] — 2026-05-13

### Added
- **Preset storage** — save the current configuration to one of five slots in
  `localStorage`, load with a click, delete with ×. Save dialog with name + slot
  picker (marks already-filled slots as "overwrite").
- **Export / import presets** as JSON for backup or device-to-device sharing.
- **Page-title info modal** explaining the definition and properties of
  inversion and what this tool is for.
- **Info modals on every advanced option** (강도, 채우기, 샘플링, 저장 포맷,
  원본 해상도, 그리드 오버레이, 군 시각화, 프리셋).
- **Three-section layout** inside the advanced panel: 이미지 / 보조 시각화 /
  입출력 (Image / Visualization / I/O).
- Footer crediting [udaque](https://bsky.app/profile/udaqueness.blog).

### Changed
- Advanced options reorganized into a three-column grid (label, info icon,
  control). Every slider, dropdown, checkbox, and radio group now starts on
  the same column edge.
- Fill mode label "정보 없는 영역" → **"채우기" / "Fill"**; default mode
  changed from black to **edge clamp**.
- "원본 해상도로 저장" moved to its own row, separate from the format
  selector. Both still share the same info modal.
- Result-canvas grid overlay now reflects the **full composition** of all
  inversion circles (not just the active one); switching the active circle
  no longer changes the right-side grid.
- "군 시각화" label simplified (the "(2 원)" qualifier moved into the info
  modal).

### Fixed
- Double-tap on the result canvas now resets the view on touch devices
  (`touch-action: none` was preventing the native `dblclick` event).

---

## [0.2] — 2026-05-12

### Added
- **Multiple inversion circles** with sequential composition rendering
  (Möbius transformation when N = 2).
- **Group exploration overlay** — classifies σ₂∘σ₁ as Elliptic / Parabolic /
  Hyperbolic, draws fixed points, the hyperbolic axis, and (optionally) seed
  orbits.
- **Strength slider** for partial inversion (linear blend of the source coord
  with the output coord).
- **Web Worker + ImageData transfer** rendering pipeline (initially
  `OffscreenCanvas` transferred, later switched to ImageData transfer for
  reliable hi-res redraw).
- **Bilinear sampling** (now the default) in addition to nearest-neighbor.
- **Edge-clamp option** for the undefined region near the inversion center.
- **Save at original resolution** — preview is capped at ≤ 900 px for speed,
  exports re-render from the full-resolution source.
- **Web Share API on save** so mobile users can route the result to the
  photo library or any installed app.
- **Zoom & pan on the result canvas** — mouse wheel, pinch, drag, double-click
  reset, plus an explicit "화면 맞춤" button and zoom-percentage label.
- **Hi-res re-render after zoom settles** — bitmap grows with `view.scale` and
  device pixel ratio (capped at 12M pixels).
- **Grid overlay** — fixed Cartesian grid on the source, mapped through the
  inversion on the result.
- **Drag inside circle pans** (instead of jumping the center); rotating
  resize cursor based on angle around the active circle.
- **Drag-and-drop + clipboard paste** image upload.
- **Undo / redo** with Ctrl/⌘ Z, Ctrl/⌘ ⇧ Z keyboard shortcuts and toolbar
  ↶ / ↷ buttons.
- **Korean / English language toggle**, persisted in `localStorage`.
- **URL hash for shareable composition links** — center as %, radius as %,
  view, fill mode and color, sampling, grid options, language, strength,
  multi-circle list.
- **IndexedDB image persistence** + **localStorage** mirror of the URL hash,
  so reload restores the last image and last settings.
- **SNS share buttons** — Bluesky, X, Threads, Instagram, device share,
  copy link. Image is copied to clipboard so the compose window can paste
  it, or routed via Web Share on mobile.
- **Installable PWA** — manifest, service worker, custom icons (cyan dashed
  circle), offline support, dark theme color, apple-touch-icon.
- **Inverted grid overlay**, **circle number labels**, and a cleaner pointer
  interaction model for the source canvas.

---

## [0.1] — 2026-05-12

### Added
- Initial release.
- Upload an image, set the inversion-circle center and radius by clicking,
  dragging, or by entering precise numbers (% width/height + pixel radius).
- Real-time inversion result on the right side.
- Undefined-region fill: black / white / custom color / transparent.
- Save as PNG (default), JPEG, or WEBP.
