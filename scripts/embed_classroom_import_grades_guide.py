import shutil, os

# 1. Save user's screenshot showing the Import Grades button and draft scores
src_img = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787207482656.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_img = os.path.join(dest_dir, 'classroom_import_grades_button_and_draft_scores.png')
shutil.copy2(src_img, dst_img)
print("Copied Classroom import grades screenshot!")

# 2. HTML Card for classroom_workshop_app.html Module 3
import_grades_card_html = '''
        <!-- 📝 測驗作業成績匯入完整流程與實作截圖卡片 -->
        <div style="background:#ffffff; border:2px solid #1a73e8; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(26,115,232,0.1);">
          <h3 style="color:#1557b0; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            📝 實務介面圖解：【匯入成績按鈕】與【草稿分數發還機制】
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            許多老師常困惑「為什麼學生考完試，全班成績總表還是空白的？」這是因為 Google Classroom 為了讓老師能統一審閱，<strong>需要老師手動點擊「匯入成績」按鈕</strong>：
          </p>

          <div style="display:grid; grid-template-columns:1.2fr 0.8fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#1557b0; margin-bottom:8px;">📷 成果展示：作業評分頁右上角【匯入成績】按鈕與「草稿」分數：</p>
              <img src="images/classroom_import_grades_button_and_draft_scores.png" alt="Google Classroom 匯入成績按鈕與草稿分數" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">點擊「匯入成績」後抓回表單分數（顯示為草稿），最後按「發還」正式公布！</p>
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#1557b0; font-size:0.95rem;">⚡ 成績匯入標準 3 步驟與 3 大前提：</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>第 1 步</strong>：進入「課堂作業 ➔ 該測驗作業 ➔ 查看作業」。</li>
                <li><strong>第 2 步</strong>：點選右上角 <code>匯入成績 (Import grades)</code> 按鈕。</li>
                <li><strong>第 3 步</strong>：分數帶入左側顯示「草稿」➔ 勾選學生點選 <code>發還 (Return)</code>，分數即同步至全班「成績」大總表！</li>
              </ul>
              <div style="background:#fef7e0; border-radius:6px; padding:8px 12px; margin-top:8px; font-size:0.82rem; color:#b06000;">
                ⚠️ <strong>3 大必要前提</strong>：① 表單為<strong>唯一附件</strong> ② 表單開啟<strong>收集電子郵件（已驗證）+ 限答 1 次</strong> ③ 學生需在<strong>同網域</strong>且為學生身分。
              </div>
            </div>
          </div>
        </div>
'''

p_cr = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'classroom_workshop_app.html')
with open(p_cr, 'r', encoding='utf-8') as f:
    h_cr = f.read()

target_m3_cr = '<h2>建立測驗作業 (Quiz Assignment) 並開啟成績匯入 (Grade importing)</h2>'
if target_m3_cr in h_cr and 'classroom_import_grades_button_and_draft_scores.png' not in h_cr:
    h_cr = h_cr.replace(target_m3_cr, target_m3_cr + '\n' + import_grades_card_html)
    with open(p_cr, 'w', encoding='utf-8') as f:
        f.write(h_cr)
    print("Embedded import grades screenshot in classroom_workshop_app.html!")

# 3. Update hands_on_tasks_app.html Task 11
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

if 'classroom_import_grades_button_and_draft_scores.png' not in h_tasks and '測驗作業與成績自動匯入' in h_tasks:
    h_tasks = h_tasks.replace('<h2>建立測驗作業 (Quiz Assignment)', import_grades_card_html + '\n<h2>建立測驗作業 (Quiz Assignment)')
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded import grades in hands_on_tasks_app.html!")

# 4. Update Markdown manual Task 11
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_cr_guide = '''
##### 📝 Classroom 實務介面圖解：匯入成績按鈕與草稿分數發還流程
![Google Classroom 匯入成績按鈕與草稿分數](../images/classroom_import_grades_button_and_draft_scores.png)
*圖 16：作業評分頁點選右上角「匯入成績」帶入測驗分數（顯示為草稿），最後點選左上角「發還」正式公布*

> 💡 **核心操作與機制解析**：
> 1. **為何不會全自動填入？** Google 設計為需教師手動點擊「匯入成績」，便於全班考完或手動批改簡答題後統一帶入。
> 2. **發還機制**：匯入後的分數屬於「草稿」，需勾選學生點選 **「發還 (Return)」**，才會正式計入全班「成績」大總表並通知學生！
> 3. **3 大前提檢核**：表單為唯一附件、表單開啟收集已驗證 Email + 限答 1 次、學生為同網域帳號。
'''

if 'classroom_import_grades_button_and_draft_scores.png' not in h_md and '#### 演練 11' in h_md:
    h_md = h_md.replace('#### 演練 11', '#### 演練 11\n' + md_cr_guide)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded import grades in markdown manual!")

print("All Classroom documentation updated! Ready to deploy.")
