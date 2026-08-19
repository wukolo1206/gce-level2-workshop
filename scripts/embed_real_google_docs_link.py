import json, re, os

real_link = "https://docs.google.com/document/d/1kE7fdTcA9Po3xXxpHmt-iaC1EQtKI0QVuEN8HhnQcXE/edit?usp=sharing"

# 1. Update docs_workshop_app.html
path_docs_app = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs_workshop_app.html'
with open(path_docs_app, 'r', encoding='utf-8') as f:
    html = f.read()

link_button_html = f'''
        <div style="background:#e6f4ea; border:1.5px solid #34a853; border-radius:10px; padding:16px; margin:16px 0; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
          <div>
            <strong style="color:#137333; font-size:1.02rem;">🔗 線上真實 Google Docs 演練檔案：</strong>
            <p style="font-size:0.88rem; color:#3c4043; margin-top:4px; margin-bottom:0;">內含多筆舊校長姓名「陳大文」，點擊開啟實檔即可直接在畫面上按 <code>Ctrl+H</code> 進行尋找與取代測試！</p>
          </div>
          <a href="{real_link}" target="_blank" style="text-decoration:none; background:#137333; color:white; padding:10px 20px; border-radius:20px; font-weight:700; font-size:0.9rem; box-shadow:0 2px 6px rgba(0,0,0,0.15);">📄 開啟真實 Google 文件進行練習</a>
        </div>
'''

if link_button_html not in html:
    html = html.replace('<h2>高效內文檢索與批次修正 (Find and Replace)</h2>', '<h2>高效內文檢索與批次修正 (Find and Replace)</h2>\n' + link_button_html)
    with open(path_docs_app, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated docs_workshop_app.html with real link!")

# 2. Update hands_on_tasks_app.html
path_tasks_app = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\hands_on_tasks_app.html'
with open(path_tasks_app, 'r', encoding='utf-8') as f:
    t_html = f.read()

task1_link_html = f'''
        <div style="background:#e6f4ea; border:1px solid #34a853; border-radius:8px; padding:12px 16px; margin:12px 0;">
          <strong style="color:#137333;">🔗 本題真實線上 Google Docs 實作檔案：</strong>
          <a href="{real_link}" target="_blank" style="color:#137333; font-weight:700; text-decoration:underline; margin-left:8px;">[點此開啟全校週報實作檔]</a>
          <span style="font-size:0.85rem; color:#5f6368; display:block; margin-top:4px;">（開啟後即可在文件內按 Ctrl+H 進行尋找與取代修改！）</span>
        </div>
'''

if task1_link_html not in t_html:
    t_html = t_html.replace('<h2 class="task-title">全校週報校長姓名全篇快速更正</h2>', '<h2 class="task-title">全校週報校長姓名全篇快速更正</h2>\n' + task1_link_html)
    with open(path_tasks_app, 'w', encoding='utf-8') as f:
        f.write(t_html)
    print("Updated hands_on_tasks_app.html with real link!")

print("Real Google Docs link embedded successfully!")
