#!/usr/bin/env python3
"""Song-Lyrics-Looper logo: a waterside warning board on one post, drawn straight on,
corners knocked off by weather, the post going down into black water lines. Inside
the board, carved in hoard gold, a horse head in profile with a wet mane plastered
flat, ears pricked, one eye a drilled dot. A thin ember stripe runs along the board
bottom edge. Song-Lyrics-Looper is painted underneath in Anek Telugu brush capitals.
At favicon size keep post, board, and gold horse head; lose words and water lines."""
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
W = H = 1024
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
TEAL = (16, 58, 60); GOLD = (198, 156, 52); EMBER = (178, 52, 34)
img = Image.new("RGB", (W, H), (206, 208, 196)); d = ImageDraw.Draw(img, "RGBA")
# post down into water
d.rectangle([486, 414, 538, 770], fill=(12, 44, 46))
for i, wy in enumerate((716, 748, 780)):
    wdt = 300 - i * 60
    d.arc([512 - wdt, wy - 14, 512 + wdt, wy + 14], 0, 180, fill=(24, 30, 28), width=5)
# board with weather knocked corners
bx0, by0, bx1, by1 = 112, 90, 912, 430
d.polygon([(bx0 + 26, by0), (bx1 - 26, by0), (bx1, by0 + 26), (bx1, by1 - 20), (bx1 - 30, by1), (bx0 + 18, by1), (bx0, by1 - 26), (bx0, by0 + 30)], fill=TEAL)
for px in range(bx0 + 30, bx1 - 20, 150):  # plank seams and nail dots
    d.line([(px, by0 + 14), (px, by1 - 14)], fill=(10, 40, 42), width=3)
for nx, ny in ((bx0 + 34, by0 + 34), (bx1 - 34, by0 + 34), (bx0 + 34, by1 - 34), (bx1 - 34, by1 - 34)):
    d.ellipse([nx - 6, ny - 6, nx + 6, ny + 6], fill=(120, 116, 104))
# horse head in profile, gold outline: poll, pricked ears, plastered mane, muzzle
pts = [(372, 158), (398, 96), (424, 152), (456, 92), (480, 158), (548, 176), (648, 204), (722, 252), (748, 302), (742, 330), (676, 330), (606, 306), (548, 330), (512, 286), (486, 336), (452, 368), (420, 300), (398, 226)]
lw = 13 if v != "v1" else 7
d.line(pts + [pts[0]], fill=GOLD, width=lw, joint="curve")
# wet mane plastered flat along the neck
for (mx, my) in ((522, 184), (490, 198), (458, 216), (432, 240)):
    d.line([(mx, my), (mx - 26, my + 52)], fill=GOLD, width=6)
d.ellipse([606, 232, 624, 250], fill=GOLD)  # drilled eye
d.arc([692, 292, 730, 326], 200, 330, fill=GOLD, width=6)  # nostril curve
d.rectangle([bx0 + 8, by1 - 26, bx1 - 8, by1 - 12], fill=EMBER)  # ember stripe last
if v != "v1":
    f = ImageFont.truetype("fonts/AnekTelugu.ttf", 58)
    txt = "Song-Lyrics-Looper"; tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, 824), txt, font=f, fill=(30, 52, 50))
rng = np.random.default_rng(7); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "logo.png" if v == "ship" else f"scratch/logo-{v}.png"
img.save(out); print(out)
img.resize((64, 64), Image.LANCZOS).save(f"scratch/logo64-{v}.png"); print("64px saved")
