import shutil, os

src_img = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787116403572.png'
dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_img = os.path.join(dest_dir, 'gmail_search_options_ui_panel.png')
shutil.copy2(src_img, dst_img)
print("Copied Gmail search options UI panel image!")

operator_comparison_html = '''
        <!-- 🔍 圖形搜尋選單 vs 鍵盤運算子指令 一對一對照卡片 -->
        <div style="background:#ffffff; border:2px solid #1a73e8; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(26,115,232,0.1);">
          <h3 style="color:#1557b0; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            🔍 觀念解密：【圖形搜尋選單】vs【鍵盤運算子指令】一對一完全對照
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            您在搜尋列右側點開的<strong>「顯示搜尋選項面板」</strong>，與我們輸入的<strong>「運算子指令」</strong>效果 100% 相同！在 Google 認證考試與行政實務中，直接鍵入運算子可省下滑鼠一格一格填寫的時間：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px; align-items:center;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#1a73e8; margin-bottom:8px;">📷 點擊搜尋列右側展開的【搜尋選項面板】：</p>
              <img src="images/gmail_search_options_ui_panel.png" alt="Gmail 顯示搜尋選項面板" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="font-size:0.88rem; color:#202124; line-height:1.8;">
              <strong style="color:#1557b0; font-size:0.95rem;">⚡ 為什麼進階老師一定要學運算子？</strong>
              <ul style="padding-left:20px; color:#3c4043; margin-top:6px;">
                <li><strong>極速搜尋</strong>：不用動滑鼠，直接在搜尋框輸入 <code>from:教務處 has:attachment filename:pdf</code>，一秒精準撈出公文！</li>
                <li><strong>支援進階組合</strong>：支援 <code>OR</code>、<code>-</code> (排除) 等圖形介面難以設定的高階篩選。</li>
              </ul>
            </div>
          </div>

          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:0.88rem; background:#f8f9fa; border-radius:8px; overflow:hidden; border:1px solid #dadce0;">
              <thead>
                <tr style="background:#1a73e8; color:white;">
                  <th style="padding:9px 12px; text-align:left; width:30%;">圖形面板欄位 (滑鼠填表)</th>
                  <th style="padding:9px 12px; text-align:left; width:35%;">對應的搜尋運算子 (鍵盤指令)</th>
                  <th style="padding:9px 12px; text-align:left;">實務範例</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #e8eaed; background:white;">
                  <td style="padding:8px 12px; font-weight:600;">寄件者</td>
                  <td style="padding:8px 12px;"><code>from:</code></td>
                  <td style="padding:8px 12px; color:#5f6368;"><code>from:主任</code> 或 <code>from:apps.ntpc.edu.tw</code></td>
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
                  <td style="padding:8px 12px; color:#5f6368;"><code>larger:5M</code> (清理吃容量大信件)</td>
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

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

target_m4 = '<h2>善用搜尋運算子 (Search operators) 撈出多年前的信件與附件</h2>'
if target_m4 in h_gmail and 'gmail_search_options_ui_panel.png' not in h_gmail:
    h_gmail = h_gmail.replace(target_m4, target_m4 + '\n' + operator_comparison_html)
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded search comparison in gmail_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

# Target module 4 in hands_on_tasks_app.html
if 'gmail_search_options_ui_panel.png' not in h_tasks and '善用搜尋運算子' in h_tasks:
    h_tasks = h_tasks.replace('<h2>善用搜尋運算子', operator_comparison_html + '\n<h2>善用搜尋運算子')
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded search comparison in hands_on_tasks_app.html!")

# 3. Update markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_search_comp = '''
##### 🔍 觀念解密：【圖形搜尋選單】vs【鍵盤運算子指令】一對一完全對照
![Gmail 顯示搜尋選項面板](../images/gmail_search_options_ui_panel.png)
*圖 9：點擊搜尋列右側展開的「搜尋選項面板」各欄位與運算子指令 100% 對應*

| 圖形面板欄位 (滑鼠填表) | 對應的搜尋運算子 (鍵盤指令) | 實務範例說明 |
| :--- | :--- | :--- |
| **寄件者** | `from:` | `from:教務處` 或 `from:apps.ntpc.edu.tw` |
| **收件人** | `to:` | `to:家長會` |
| **主旨** | `subject:` | `subject:校外教學` |
| **包含字詞** | 直接輸入關鍵字 | `校務會議 提案` |
| **不包含字詞** | `-` (減號排除) | `-廣告 -促銷` |
| **勾選「有附件」** | `has:attachment` | `has:attachment filename:xlsx` |
| **大小大於** | `larger:` 或 `size:` | `larger:5M` (清理超大容量信件) |
| **日期範圍** | `after:` / `before:` | `after:2025/09/01 before:2026/01/20` |
'''

if 'gmail_search_options_ui_panel.png' not in h_md and '#### 演練 25' in h_md:
    h_md = h_md.replace('#### 演練 25', '#### 演練 25\n' + md_search_comp)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded search comparison in markdown manual!")

print("All files updated with search operators comparison!")
