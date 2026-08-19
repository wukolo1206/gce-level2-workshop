import shutil, os

src_img = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787150547147.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_img = os.path.join(dest_dir, 'sheets_filter_view_math.png')
shutil.copy2(src_img, dst_img)
print("Copied Sheets filter view image!")

p_sheets = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'sheets_workshop_app.html')
with open(p_sheets, 'r', encoding='utf-8') as f:
    h_sheets = f.read()

# Update module 3 step 3 in sheets_workshop_app.html
old_step3 = '<label for="m3-s3">選取「狀態」欄位，點選 <strong>「資料 ➔ 資料驗證 (Data validation)」</strong>。</label>'
new_step3 = '<label for="m3-s3">在 <strong>E1 儲存格輸入「狀態」</strong>（用來追蹤補救進度），選取 <strong>E2:E6 範圍</strong>，點選 <strong>「資料 ➔ 資料驗證 (Data validation)」</strong>。</label>'

if old_step3 in h_sheets:
    h_sheets = h_sheets.replace(old_step3, new_step3)
    print("Updated step 3 in sheets_workshop_app.html!")

# Add filter view illustration card
filter_view_card = '''
        <!-- 🔒 篩選器檢視畫面 vs 一般篩選器 & 資料驗證下拉選單解析 -->
        <div style="background:#ffffff; border:2px solid #1a73e8; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(26,115,232,0.1);">
          <h3 style="color:#1557b0; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            🔒 實作圖解：【篩選器檢視畫面 (Filter view)】與【資料驗證下拉選單 (狀態)】
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            當多位老師共用同一張試算表時，「篩選器檢視畫面」能讓您<strong>只改變自己的螢幕畫面，完全不干擾其他正在看表的老師</strong>；而「資料驗證」則能建立統一的「狀態」下拉選單：
          </p>

          <div style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#1a73e8; margin-bottom:8px;">📷 建立專屬「math」篩選器檢視（頂部呈現深色/綠色外框）：</p>
              <img src="images/sheets_filter_view_math.png" alt="Google Sheets 篩選器檢視畫面" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">在此模式下篩選數學成績，其他共同編輯者的畫面完全不會跳動！</p>
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#1557b0; font-size:0.95rem;">💡 什麼是「狀態」欄位？為什麼要用資料驗證？</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>建立「狀態」欄位</strong>：在 <code>E1</code> 輸入「狀態」（或補救教學進度），用來標記學生輔導進度。</li>
                <li><strong>設定下拉式選單</strong>：選取 <code>E2:E6</code> ➔ 點「資料 ➔ 資料驗證」➔ 新增規則「下拉式選單」➔ 輸入 <code>未開始</code>、<code>進行中</code>、<code>已完成</code>。</li>
                <li><strong>防止格式混亂</strong>：避免老師們各自輸入「OK」、「完成」、「已補救」等不同寫法，確保後續可以用樞紐分析表精準統計！</li>
              </ul>
            </div>
          </div>
        </div>
'''

if 'sheets_filter_view_math.png' not in h_sheets and '<h2>篩選器檢視畫面 (Filter views) 與資料驗證 (Data validation) 保護共用表格</h2>' in h_sheets:
    h_sheets = h_sheets.replace('<h2>篩選器檢視畫面 (Filter views) 與資料驗證 (Data validation) 保護共用表格</h2>', '<h2>篩選器檢視畫面 (Filter views) 與資料驗證 (Data validation) 保護共用表格</h2>\n' + filter_view_card)
    print("Embedded filter view card in sheets_workshop_app.html!")

with open(p_sheets, 'w', encoding='utf-8') as f:
    f.write(h_sheets)

# Update Markdown manual Task 18
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_sheets_update = '''
##### 🔒 篩選器檢視畫面與資料驗證實務操作圖解
![Google Sheets 篩選器檢視畫面](../images/sheets_filter_view_math.png)
*圖 14：建立名為「math」的篩選器檢視，外框變色代表僅影響個人視角，不干擾他人*

> 💡 **「狀態」欄位操作說明**：
> 1. 在 `E1` 儲存格輸入 **「狀態」**（用來記錄補救教學或作業繳交進度）。
> 2. 選取 `E2:E6` 範圍，點選選單 **「資料 ➔ 資料驗證」**。
> 3. 規則選擇 **「下拉式選單」**，設定 `未開始`、`進行中`、`已完成` 三個固定選項，從源頭避免輸入混亂！
'''

if 'sheets_filter_view_math.png' not in h_md and '#### 演練 18' in h_md:
    h_md = h_md.replace('#### 演練 18', '#### 演練 18\n' + md_sheets_update)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded filter view in markdown manual!")

print("All Sheets documentation updated! Ready to deploy.")
