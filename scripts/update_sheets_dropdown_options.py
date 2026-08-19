import shutil, os

# 1. Save user's latest screenshot showing the dropdown in action
src_img = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787151056253.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_img = os.path.join(dest_dir, 'sheets_data_validation_status_dropdown.png')
shutil.copy2(src_img, dst_img)
print("Copied Sheets data validation dropdown image!")

# 2. Updated Card HTML for sheets_workshop_app.html
new_module3_card = '''        <!-- 🔒 篩選器檢視畫面 vs 資料驗證【考卷訂正追蹤】下拉選單解析 -->
        <div style="background:#ffffff; border:2px solid #1a73e8; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(26,115,232,0.1);">
          <h3 style="color:#1557b0; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            🔒 實作圖解：【篩選器檢視畫面】與【考卷訂正追蹤下拉選單 (資料驗證)】
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            當多位任課老師共用同一張成績單時，「篩選器檢視」讓您<strong>只篩選自己要看的科目（不跳掉他人螢幕）</strong>；「資料驗證」則可在成績後方建立<strong>「考卷訂正追蹤」</strong>下拉選單：
          </p>

          <div style="display:grid; grid-template-columns:1.1fr 0.9fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#1a73e8; margin-bottom:8px;">📷 成果展示：E 欄「考卷訂正追蹤」下拉選單晶片：</p>
              <img src="images/sheets_data_validation_status_dropdown.png" alt="Google Sheets 考卷訂正狀態資料驗證下拉選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">頂部 math 專屬檢視 + E 欄標準化訂正選項，防呆又防干擾！</p>
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#1557b0; font-size:0.95rem;">💡 為什麼成績後面要設【考卷訂正追蹤】？</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>學校實務情境</strong>：期中考後，老師需追蹤不及格學生的訂正進度，在 <code>E1</code> 建立「考卷訂正狀態」。</li>
                <li><strong>統一 3 大標準選項</strong>：設定下拉選單為 <code>未訂正</code>、<code>訂正中</code>、<code>已訂正過關</code>。</li>
                <li><strong>避免文字混亂</strong>：防止每位老師各打各的（有人寫 OK、有人寫完成），確保可用樞紐分析表一秒統計出「全班還有幾人未訂正」！</li>
              </ul>
            </div>
          </div>
        </div>'''

p_sheets = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'sheets_workshop_app.html')
with open(p_sheets, 'r', encoding='utf-8') as f:
    h_sheets = f.read()

# Replace the previous card in Module 3
target_card_start = '<!-- 🔒 篩選器檢視畫面 vs 一般篩選器 & 資料驗證下拉選單解析 -->'
target_card_end = '<!-- MODULE 3 -->'
idx_c_start = h_sheets.find(target_card_start)
if idx_c_start != -1:
    idx_c_end = h_sheets.find('</div>\n        </div>', idx_c_start)
    if idx_c_end != -1:
        h_sheets = h_sheets[:idx_c_start] + new_module3_card + h_sheets[idx_c_end + 15:]

# Update target text and steps
h_sheets = h_sheets.replace('學年共用一張「補救教學名單」試算表', '學年共用一張「期中測驗成績單」試算表進行考卷訂正與補救追蹤')
h_sheets = h_sheets.replace('在 <strong>E1 儲存格輸入「狀態」</strong>（用來追蹤補救進度）', '在 <strong>E1 儲存格輸入「考卷訂正狀態」</strong>（用來追蹤學生訂正進度）')
h_sheets = h_sheets.replace('輸入固定選項（如：未開始／進行中／已完成）', '輸入 3 個固定選項：<code>未訂正</code> ／ <code>訂正中</code> ／ <code>已訂正過關</code>')
h_sheets = h_sheets.replace('對狀態欄位設定「資料驗證 ➔ 下拉式選單」限定選項', '在 E 欄設定「考卷訂正追蹤」下拉選單（未訂正／訂正中／已訂正過關）')

with open(p_sheets, 'w', encoding='utf-8') as f:
    f.write(h_sheets)
print("Updated sheets_workshop_app.html with 考卷訂正追蹤 options!")

# 3. Update markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_sheets_new = '''##### 🔒 篩選器檢視畫面與【考卷訂正追蹤】資料驗證實務圖解
![Google Sheets 考卷訂正狀態資料驗證下拉選單](../images/sheets_data_validation_status_dropdown.png)
*圖 14：建立名為「math」的篩選器檢視，搭配 E 欄「考卷訂正追蹤」下拉選單（未訂正／訂正中／已訂正過關）*

> 💡 **【考卷訂正追蹤】資料驗證操作指引**：
> 1. 在 `E1` 儲存格輸入 **「考卷訂正狀態」**。
> 2. 選取 `E2:E6` 範圍，點選選單 **「資料 ➔ 資料驗證」**（或「插入 ➔ 下拉式選單」）。
> 3. 規則選擇 **「下拉式選單」**，設定 `未訂正`（紅色）、`訂正中`（黃色）、`已訂正過關`（綠色）三個選項，從源頭杜絕各班寫法混亂！
'''

if '##### 🔒 篩選器檢視畫面與資料驗證實務操作圖解' in h_md:
    idx_m_s = h_md.find('##### 🔒 篩選器檢視畫面與資料驗證實務操作圖解')
    idx_m_e = h_md.find('- **🎓 Google 認證', idx_m_s)
    if idx_m_e == -1:
        idx_m_e = h_md.find('- **▶️ 手把手', idx_m_s)
    if idx_m_e != -1:
        h_md = h_md[:idx_m_s] + md_sheets_new + '\n' + h_md[idx_m_e:]
        with open(p_md, 'w', encoding='utf-8') as f:
            f.write(h_md)
        print("Updated markdown manual!")

print("All files updated with 考卷訂正追蹤! Ready to deploy.")
