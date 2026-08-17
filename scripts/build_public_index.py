# -*- coding: utf-8 -*-
"""
產生公開版首頁 public/index.html（GitHub Pages 用）。

與 study_guide_app.html 的差別：公開版<不包含>官方考試報名教學、完整版 6 Unit 講義、
考場實景截圖等與認證考試直接相關的內容，只保留十篇工具講義與課程結構對照。
"""
import io
import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 公開版輸出到 Drive 同步範圍外，避免 Drive 鎖檔與重複上傳
OUT = os.path.join('C:' + os.sep, 'repos', 'gce-level2-workshop')

TOOLS = [
    ('docs', '📄', 'Google Docs', '智慧晶片、段落樣式、翻譯、探索學習單', 7, ''),
    ('classroom', '🏫', 'Google Classroom', '協同教師、主題、成績匯入、公告', 5, ''),
    ('calendar', '📅', 'Google Calendar', '預約表、直播、權限、會議記錄、系列活動', 5, ''),
    ('slides', '🎨', 'Google Slides', '超連結、母版、內嵌影片、分享權限', 4, ''),
    ('sheets', '📊', 'Google Sheets', '條件式格式、樞紐分析、篩選器檢視', 3, ''),
    ('meet', '📹', 'Google Meet', '電話備援、檔案內視訊、分組討論室', 3, ''),
    ('forms', '📋', 'Google Forms', '區段跳轉、測驗評分、回應驗證', 3, ''),
    ('sites', '🌐', 'Google Sites', '子頁面、發布權限、內嵌動態內容', 3, ''),
    ('gmail', '📧', 'Gmail', '帳戶代理、篩選器、範本排程、搜尋運算子', 4, ''),
    ('practicesets', '💡', 'Practice Sets', '額外協助、題組共享、課程深入分析', 3, '⚠️ 需 Education Plus 授權'),
]

cards = ''
for key, emo, name, desc, n, note in TOOLS:
    nt = (f'<div style="margin-top:8px; font-size:.8rem; color:#b06000; font-weight:600;">{note}</div>'
          if note else '')
    cards += f'''
      <a href="{key}_workshop_app.html" style="display:block; text-decoration:none; background:#fff;
         border:1px solid #dadce0; border-radius:12px; padding:18px; transition:all .2s;"
         onmouseover="this.style.boxShadow='0 6px 18px rgba(0,0,0,.12)'; this.style.transform='translateY(-2px)'"
         onmouseout="this.style.boxShadow='none'; this.style.transform='none'">
        <div style="font-size:1.6rem; margin-bottom:8px;">{emo}</div>
        <div style="font-size:1.05rem; font-weight:700; color:#202124;">{name}</div>
        <div style="font-size:.85rem; color:#5f6368; margin-top:5px; line-height:1.5;">{desc}</div>
        <div style="margin-top:10px; font-size:.82rem; color:#1a73e8; font-weight:700;">{n} 個實務演練 ➔</div>
        {nt}
      </a>'''

sidebar = ''
for key, emo, name, desc, n, note in TOOLS:
    sidebar += (f'      <a href="{key}_workshop_app.html" style="display:flex; align-items:center; '
                f'justify-content:space-between; text-decoration:none; padding:9px 12px; border-radius:8px; '
                f'font-size:0.9rem; margin-bottom:3px; color:#3c4043;" '
                f'onmouseover="this.style.background=\'#f1f3f4\'" onmouseout="this.style.background=\'transparent\'">'
                f'<span>{emo} {name}</span>'
                f'<span style="font-size:.78rem; color:#5f6368;">{n} 個演練</span></a>\n')

