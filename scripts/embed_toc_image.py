import shutil, os

src = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1786861804610.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)
dest = os.path.join(dest_dir, 'docs_insert_toc_menu.png')

shutil.copy2(src, dest)
print(f"Copied {src} to {dest}")

# 1. Update docs_workshop_app.html
path_app = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs_workshop_app.html'
with open(path_app, 'r', encoding='utf-8') as f:
    html = f.read()

img_card = '''
        <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:10px; padding:16px; margin:16px 0; text-align:center;">
          <p style="font-size:0.9rem; font-weight:700; color:#1a73e8; margin-bottom:8px;">📷 Google Docs 插入目錄介面對照圖（插入 ➔ 頁面元素 ➔ 目錄）：</p>
          <img src="images/docs_insert_toc_menu.png" alt="Google Docs 插入目錄介面截圖" style="max-width:100%; border-radius:8px; box-shadow:0 2px 8px rgba(0,0,0,0.12);">
        </div>
'''

if 'docs_insert_toc_menu.png' not in html:
    html = html.replace('<h2>結構化排版與動態導覽目錄 (Paragraph Styles)</h2>', '<h2>結構化排版與動態導覽目錄 (Paragraph Styles)</h2>\n' + img_card)
    with open(path_app, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Embedded image in docs_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
path_tasks = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\hands_on_tasks_app.html'
with open(path_tasks, 'r', encoding='utf-8') as f:
    t_html = f.read()

img_card_task = '''
        <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; margin:12px 0; text-align:center;">
          <p style="font-size:0.85rem; font-weight:700; color:#1a73e8; margin-bottom:6px;">📷 目錄介面指引圖（選單路徑：插入 ➔ 頁面元素 ➔ 目錄）：</p>
          <img src="images/docs_insert_toc_menu.png" alt="Google Docs 插入目錄介面截圖" style="max-width:100%; max-height:350px; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
        </div>
'''

if 'docs_insert_toc_menu.png' not in t_html:
    t_html = t_html.replace('<h2 class="task-title">校本課程實施計畫手冊自動目錄製作</h2>', '<h2 class="task-title">校本課程實施計畫手冊自動目錄製作</h2>\n' + img_card_task)
    with open(path_tasks, 'w', encoding='utf-8') as f:
        f.write(t_html)
    print("Embedded image in hands_on_tasks_app.html!")

# 3. Update Markdown files
path_md1 = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\Google_Docs_進階功能與行政自動化研習講義.md'
with open(path_md1, 'r', encoding='utf-8') as f:
    md1 = f.read()

md_img = '\n![Google Docs 插入目錄選單對照圖](../images/docs_insert_toc_menu.png)\n*圖：Google Docs 插入目錄功能路徑（選單：插入 ➔ 頁面元素 ➔ 目錄）*\n'

if 'docs_insert_toc_menu.png' not in md1:
    md1 = md1.replace('## 📖 核心功能應用二：結構化排版與動態導覽目錄', '## 📖 核心功能應用二：結構化排版與動態導覽目錄\n' + md_img)
    with open(path_md1, 'w', encoding='utf-8') as f:
        f.write(md1)
    print("Embedded image in Google_Docs_進階功能與行政自動化研習講義.md!")

print("All TOC menu image embeddings complete!")
