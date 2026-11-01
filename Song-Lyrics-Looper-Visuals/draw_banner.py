#!/usr/bin/env python3
"""Song-Lyrics-Looper wordmark banner: a Highland loch near dusk. Left bank foreground:
three warning boards at the path bend, freshly repainted, one with the horse head,
one with a hand held flat in a stop gesture, one blank with the paint pot and brush
at its foot, and a fourth post hole dug. The path runs along shingle to a small
village: washing lines, a boat shed, chimneys with peat smoke straight up. Hills in
layered smoke grey behind. Low in the water a horse shape stands in the shallows,
head up, too still, facing the bank; nobody looks at it. The largest board carries
Song-Lyrics-Looper painted in uneven gold capitals in Anek Telugu."""
import sys, random
from PIL import Image, ImageDraw, ImageFont
import numpy as np
random.seed(91)
W, H = 2560, 640
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
TEAL = (16, 58, 60); GOLD = (206, 164, 56); EMBER = (178, 52, 34)
img = Image.new("RGB", (W, H), (150, 152, 144)); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(158 - 26 * t), int(160 - 24 * t), int(150 - 20 * t)))
# hills layered smoke grey
d.polygon([(0, 210), (500, 130), (1050, 196), (1600, 120), (2150, 180), (2560, 140), (2560, 330), (0, 330)], fill=(100, 106, 100))
d.polygon([(0, 268), (620, 196), (1300, 250), (1980, 204), (2560, 240), (2560, 340), (0, 340)], fill=(80, 88, 80))
# village: houses, boat shed, chimneys with peat smoke straight up
for hx, hy, hw in ((1560, 252, 110), (1730, 262, 92), (1900, 248, 120), (2100, 264, 96), (2280, 254, 108)):
    d.rectangle([hx, hy, hx + hw, hy + 62], fill=(228, 226, 216))
    d.polygon([(hx - 8, hy), (hx + hw + 8, hy), (hx + hw // 2, hy - 34)], fill=(58, 56, 54))
    d.rectangle([hx + hw - 30, hy - 52, hx + hw - 12, hy - 20], fill=(88, 78, 68))
    for si in range(5):  # peat smoke straight up
        d.ellipse([hx + hw - 34 + si * 2, hy - 66 - si * 16, hx + hw - 4 + si * 2, hy - 52 - si * 16], fill=(196, 196, 190, 130))
d.rectangle([1330, 272, 1470, 330], fill=(104, 110, 100))  # boat shed
d.polygon([(1322, 272), (1478, 272), (1400, 240)], fill=(50, 52, 50))
for wx in range(1560, 2400, 190):  # washing lines
    d.line([(wx, 300), (wx + 150, 306)], fill=(220, 220, 212), width=2)
    for ci, col in enumerate(((196, 180, 150), (150, 164, 170), (210, 206, 196))):
        d.rectangle([wx + 16 + ci * 44, 304, wx + 48 + ci * 44, 340], fill=col)
# the water, nearly black
for y in range(346, 520):
    t = (y - 346) / 174
    d.line([(0, y), (W, y)], fill=(int(34 - 10 * t), int(48 - 12 * t), int(46 - 12 * t)))
# the horse shape in the shallows: body, legs in the water, neck and head up facing the bank
hx, hy = 1740, 372
d.rectangle([hx, hy + 30, hx + 168, hy + 74], fill=(14, 22, 20))  # body
for lx in (hx + 14, hx + 52, hx + 116, hx + 148):
    d.line([(lx, hy + 74), (lx, hy + 112)], fill=(14, 22, 20), width=9)  # legs standing in the shallows
d.polygon([(hx + 6, hy + 40), (hx - 22, hy - 28), (hx - 6, hy - 52), (hx + 14, hy - 20), (hx + 44, hy + 18)], fill=(14, 22, 20))  # neck up
d.polygon([(hx - 26, hy - 50), (hx + 22, hy - 58), (hx + 34, hy - 36), (hx + 6, hy - 22), (hx - 20, hy - 28)], fill=(14, 22, 20))  # head, facing the bank
d.polygon([(hx - 8, hy - 56), (hx - 2, hy - 76), (hx + 8, hy - 54)], fill=(14, 22, 20))  # one ear
for lx in range(hx - 30, hx + 200, 26):  # faint reflection breaks
    d.line([(lx, hy + 118), (lx + 16, hy + 118)], fill=(90, 104, 96), width=2)
# shingle foreground
for y in range(520, 640):
    t = (y - 520) / 120
    d.line([(0, y), (W, y)], fill=(int(104 + 8 * t), int(104 + 6 * t), int(92 + 6 * t)))
for _ in range(700):
    x, y = random.randint(0, 2559), random.randint(526, 639)
    g = random.randint(120, 168)
    d.ellipse([x, y, x + random.randint(3, 8), y + 3], fill=(g, g - 4, g - 14))
# path along the shingle toward the village
d.polygon([(420, 640), (760, 640), (1330, 356), (1250, 350)], fill=(142, 134, 110))
# three warning boards at the path bend, left foreground
def board(bx, by, bw, bh):
    d.rectangle([bx + bw // 2 - 9, by + bh, bx + bw // 2 + 9, by + bh + 74], fill=(12, 44, 46))
    d.polygon([(bx + 14, by), (bx + bw - 14, by), (bx + bw, by + 14), (bx + bw, by + bh - 10), (bx + bw - 16, by + bh), (bx + 10, by + bh), (bx, by + bh - 12), (bx, by + 16)], fill=TEAL)
    for nx, ny in ((bx + 20, by + 18), (bx + bw - 20, by + 18)):
        d.ellipse([nx - 4, ny - 4, nx + 4, ny + 4], fill=(120, 116, 104))
    d.rectangle([bx + 4, by + bh - 14, bx + bw - 4, by + bh - 6], fill=EMBER)
# largest board: the horse head and the painted title
board(90, 190, 560, 240)
pts = [(212, 262), (232, 224), (250, 256), (268, 220), (282, 258), (330, 270), (392, 288), (436, 316), (452, 344), (448, 360), (408, 360), (368, 344), (336, 356), (318, 330), (306, 352), (288, 372), (268, 330), (254, 292)]
d.line(pts + [pts[0]], fill=GOLD, width=8, joint="curve")
d.ellipse([368, 300, 380, 312], fill=GOLD)
try:
    f = ImageFont.truetype("fonts/AnekTelugu.ttf", 44 if v != "v1" else 30)
except Exception:
    f = ImageFont.load_default()
txt = "Song-Lyrics-Looper"; tw = d.textlength(txt, font=f)
d.text((90 + 280 - tw / 2, 362), txt, font=f, fill=GOLD)
# second board: a hand held flat, stop
board(700, 226, 300, 190)
hx2, hy2 = 850, 268
d.polygon([(hx2 - 44, hy2 + 108), (hx2 - 44, hy2 + 30), (hx2 - 30, hy2 + 30), (hx2 - 30, hy2 - 26), (hx2 - 16, hy2 - 30), (hx2 - 14, hy2 + 22), (hx2 - 2, hy2 + 22), (hx2 - 2, hy2 - 38), (hx2 + 12, hy2 - 38), (hx2 + 12, hy2 + 22), (hx2 + 24, hy2 + 22), (hx2 + 24, hy2 - 26), (hx2 + 38, hy2 - 20), (hx2 + 40, hy2 + 34), (hx2 + 52, hy2 + 52), (hx2 + 44, hy2 + 108)], fill=GOLD)
# third board: blank, wet paint, pot and brush at its foot
board(1050, 246, 260, 160)
d.rectangle([1066, 262, 1294, 380], fill=(24, 74, 76))  # fresh paint sheen panel
d.rectangle([1120, 470, 1168, 512], fill=(150, 96, 54)); d.ellipse([1120, 462, 1168, 478], fill=(196, 164, 56))
d.line([(1196, 500), (1246, 462)], fill=(120, 92, 54), width=7); d.polygon([(1246, 462), (1264, 448), (1272, 458), (1254, 472)], fill=GOLD)
# a fourth post hole dug, with the spade
d.ellipse([880, 560, 960, 584], fill=(40, 36, 30)); d.ellipse([892, 554, 948, 572], fill=(58, 50, 40))
d.line([(990, 500), (1036, 566)], fill=(120, 92, 54), width=7); d.polygon([(1036, 566), (1058, 560), (1052, 590), (1032, 592)], fill=(110, 110, 106))
rng = np.random.default_rng(9); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "banner.png" if v == "ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
