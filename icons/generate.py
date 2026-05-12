#!/usr/bin/env python3
"""Generate PWA icons: a cyan dashed circle around a cyan dot on a dark bg.

Outputs:
  icon-192.png, icon-512.png  - standard PWA icons
  icon-maskable-512.png       - same but with extra safe-area padding (Android)
  favicon-32.png              - small favicon
"""
from PIL import Image, ImageDraw
import math
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
BG = (17, 20, 24, 255)       # #111418 — app background
ACCENT = (80, 200, 255, 255) # #50c8ff — grid/accent cyan


def draw_dashed_circle(draw, cx, cy, r, color, stroke, dash_len, gap_len):
    circumference = 2 * math.pi * r
    seg = dash_len + gap_len
    n = max(8, int(circumference / seg))
    seg_angle = 360.0 / n
    dash_angle = seg_angle * dash_len / seg
    for i in range(n):
        start = i * seg_angle - 90
        end = start + dash_angle
        draw.arc(
            [cx - r, cy - r, cx + r, cy + r],
            start=start,
            end=end,
            fill=color,
            width=stroke,
        )


def draw_icon(size, padding_ratio=0.0):
    """padding_ratio shrinks the visual elements toward the center (safe area)."""
    # Render at 4x then downscale for smoother edges.
    scale = 4
    s = size * scale
    img = Image.new("RGBA", (s, s), BG)
    d = ImageDraw.Draw(img, "RGBA")

    cx = cy = s / 2
    # Visible region inside padding
    inset = padding_ratio * s / 2
    avail_r = s / 2 - inset

    # Dashed circle radius: 72% of available radius
    ring_r = int(avail_r * 0.72)
    stroke = max(2, int(s * 0.018))
    dash_len = max(4, int(s * 0.05))
    gap_len = max(4, int(s * 0.035))
    draw_dashed_circle(d, cx, cy, ring_r, ACCENT, stroke, dash_len, gap_len)

    # Center dot
    dot_r = max(3, int(s * 0.045))
    d.ellipse(
        [cx - dot_r, cy - dot_r, cx + dot_r, cy + dot_r],
        fill=ACCENT,
    )

    return img.resize((size, size), Image.LANCZOS)


def main():
    for size in (192, 512):
        draw_icon(size).save(os.path.join(OUT_DIR, f"icon-{size}.png"), optimize=True)
    # Maskable: extra padding so visual stays inside the safe circle when masked
    draw_icon(512, padding_ratio=0.18).save(
        os.path.join(OUT_DIR, "icon-maskable-512.png"), optimize=True
    )
    # Favicon (transparent bg for tabs)
    fav = draw_icon(32)
    fav.save(os.path.join(OUT_DIR, "favicon-32.png"), optimize=True)
    print("generated:", *[f for f in os.listdir(OUT_DIR) if f.endswith(".png")])


if __name__ == "__main__":
    main()