HTML = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Google Certified Educator Level 2 研習講義</title>
<link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:'Google Sans','Noto Sans TC',sans-serif; background:#f8f9fa; color:#202124; line-height:1.65; }}
  header {{ background:#1a73e8; color:#fff; padding:26px 32px; box-shadow:0 4px 12px rgba(26,115,232,.25); }}
  header h1 {{ font-size:1.5rem; }}
  header p {{ opacity:.92; font-size:.92rem; margin-top:5px; }}
  .layout {{ max-width:1200px; margin:28px auto; padding:0 20px; display:grid; grid-template-columns:260px 1fr; gap:24px; }}
  @media (max-width:900px) {{ .layout {{ grid-template-columns:1fr; }} }}
  aside, main {{ background:#fff; border-radius:12px; padding:22px; box-shadow:0 4px 16px rgba(0,0,0,.06); height:fit-content; }}
  .sidebar-title {{ font-size:.85rem; font-weight:700; color:#5f6368; letter-spacing:.5px; margin-bottom:10px; }}
  h2 {{ font-size:1.35rem; color:#1557b0; margin-bottom:10px; }}
</style>
</head>
<body>
<header>
  <h1>🎓 Google Certified Educator Level 2</h1>
  <p>研習講義 ‧ 十個工具 ‧ 40 個實務演練 ‧ 每則都有真實情境與可動手的練習環境</p>
</header>

<div class="layout">
  <aside>
    <div class="sidebar-title">🧰 十篇工具講義</div>
{sidebar}
    <div class="sidebar-title" style="margin-top:20px;">🗺️ 另一種視角</div>
    <a href="course_structure_map.html" style="display:block; text-decoration:none; padding:10px 12px;
       background:#f3e8fd; color:#7b1fa2; border-radius:8px; font-size:0.87rem; font-weight:600;">
      繁中 11 單元 × 英文 6 Units 對照</a>

    <div class="sidebar-title" style="margin-top:20px;">📋 認證報名</div>
    <a href="exam_registration.html" style="display:block; text-decoration:none; padding:10px 12px;
       background:#e6f4ea; color:#137333; border-radius:8px; font-size:0.87rem; font-weight:600; line-height:1.45;">
      官方報名流程與考試架構
      <span style="display:block; font-size:.76rem; color:#5f6368; font-weight:500;">5 大步驟 ‧ 控制台導覽 ‧ 題型說明</span></a>

    <div class="sidebar-title" style="margin-top:20px;">🔗 官方課程</div>
    <a href="https://edu.exceedlms.com/student/path/1727915?locale=zh_tw" target="_blank" rel="noopener"
       style="display:block; text-decoration:none; padding:10px 12px; background:#e8f0fe; color:#1557b0;
              border-radius:8px; font-size:0.87rem; font-weight:600; margin-bottom:5px; line-height:1.45;">
      🇹🇼 繁體中文版課程
      <span style="display:block; font-size:.76rem; color:#5f6368; font-weight:500;">11 個實務單元 ‧ Path 1727915</span></a>
    <a href="https://edu.exceedlms.com/student/path/1717663" target="_blank" rel="noopener"
       style="display:block; text-decoration:none; padding:10px 12px; background:#e8f0fe; color:#1557b0;
              border-radius:8px; font-size:0.87rem; font-weight:600; margin-bottom:5px; line-height:1.45;">
      🇬🇧 英文版課程
      <span style="display:block; font-size:.76rem; color:#5f6368; font-weight:500;">6 Units / 18 Lessons ‧ Path 1717663</span></a>
    <a href="https://edu.google.com/teacher-center/" target="_blank" rel="noopener"
       style="display:block; text-decoration:none; padding:10px 12px; background:#f1f3f4; color:#3c4043;
              border-radius:8px; font-size:0.87rem; font-weight:600; line-height:1.45;">
      🎓 Google Teacher Center
      <span style="display:block; font-size:.76rem; color:#5f6368; font-weight:500;">官方教師培訓總入口</span></a>
  </aside>

  <main>
    <h2>十篇工具講義</h2>
    <p style="color:#5f6368; margin-bottom:8px;">
      本研習以<strong>工具</strong>為主軸：一個工具的功能一次學完，不用在工具之間跳來跳去。
      共 <strong>40 個實務演練</strong>，每則都有真實教學情境、可動手的練習環境與步驟勾選清單。</p>
    <p style="color:#5f6368; margin-bottom:20px; font-size:.9rem;">
      每則演練都會標明<strong>練習方式</strong>：複製範本、一鍵建立、兩人一組、講師開房、自己建一次，
      或標註需付費授權並附上一般帳號的替代練習。</p>
    <div style="display:grid; grid-template-columns:repeat(auto-fill,minmax(250px,1fr)); gap:16px;">
{cards}
    </div>
    <div style="background:#fef7e0; border-left:4px solid #f9ab00; padding:16px 20px;
                border-radius:0 8px 8px 0; margin-top:24px;">
      <strong style="color:#b06000;">💡 想從「教學情境」而不是「工具」切入？</strong>
      <p style="margin-top:6px; color:#3c4043;">
        點左側的<strong>課程結構對照</strong>，可以看到官方繁中 11 個實務單元、英文 6 大 Units
        與這十篇工具講義的三方對應——同一批內容的另一種組織方式。</p>
    </div>
  </main>
</div>

  <footer style="max-width:1200px; margin:8px auto 40px; padding:22px 20px 0; border-top:1px solid #dadce0;
                 color:#5f6368; font-size:.84rem; line-height:1.8; text-align:center;">
    <div style="font-weight:700; color:#3c4043; margin-bottom:6px;">
      Google Certified Educator Level 2 研習講義
    </div>
    <div>製作：<strong>碧華國小　吳國榮</strong></div>
    <div style="margin-top:8px;">
      © 2026 吳國榮．本講義之情境設計、演練編排與文字內容為原創教學素材，
      歡迎教育工作者於教學與研習用途自由使用與改編，轉載請註明出處。
    </div>
    <div style="margin-top:6px; color:#80868b;">
      Google、Google Workspace、Google Classroom、Google Meet 等名稱與標誌為 Google LLC 之商標。
      本講義為個人教學製作，與 Google LLC 無隸屬或合作關係。
    </div>
  </footer>
</body>
</html>
'''

# ---- 產生 public/ 目錄 ----
for sub in ('', 'images', 'scripts'):
    d = os.path.join(OUT, sub) if sub else OUT
    os.makedirs(d, exist_ok=True)
# 清掉舊的產出檔（保留 .git）
# 只清掉本腳本產生的檔案，保留 repo 層級檔案（README、LICENSE、.gitignore 等）
KEEP = {'.git', '.gitignore', 'README.md', 'LICENSE', '.nojekyll'}
for name in os.listdir(OUT):
    if name in KEEP:
        continue
    fp = os.path.join(OUT, name)
    if os.path.isfile(fp):
        os.remove(fp)

io.open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(HTML)

def copy_page(src_name, dst_name=None):
    """複製頁面，並把指向主講義的連結改為公開版首頁（公開版不含 study_guide_app.html）。"""
    dst_name = dst_name or src_name
    html = io.open(os.path.join(ROOT, src_name), encoding='utf-8').read()
    html = html.replace('href="study_guide_app.html"', 'href="index.html"')
    html = html.replace('📖 回研習主講義', '🏠 回講義首頁')
    io.open(os.path.join(OUT, dst_name), 'w', encoding='utf-8', newline='').write(html)


copied = 1
for key, *_ in TOOLS:
    copy_page(f'{key}_workshop_app.html'); copied += 1
copy_page('course_structure_map.html'); copied += 1
copy_page('exam_registration.html'); copied += 1
for img in ['docs_insert_toc_menu.png',
            # 認證報名頁使用（報名流程與控制台導覽）
            'gce_launchpad.png', 'confirm_eligibility.png', 'registration_complete.png',
            'continue_exams_card.png', 'switch_language_menu.png',
            'exam_structure_dropdown.png', 'actual_exam_screen.png']:
    shutil.copy2(os.path.join(ROOT, 'images', img), os.path.join(OUT, 'images', img)); copied += 1
for f in ['workshop_content.py', 'workshop_glossary.py', 'build_workshop_apps.py',
          'build_course_structure_map.py', 'build_public_index.py']:
    shutil.copy2(os.path.join(ROOT, 'scripts', f), os.path.join(OUT, 'scripts', f)); copied += 1

print(f'{OUT} 已更新：{copied} 個檔案（index + 10 篇工具講義 + 結構對照 + 1 張圖 + 5 支產生器）')
