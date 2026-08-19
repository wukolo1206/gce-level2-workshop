# -*- coding: utf-8 -*-
"""產生考場實景圖的去識別打碼版，供公開版使用。

遮蔽兩類內容：
1. 右上角帳號頭像（個人資料）
2. 正式試題題幹文字（官方考題內容，不可公開散布）

保留考試介面外框、麵包屑與導覽按鈕，讓學員仍看得出畫面長相。
公開版一律使用本腳本產出的 *_masked.png；原圖只留在私人 repo。
新增需打碼的圖時，在 JOBS 補一筆即可。
"""
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES = os.path.join(ROOT, 'images')

# 座標為 (left, top, right, bottom)，對應各圖原始尺寸
JOBS = [
    # 1024x472：帳號頭像 + 第 1 題題幹
    {'src': 'actual_exam_screen.png',
     'avatars': [(984, 10, 1020, 46)],
     'blurs': [((270, 300, 780, 372), '（題目內容不公開）')]},
    # 508x427：只有右上角帳號頭像
    {'src': 'switch_language_menu.png',
     'avatars': [(432, 18, 484, 70)],
     'blurs': []},
]

try:
    FONT = ImageFont.truetype('C:/Windows/Fonts/msjh.ttc', 20)
except OSError:
    FONT = ImageFont.load_default()


def mask(job):
    src = os.path.join(IMAGES, job['src'])
    dst = os.path.join(IMAGES, job['src'].replace('.png', '_masked.png'))
    im = Image.open(src).convert('RGBA')

    # 頭像：以中性灰圓形覆蓋
    draw = ImageDraw.Draw(im)
    for box in job['avatars']:
        draw.ellipse(box, fill=(189, 193, 198, 255))

    # 題幹：重度模糊後再壓一層半透明白，確保文字不可還原
    for box, label in job['blurs']:
        im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(14)), box)
        overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
        ImageDraw.Draw(overlay).rectangle(box, fill=(255, 255, 255, 205))
        im = Image.alpha_composite(im, overlay)

        d = ImageDraw.Draw(im)
        d.rectangle(box, outline=(218, 220, 224, 255), width=1)
        bb = d.textbbox((0, 0), label, font=FONT)
        d.text(((box[0] + box[2] - bb[2] + bb[0]) // 2,
                (box[1] + box[3] - bb[3] + bb[1]) // 2),
               label, font=FONT, fill=(95, 99, 104, 255))

    im.convert('RGB').save(dst)
    print('已產生 {} （{}）'.format(os.path.basename(dst), im.size))


for j in JOBS:
    mask(j)
