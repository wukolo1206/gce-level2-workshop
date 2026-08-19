import shutil, os

src_menu = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787117406801.png'
src_panel = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787117499843.png'

dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_menu = os.path.join(dest_dir, 'meet_docs_join_call_here_menu.png')
dst_panel = os.path.join(dest_dir, 'meet_docs_side_panel_video_collab.png')

shutil.copy2(src_menu, dst_menu)
shutil.copy2(src_panel, dst_panel)
print("Copied Meet in-file collaboration screenshots!")

infile_meet_html = '''
        <!-- 💻 Docs / Slides 檔案內發起 Meet 實戰截圖與操作解析 -->
        <div style="background:#ffffff; border:2px solid #34a853; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(52,168,83,0.1);">
          <h3 style="color:#137333; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            💻 實務介面圖解：從 Docs 頂部發起「檔案內 Meet 側邊欄邊看邊修」
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            過去視訊會議需要「切換分頁 ➔ 螢幕分享」，對方只能看不能同步動手改。現在只要在 Docs/Slides 點擊右上角攝影機圖示，視訊畫面就能<strong>直接浮動在文件右側側邊欄</strong>：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#137333; margin-bottom:8px;">📷 1. 點右上角攝影機圖示 ➔「在這裡進行通話」：</p>
              <img src="images/meet_docs_join_call_here_menu.png" alt="Google Docs 頂部 Meet 圖示下拉選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">可選擇「在這裡進行通話」或「只分享這個分頁畫面」</p>
            </div>
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#137333; margin-bottom:8px;">📷 2. 成果：左邊共同編輯、右邊即時視訊討論：</p>
              <img src="images/meet_docs_side_panel_video_collab.png" alt="Google Docs 右側浮動 Meet 側邊欄" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">視訊鏡頭與麥克風常駐右側，完全不遮擋左側文件編輯區！</p>
            </div>
          </div>

          <div style="background:#e6f4ea; border-left:4px solid #34a853; border-radius:0 8px 8px 0; padding:14px; font-size:0.9rem; line-height:1.7;">
            <div style="font-weight:700; color:#137333; margin-bottom:6px;">✨ 檔案內視訊 (In-file Meet) 的三大實戰教學優勢：</div>
            <ul style="padding-left:20px; color:#202124;">
              <li><strong>真正即時共編</strong>：所有人都能一邊看到彼此游標與修改內容、一邊即時對話討論。</li>
              <li><strong>免切換視窗</strong>：不用在 Meet 分頁與 Google Docs 分頁之間來回跳轉切換。</li>
              <li><strong>一鍵邀請共編者</strong>：右側側邊欄提供 <code>這個檔案和視訊通話</code> 快速分享連結，一次完成文件共編授權與會議加入！</li>
            </ul>
          </div>
        </div>
'''

# 1. Update meet_workshop_app.html
p_meet = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'meet_workshop_app.html')
with open(p_meet, 'r', encoding='utf-8') as f:
    h_meet = f.read()

target_m2_meet = '<h2>從 Google Docs/Slides 頂部工具列直接發起或加入 Meet 會議</h2>'
if target_m2_meet in h_meet and 'meet_docs_join_call_here_menu.png' not in h_meet:
    h_meet = h_meet.replace(target_m2_meet, target_m2_meet + '\n' + infile_meet_html)
    with open(p_meet, 'w', encoding='utf-8') as f:
        f.write(h_meet)
    print("Embedded in-file Meet screenshots in meet_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'meet_docs_join_call_here_menu.png' not in h_tasks and '文件內即時視訊邊看邊修範本' in h_tasks:
    h_tasks = h_tasks.replace('文件內即時視訊邊看邊修範本', '文件內即時視訊邊看邊修範本' + '\n' + infile_meet_html)
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded in-file Meet screenshots in hands_on_tasks_app.html!")

# 3. Update Markdown manual Task 25 (Docs in-file Meet)
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_meet_m2 = '''
##### 💻 Docs 檔案內發起 Meet 實務介面圖解
![Google Docs 頂部 Meet 圖示下拉選單](../images/meet_docs_join_call_here_menu.png)
*圖 12：點擊右上角攝影機圖示 ➔ 選擇「在這裡進行通話 (Join the call here)」*

![Google Docs 右側浮動 Meet 側邊欄](../images/meet_docs_side_panel_video_collab.png)
*圖 13：成果——左側文件即時共編、右側 Meet 側邊欄視訊與語音同步進行！*

> ✨ **核心優勢**：免螢幕分享、免切換分頁，左邊打字修改、右邊視訊對話，支援一鍵發送「這個檔案和視訊通話」連結！
'''

if 'meet_docs_join_call_here_menu.png' not in h_md and '#### 演練 25' in h_md:
    h_md = h_md.replace('#### 演練 25', '#### 演練 25\n' + md_meet_m2)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded in-file Meet in markdown manual!")

print("All in-file Meet updates ready for deployment!")
