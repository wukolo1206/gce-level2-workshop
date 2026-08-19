# -*- coding: utf-8 -*-
"""
把 study_guide_app.html 裡的「官方考試報名教學」抽成獨立頁面 exam_registration.html。

原本它是主講義的一個分頁，但學員（含公開版）也需要這份資訊，
獨立成頁後本機版與公開版可以共用同一份，不必維護兩份內容。
"""
import io
import os
import sys
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workshop_footer import FOOTER  # noqa: E402
SRC = os.path.join(ROOT, 'study_guide_app.html')

src = io.open(SRC, encoding='utf-8').read()

# 取出 reg-view 的內容（去掉外層 div）
start = src.index('<div id="reg-view"')
body_start = src.index('>', start) + 1
end = src.index('<div id="cheatsheet-view"')
inner = src[body_start:end]
# 移掉尾端多餘的收尾標籤
inner = inner.rstrip()
if inner.endswith('</div>'):
    inner = inner[:-len('</div>')].rstrip()

imgs = re.findall(r'src="(images/[^"]+)"', inner)

HTML = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>官方認證報名流程與考試架構</title>
<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:'Google Sans','Noto Sans TC',sans-serif; background:#f8f9fa; color:#202124; line-height:1.7; }}
  header {{ background:#1a73e8; color:#fff; padding:24px 32px; box-shadow:0 4px 12px rgba(26,115,232,.25);
            display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;
            position:sticky; top:0; z-index:100; }}
  header h1 {{ font-size:1.45rem; }}
  header p {{ opacity:.92; font-size:.9rem; margin-top:4px; }}
  .nav-btn {{ text-decoration:none; background:rgba(255,255,255,.2); color:#fff; padding:8px 16px;
              border-radius:20px; font-size:.85rem; font-weight:600; }}
  .nav-btn:hover {{ background:#fff; color:#1a73e8; }}
  .wrap {{ max-width:1000px; margin:28px auto; padding:0 20px 60px; }}
  .card {{ background:#fff; border-radius:12px; padding:28px; box-shadow:0 4px 16px rgba(0,0,0,.06); }}
  h2 {{ font-size:1.3rem; color:#1557b0; margin:26px 0 14px; }}
  h2:first-child {{ margin-top:0; }}
  h3 {{ font-size:1.08rem; margin:20px 0 10px; }}
  p, li {{ color:#3c4043; }}
  ul, ol {{ padding-left:22px; margin-bottom:14px; }}
  li {{ margin-bottom:6px; }}
  img {{ max-width:100%; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,.12); margin:8px 0; }}
  a {{ color:#1a73e8; }}
  table {{ width:100%; border-collapse:collapse; margin:14px 0; }}
  th, td {{ padding:10px 12px; border:1px solid #e8eaed; text-align:left; }}
  th {{ background:#f1f3f4; }}
</style>
</head>
<body>
<header>
  <div>
    <h1>📋 官方認證報名流程與考試架構</h1>
    <p>報名步驟 ‧ 認證控制台導覽 ‧ 兩大題型說明</p>
  </div>
  <div><a href="index.html" class="nav-btn">🏠 回講義首頁</a></div>
</header>

<div class="wrap">
  <div class="card">
{inner}
  </div>
</div>
{FOOTER}
</body>
</html>
'''

out = os.path.join(ROOT, 'exam_registration.html')
io.open(out, 'w', encoding='utf-8', newline='').write(HTML)
print(f'exam_registration.html 已產生：{len(HTML):,} 字元，引用 {len(imgs)} 張圖')
for i in imgs:
    print('   ', i)
