import os

filter_panel_module2_html = '''
        <!-- 🔍 透過搜尋選項面板建立篩選器 圖文對照卡片 -->
        <div style="background:#ffffff; border:2px solid #00897b; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(0,137,123,0.1);">
          <h3 style="color:#00695c; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            ⚙️ 篩選器設定前置：透過【搜尋選項面板】設定條件 ➔ 點選「建立篩選器」
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            建立篩選器的第一步，就是點擊搜尋列右側的選項圖示展開<strong>「搜尋條件面板」</strong>。填寫完過濾規則後，<strong>請勿點「搜尋」，而是點選右下角的「建立篩選器」</strong>：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#00695c; margin-bottom:8px;">📷 點擊搜尋列右側展開的【篩選條件面板】：</p>
              <img src="images/gmail_search_options_ui_panel.png" alt="Gmail 顯示搜尋選項與建立篩選器面板" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
              <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">⚠️ 設定好條件後，記得點藍色按鈕旁的<strong>「建立篩選器」</strong>！</p>
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#00695c; font-size:0.95rem;">💡 各欄位常用篩選情境：</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>寄件者 (from:)</strong>：填入 <code>教務處</code>、<code>校長信箱</code> 或特定系統通知信箱。</li>
                <li><strong>主旨 (subject:)</strong>：填入 <code>[研習]</code>、<code>[請假]</code>、<code>[社群]</code> 等常態標題關鍵字。</li>
                <li><strong>包含字詞</strong>：填入 <code>成績單</code>、<code>調代課</code> 自動進行分類。</li>
                <li><strong>勾選「有附件」</strong>：專門將帶有檔案的公文信件自動歸檔。</li>
              </ul>
            </div>
          </div>

          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#f8f9fa; border-radius:8px; overflow:hidden; border:1px solid #dadce0;">
              <thead>
                <tr style="background:#00695c; color:white;">
                  <th style="padding:9px 12px; text-align:left; width:30%;">篩選面板欄位</th>
                  <th style="padding:9px 12px; text-align:left; width:35%;">對應的運算子語法</th>
                  <th style="padding:9px 12px; text-align:left;">常見行政/教學套用規則</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">寄件者</td>
                  <td style="padding:8px 12px;"><code>from:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;">收到主管/教育局來信 ➔ 自動標示為重要並加上星號</td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed;">
                  <td style="padding:8px 12px; font-weight:600;">收件人</td>
                  <td style="padding:8px 12px;"><code>to:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;">群組郵件群發 ➔ 自動套用「各處室公告」標籤</td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">主旨</td>
                  <td style="padding:8px 12px;"><code>subject:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;">主旨含「研習」 ➔ 自動貼上「教師研習」綠色標籤</td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed;">
                  <td style="padding:8px 12px; font-weight:600;">包含字詞</td>
                  <td style="padding:8px 12px;">直接輸入關鍵字</td>
                  <td style="padding:8px 12px; color:#5f6368;">包含「校外教學 回條」 ➔ 集中歸檔</td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">不包含字詞</td>
                  <td style="padding:8px 12px;"><code>-</code> (減號排除)</td>
                  <td style="padding:8px 12px; color:#5f6368;">排除廣告或垃圾信</td>
                </tr>
                <tr style="border-bottom:1px solid #e8eaed;">
                  <td style="padding:8px 12px; font-weight:600;">勾選「有附件」</td>
                  <td style="padding:8px 12px;"><code>has:attachment</code></td>
                  <td style="padding:8px 12px; color:#5f6368;">含附件之公文 ➔ 自動套用「公文附件」標籤</td>
                </tr>
                <tr>
                  <td style="padding:8px 12px; font-weight:600;">大小大於</td>
                  <td style="padding:8px 12px;"><code>larger:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>larger:10M</code> ➔ 自動標記大容量檔案便於後續清理</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
'''

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

# Remove from Module 4
target_m4_panel = '<!-- 🔍 圖形搜尋選單 vs 鍵盤運算子指令 一對一對照卡片 -->'
idx_m4 = h_gmail.find(target_m4_panel)
if idx_m4 != -1:
    end_m4 = h_gmail.find('</div>\n        </div>', idx_m4)
    if end_m4 != -1:
        h_gmail = h_gmail[:idx_m4] + h_gmail[end_m4 + 15:]
        print("Removed search panel from Module 4 in gmail_workshop_app.html!")

# Insert into Module 2 (under <h2>建立篩選器 (Filters) 與標籤 (Labels) 讓信件自動歸位</h2>)
target_m2_heading = '<h2>建立篩選器 (Filters) 與標籤 (Labels) 讓信件自動歸位</h2>'
if target_m2_heading in h_gmail and '透過【搜尋選項面板】設定條件' not in h_gmail:
    h_gmail = h_gmail.replace(target_m2_heading, target_m2_heading + '\n' + filter_panel_module2_html)
    print("Inserted filter panel into Module 2 in gmail_workshop_app.html!")

with open(p_gmail, 'w', encoding='utf-8') as f:
    f.write(h_gmail)

# 2. Update markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

# Update Markdown Task 24 or Task for filters
# Let's replace the heading in markdown
if '##### 🔍 觀念解密：【圖形搜尋選單】vs【鍵盤運算子指令】一對一完全對照' in h_md:
    h_md = h_md.replace('##### 🔍 觀念解密：【圖形搜尋選單】vs【鍵盤運算子指令】一對一完全對照', '##### ⚙️ 篩選器設定前置：透過【搜尋選項面板】設定條件 ➔ 點選「建立篩選器」')
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Updated markdown manual!")

print("Correction applied! Ready to deploy to GitHub Pages.")
