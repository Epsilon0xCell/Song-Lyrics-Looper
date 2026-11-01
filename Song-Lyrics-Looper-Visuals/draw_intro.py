#!/usr/bin/env python3
"""Song-Lyrics-Looper intro banner: Kelpie's loch warning signs, before the signs.
Pure scenery: no writing, no painted symbols, no logos, no interface markers.
Shingle and wet grass, a worn path cutting diagonally to the water and flooding
out into the loch, a row of bare sign posts with their boards removed for winter,
one leaning, a rusting paint tin, a coil of rope on a boulder, flat peat dark
water, reeds without a ripple, a smoother patch of shallows, low hills, white
houses with no lights, sheep dots, gorse scrub. Thin grey light with one warmer
break in the west. In the glassy shallows, hoofprints in the submerged silt lead
out of the deep water toward the path, and stop."""
import sys, random
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
random.seed(83)
W, H = 1600, 900
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
img = Image.new("RGB", (W, H), (168, 172, 168)); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):  # colourless overcast sky
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(176 - 30 * t), int(178 - 28 * t), int(172 - 24 * t)))
# one warmer break low in the west
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.ellipse([-200, 210, 520, 430], fill=(255, 196, 120, 54))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(40))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
# far hills in layered smoke grey
d.polygon([(0, 330), (300, 250), (620, 310), (900, 238), (1250, 300), (1600, 262), (1600, 430), (0, 430)], fill=(104, 110, 104))
d.polygon([(0, 380), (380, 306), (760, 360), (1120, 312), (1600, 352), (1600, 450), (0, 450)], fill=(84, 92, 84))
for _ in range(26):  # sheep dots on the slope
    x, y = random.randint(60, 1540), random.randint(300, 380)
    d.ellipse([x, y, x + 8, y + 4], fill=(206, 204, 194))
# white houses, no lights yet
for hx, hy, hw in ((180, 356, 74), (300, 366, 58), (1080, 350, 66), (1210, 360, 54), (1420, 348, 70)):
    d.rectangle([hx, hy, hx + hw, hy + 40], fill=(232, 230, 222))
    d.polygon([(hx - 6, hy), (hx + hw + 6, hy), (hx + hw // 2, hy - 24)], fill=(70, 68, 64))
    d.rectangle([hx + hw // 2 - 7, hy + 16, hx + hw // 2 + 7, hy + 40], fill=(96, 94, 90))
# gorse scrub along the shore road
for gx in range(40, 1580, 90):
    gy = 428 + (gx % 5) * 3
    d.ellipse([gx, gy, gx + 44, gy + 18], fill=(74, 88, 52))
    for _ in range(4):
        px, py = gx + random.randint(4, 38), gy + random.randint(2, 12)
        d.ellipse([px, py, px + 4, py + 4], fill=(168, 142, 54))
# the loch: flat, peat dark
for y in range(452, 700):
    t = (y - 452) / 248
    d.line([(0, y), (W, y)], fill=(int(52 - 16 * t), int(66 - 18 * t), int(62 - 16 * t)))
d.rectangle([0, 452, 1600, 458], fill=(120, 128, 118))  # far shore line
# reeds standing without a ripple
for rx in range(60, 1560, 46):
    rh = random.randint(26, 54)
    d.line([(rx, 640), (rx + random.randint(-4, 4), 640 - rh)], fill=(52, 66, 48), width=3)
    d.line([(rx + 9, 640), (rx + 12, 640 - rh + 10)], fill=(62, 76, 56), width=2)
# the smoother patch of shallows: lighter, glassier than anywhere else
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.ellipse([520, 520, 1080, 668], fill=(214, 220, 208, 52 if v != "v1" else 26))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(18))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
# hoofprints in the submerged silt, leading out of deep water toward the path, then stopping
for i in range(6):
    t = i / 5
    hx = 700 + int(150 * t) + (26 if i % 2 else -8)
    hy = 560 + int(118 * t)
    s = 15 + int(7 * t)
    d.arc([hx - s, hy - s - 4, hx + s, hy + s], 15, 165, fill=(206, 202, 176), width=4)
    d.line([(hx - s + 2, hy - 4), (hx - s + 2, hy - 12)], fill=(206, 202, 176), width=3)
    d.line([(hx + s - 2, hy - 4), (hx + s - 2, hy - 12)], fill=(206, 202, 176), width=3)
# near shore: shingle and wet grass
for y in range(700, 900):
    t = (y - 700) / 200
    d.line([(0, y), (W, y)], fill=(int(96 + 10 * t), int(98 + 8 * t), int(84 + 6 * t)))
for _ in range(900):
    x, y = random.randint(0, 1599), random.randint(706, 899)
    g = random.randint(120, 170)
    d.ellipse([x, y, x + random.randint(3, 9), y + 3], fill=(g, g - 4, g - 16))
for gx in range(0, 1600, 34):  # wet grass tufts
    gy = 712 + (gx * 7) % 150
    d.line([(gx, gy), (gx - 5, gy - 14)], fill=(70, 88, 54), width=2)
    d.line([(gx + 6, gy), (gx + 10, gy - 12)], fill=(70, 88, 54), width=2)
# worn path diagonally from lower corner to the water, last yards flooded
d.polygon([(150, 900), (330, 900), (690, 692), (622, 670)], fill=(128, 120, 98))
d.polygon([(620, 668), (700, 690), (760, 640), (700, 622)], fill=(104, 110, 96))  # flooded stretch
# row of bare sign posts, boards removed, one leaning, tops dark with rain
posts = [(420, 596, 0), (600, 578, 0), (788, 566, 13), (972, 556, 0), (1150, 548, 0)]
for px, py, lean in posts:
    d.line([(px, py + 130), (px + lean, py)], fill=(44, 46, 44), width=13)
    d.line([(px + lean - 9, py), (px + lean + 9, py)], fill=(30, 32, 30), width=7)  # rain dark top
    d.ellipse([px + lean - 3, py + 16, px + lean + 3, py + 22], fill=(150, 148, 140))  # empty bolt hole
# boulder with a coil of rope, rusting paint tin beside the leaning post
d.polygon([(1240, 700), (1360, 688), (1406, 730), (1396, 776), (1256, 776), (1228, 736)], fill=(104, 104, 98))
for r in (27, 18, 9):
    d.arc([1318 - r, 700 - r // 2, 1318 + r, 700 + r // 2 + 8], 20, 320, fill=(146, 122, 80), width=5)
d.ellipse([842, 738, 908, 754], fill=(70, 72, 62))
d.rectangle([848, 700, 900, 748], fill=(128, 84, 52)); d.ellipse([848, 692, 900, 708], fill=(150, 100, 62)); d.ellipse([856, 695, 892, 705], fill=(96, 60, 38))
# warm break touching the post tops
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
for px, py, lean in posts:
    ld.line([(px + lean - 8, py), (px + lean + 8, py)], fill=(255, 198, 120, 160), width=5)
img = Image.alpha_composite(img.convert("RGBA"), layer).convert("RGB")
rng = np.random.default_rng(13); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "intro-banner.png" if v == "ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
