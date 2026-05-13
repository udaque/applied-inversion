# Changelog

All notable changes to **Applied Inversive Geometry** are recorded here.
Newest first.

---

## [0.4] — 2026-05-13

### Added
- **Animation mode** — interpolate between two keyframes (first / last) and
  export the result as a video. The header **애니메이션 / Animate** button
  enters the mode and copies the current configuration into both keyframes;
  a banner on top of the source panel switches between first and last and
  exposes duration, FPS, format, codec, easing, and the
  **영상 저장 / Save video** button. Each keyframe edits independently
  (circle positions, radii, strength), and the renderer tweens the
  in-between frames.
- **MP4 / WebM / GIF** animation export. MP4 and WebM are encoded with
  **WebCodecs + mp4-muxer / webm-muxer** (loaded on demand from jsDelivr),
  with a **MediaRecorder** fallback for older browsers; GIF uses **gifenc**.
  Default is MP4.
- **Codec picker** — H.264 Baseline / Main / High for MP4, VP9 / VP8 for
  WebM, plus **Auto** that probes `VideoEncoder.isConfigSupported` and picks
  the most compatible codec. Lets users work around iOS Safari codec quirks
  (one profile may fail while another works).
- **Interpolation (easing) picker** — Linear, Ease-in-out (default),
  Smoothstep, Smootherstep.
- **Animation original-resolution toggle** — render each frame at the
  uploaded image's full resolution instead of the preview. Bitrate is scaled
  with pixel count (capped at ~50 Mbps). The hint warns that this is slower
  and produces larger files.
- **AVIF** added to the image save formats (next to PNG / JPEG / WEBP),
  feature-detected via `canvas.toBlob`.
- **Floating PIP for the result canvas on narrow viewports** (≤ 900 px).
  The right panel shrinks into a small floating thumbnail at the bottom-right
  corner so the result is visible while editing the source. Tap to expand
  to a full-screen view with zoom controls; × collapses back; a second ×
  hides the PIP entirely, and a round restore button at the same corner
  brings it back. The PIP fades to 30% while the user's pointer overlaps it
  during a source-canvas gesture, and animates toward / from the restore
  button when hidden / shown.

### Changed
- **Animation banner layout** — animation controls (duration, FPS, format,
  codec, easing, original-resolution, save) live in a dedicated banner above
  the source canvas. Circle add / remove buttons are locked on the last
  keyframe (with a title hint) so the circle count is set on the first frame.
- **Duration is capped at 4 seconds** — encoders get less stable beyond that
  on some mobile browsers.
- **Radius is capped at 1000 px app-wide** — values entered above 1000 are
  clamped with a toast, both for live editing and for animation frames.
- **Animation progress bar** uses an explicit `width: %` per frame instead
  of a CSS transition, so progress is visible the whole way through (no more
  "stuck at 0, then jumps to 100" behaviour).
- **cx / cy / radius inputs stay on one row at every viewport width** — the
  controls were collapsing onto separate lines on narrow mobile.
- Animation-explain modal no longer mentions the radius cap (it applies
  app-wide), and the format line now lists GIF too.
- Removed dead i18n keys (`animModeLabel`, `animEnter`, `animFormatExplain`,
  `animEasingExplain`).

### Fixed
- **iOS Safari MP4 false-negative** — previously the MP4 option said
  "not supported" even though the encoder worked. Detection now consults
  both `MediaRecorder.isTypeSupported` and `VideoEncoder.isConfigSupported`.
- Animation render no longer freezes on the first frame — pending edits on
  the active keyframe are flushed before the render loop starts.
- **Zoom / pan no longer reset when collapsing the PIP** back to mini view
  (the unconditional `resetView` on expand/collapse was wiping the user's
  view state). Wrap-size change now just re-triggers a hi-res render.
- **PIP no longer goes black after expand-zoom-pan-collapse** — `view.tx`
  / `view.ty` are absolute wrap pixels, so they're now rescaled by the
  width/height ratio whenever the wrap dimensions change (expand ↔ collapse).
- **Reload now restores both zoom and pan**, not just zoom. The
  `has-image` class is added synchronously after the canvas displays so
  the layout settles into the mobile PIP shape before the saved
  `vtx`/`vty` fractions are multiplied by the wrap rect.
- **Hi-res re-render no longer changes the result's vertical aspect.**
  The hi-res bitmap is now sized at the source aspect ratio so the
  inversion math (computed in output coordinates) stays isotropic — the
  previous wrap-aspect bitmap made `sxScale ≠ syScale`, turning the
  circle of inversion into an ellipse and visibly stretching the result
  the moment hi-res replaced the preview (most apparent in the expanded
  PIP layout).

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
- App icon in the header next to the title.
- Footer crediting [udaque](https://bsky.app/profile/udaqueness.blog) and
  noting the project was built with Claude Code.

### Changed
- Renamed the app to **Applied Inversive Geometry** (page title, share text,
  PWA manifest, READMEs). The browser tab title is unified to "Inversion"
  to match the PWA home-screen name.
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
  modal). The checkbox is now disabled unless there are exactly two circles,
  and the row dims visually when unavailable. Orbit-mode / clear-orbit
  buttons only appear while group exploration is on.
- Toolbar redesigned for narrow viewports: native file input replaced with a
  compact "이미지 업로드 / Upload image" button, gaps tightened, and a media
  query keeps the six toolbar items on a single row down to ~360px.

### Fixed
- Double-tap on the result canvas now resets the view on touch devices
  (`touch-action: none` was preventing the native `dblclick` event).
- Hidden buttons (orbit mode, clear orbits, etc.) were being overridden by an
  earlier `button { display: inline-flex }` rule. Restored the `[hidden]`
  semantic with an explicit `!important` rule.

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
