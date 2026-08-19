import os

# Module 2 Component: Focused on "Create Filter" Action
module2_filter_card_html = '''
        <!-- 📂 演練二：透過搜尋選項面板【建立篩選器】自動歸檔 -->
        <div style="background:#ffffff; border:2px solid #00897b; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(0,137,123,0.1);">
          <h3 style="color:#00695c; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            ⚙️ 篩選器設定核心：在【搜尋面板】輸入條件 ➔ 點選「建立篩選器」
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            建立篩選器時，請點擊搜尋列右側的選項圖示展開條件面板。填好過濾規則後，<strong>請特別注意：不要點「搜尋」，而是點選藍色按鈕旁的「建立篩選器」</strong>：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#00695c; margin-bottom:8px;">📷 點擊搜尋列右側展開的【建立篩選器面板】：</p>
              <img src="images/gmail_search_options_ui_panel.png" alt="Gmail 顯示搜尋選項與建立篩選器面板" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">⚠️ 填寫完條件後，點擊右下角的<strong>「建立篩選器」</strong>按鈕！</p>
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#00695c; font-size:0.95rem;">🚀 點擊「建立篩選器」後的下一步常用動作：</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>✅ 套用標籤 (Apply the label)</strong>：例如將特定寄件者自動貼上「行政公文」或「家長聯絡」標籤。</li>
                <li><strong>✅ 略過收件匣 (Skip the Inbox)</strong>：系統通知或常態報表自動封存歸檔，不再干擾收件匣。</li>
                <li><strong>✅ 標示為已讀 (Mark as read)</strong> / <strong>標示為星號 (Star it)</strong>：重要主管來信自動標星。</li>
                <li><strong>✅ 同時套用至相符的會話群組</strong>：將信箱裡過去已收到的舊信一次全部歸檔！</li>
              </ul>
            </div>
          </div>
        </div>
'''

# Module 4 Component: Search Operators 1-to-1 Mapping with the UI Panel
module4_operators_card_html = '''
        <!-- 🔍 演練四：圖形搜尋選單 vs 鍵盤運算子指令 一對一完全對照 -->
        <div style="background:#ffffff; border:2px solid #1a73e8; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(26,115,232,0.1);">
          <h3 style="color:#1557b0; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            🔍 觀念解密：【圖形搜尋面板欄位】vs【鍵盤運算子指令】一對一完全對照
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            許多老師習慣點開搜尋面板一格一格填寫，但其實<strong>運算子指令就是圖形面板各欄位的鍵盤快速語法</strong>！在 Google 認證 Level 2 考試與大量行政處理中，直接在搜尋框鍵入運算子可大幅提升效率：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#1a73e8; margin-bottom:8px;">📷 圖形面板（滑鼠填寫各欄位）：</p>
              <img src="images/gmail_search_options_ui_panel.png" alt="Gmail 顯示搜尋選項面板" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#1557b0; font-size:0.95rem;">⚡ 運算子的超強進階威力：</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>鍵盤秒搜</strong>：直接輸入 <code>from:主任 has:attachment filename:xlsx</code>，省去滑鼠開選單與點選時間。</li>
                <li><strong>邏輯組合</strong>：支援 <code>OR</code>、<code>-</code> (減號排除)、<code>larger:5M</code> 等複合精準過濾。</li>
              </ul>
            </div>
          </div>

          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#f8f9fa; border-radius:8px; overflow:hidden; border:1px solid #dadce0;">
              <thead>
                <tr style="background:#1a73e8; color:white;">
                  <th style="padding:9px 12px; text-align:left; width:28%;">圖形面板欄位 (滑鼠填表)</th>
                  <th style="padding:9px 12px; text-align:left; width:34%;">對應的搜尋運算子 (鍵盤指令)</th>
                  <th style="padding:9px 12px; text-align:left;">實務指令範例說明</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">寄件者</td>
                  <td style="padding:8px 12px;"><code>from:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>from:教務處</code> 或 <code>from:apps.ntpc.edu.tw</code></td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed;">
                  <td style="padding:8px 12px; font-weight:600;">收件人</td>
                  <td style="padding:8px 12px;"><code>to:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>to:家長會</code></td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">主旨</td>
                  <td style="padding:8px 12px;"><code>subject:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>subject:校外教學</code></td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed;">
                  <td style="padding:8px 12px; font-weight:600;">包含字詞</td>
                  <td style="padding:8px 12px;">直接輸入關鍵字</td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>校務會議 提案</code></td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">不包含字詞</td>
                  <td style="padding:8px 12px;"><code>-</code> (減號排除)</td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>-廣告 -促銷</code></td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed;">
                  <td style="padding:8px 12px; font-weight:600;">勾選「有附件」</td>
                  <td style="padding:8px 12px;"><code>has:attachment</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>has:attachment filename:xlsx</code></td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">大小大於</td>
                  <td style="padding:8px 12px;"><code>larger:</code> 或 <code>size:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>larger:5M</code> (快速撈出吃空間的大信件)</td>
                </tr>
                <tr>
                  <td style="padding:8px 12px; font-weight:600;">日期範圍</td>
                  <td style="padding:8px 12px;"><code>after:</code> / <code>before:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>after:2025/09/01 before:2026/01/20</code></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
'''

# Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

# Replace in Module 2
target_m2_start = '<!-- 🔍 透過搜尋選項面板建立篩選器 圖文對照卡片 -->'
idx_m2_start = h_gmail.find(target_m2_start)
if idx_m2_start != -1:
    idx_m2_end = h_gmail.find('</div>\n        </div>', idx_m2_start)
    if idx_m2_end != -1:
        h_gmail = h_gmail[:idx_m2_start] + module2_filter_card_html + h_gmail[idx_m2_end + 15:]

# Add into Module 4
target_m4_head = '<h2>善用搜尋運算子 (Search operators) 撈出多年前的信件與附件</h2>'
if target_m4_head in h_gmail and '觀念解密：【圖形搜尋面板欄位】vs【鍵盤運算子指令】' not in h_gmail:
    h_gmail = h_gmail.replace(target_m4_head, target_m4_head + '\n' + module4_operators_card_html)

with open(p_gmail, 'w', encoding='utf-8') as f:
    f.write(h_gmail)
print("Updated gmail_workshop_app.html with perfect Module 2 and Module 4 structure!")

# Update Markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_aligned = '''
##### ⚙️ 演練二篩選器設定：在【搜尋面板】輸入條件 ➔ 點選「建立篩選器」
![Gmail 顯示搜尋選項與建立篩選器面板](../images/gmail_search_options_ui_panel.png)
*圖 9：填寫篩選條件後，點選右下角「建立篩選器」按鈕進行自動貼標籤與歸檔*

##### 🔍 演練四搜尋運算子解密：【圖形面板欄位】vs【鍵盤運算子指令】完全對照
| 圖形面板欄位 (滑鼠填表) | 對應的搜尋運算子 (鍵盤指令) | 實務指令範例說明 |
| :--- | :--- | :--- |
| **寄件者** | `from:` | `from:教務處` 或 `from:apps.ntpc.edu.tw` |
| **收件人** | `to:` | `to:家長會` |
| **主旨** | `subject:` | `subject:校外教學` |
| **包含字詞** | 直接輸入關鍵字 | `校務會議 提案` |
| **不包含字詞** | `-` (減號排除) | `-廣告 -促銷` |
| **勾選「有附件」** | `has:attachment` | `has:attachment filename:xlsx` |
| **大小大於** | `larger:` 或 `size:` | `larger:5M` (快速撈出吃空間的大信件) |
| **日期範圍** | `after:` / `before:` | `after:2025/09/01 before:2026/01/20` |
'''

if '##### ⚙️ 篩選器設定前置：' in h_md:
    target_md_sec = '##### ⚙️ 篩選器設定前置：'
    idx_m = h_md.find(target_md_sec)
    end_m = h_md.find('- **🎯 實務情境課題**', idx_m)
    if end_m != -1:
        h_md = h_md[:idx_m] + md_aligned + '\n' + h_md[end_m:]
        with open(p_md, 'w', encoding='utf-8') as f:
            f.write(h_md)
        print("Updated markdown manual!")

print("All aligned! Ready to deploy to GitHub Pages.")
