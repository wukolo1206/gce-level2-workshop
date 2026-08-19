import os

# Build rich comparison and template sample component
signature_template_deep_dive_html = '''
        <!-- ✍️ 簽名檔 vs 📋 範本 深度解析與實戰對照卡片 -->
        <div style="background:#ffffff; border:2px solid #00897b; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(0,137,123,0.1);">
          <h3 style="color:#00695c; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            ⚖️ 關鍵觀念深度解析：【✍️ 簽名檔 (Signature)】vs【📋 範本 (Templates)】
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            在學校行政與教學日常中，老師們常常容易混淆這兩項功能。其實只要記住一句話：<strong>「每封信結尾自動帶入的叫『簽名檔』；整篇完整信件內容重複叫出的叫『範本』！」</strong>
          </p>

          <div style="overflow-x:auto; margin-bottom:18px;">
            <table style="width:100%; border-collapse:collapse; font-size:0.9rem; background:#f8fdfc; border-radius:8px; overflow:hidden; border:1px solid #b2dfdb;">
              <thead>
                <tr style="background:#00695c; color:white;">
                  <th style="padding:10px 12px; text-align:left; width:22%;">比較面向</th>
                  <th style="padding:10px 12px; text-align:left; width:39%;">✍️ 簽名檔 (Signature)</th>
                  <th style="padding:10px 12px; text-align:left; width:39%;">📋 範本 (Templates / 舊稱罐頭回應)</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #e0f2f1;">
                  <td style="padding:10px 12px; font-weight:700; color:#00695c;">📍 設定路徑</td>
                  <td style="padding:10px 12px;"><code>設定 ➔ 一般設定 ➔ 簽名</code></td>
                  <td style="padding:10px 12px;"><code>設定 ➔ 進階 ➔ 啟用範本</code><br><span style="font-size:0.82rem; color:#5f6368;">（撰寫信件時：右下角三點 ➔ 範本）</span></td>
                </tr>
                <tr style="border-bottom:1px solid #e0f2f1; background:#ffffff;">
                  <td style="padding:10px 12px; font-weight:700; color:#00695c;">⚡ 觸發方式</td>
                  <td style="padding:10px 12px;"><span style="color:#137333; font-weight:700;">自動產生</span>：只要按「撰寫」或「回覆」，信件最底端自動帶出。</td>
                  <td style="padding:10px 12px;"><span style="color:#1a73e8; font-weight:700;">手動插入 / 規則觸發</span>：寫信時手動點選套用，或由篩選器自動回信。</td>
                </tr>
                <tr style="border-bottom:1px solid #e0f2f1;">
                  <td style="padding:10px 12px; font-weight:700; color:#00695c;">📝 內容性質</td>
                  <td style="padding:10px 12px;"><strong>個人資訊與名片</strong>：職稱、學校電話、分機、公務信箱、問候結語、學校 Logo。</td>
                  <td style="padding:10px 12px;"><strong>整篇完整信件內文</strong>：包含主旨、開頭稱謂、條列注意事項、常見問題解答。</td>
                </tr>
                <tr style="background:#ffffff;">
                  <td style="padding:10px 12px; font-weight:700; color:#00695c;">🏫 學校應用實例</td>
                  <td style="padding:10px 12px;">教務處組長名片、導師聯絡資訊、免責聲明。</td>
                  <td style="padding:10px 12px;">戶外教育通知信、請假缺補課流程回覆、家長會常態詢問答覆。</td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- 實戰範本演練文章展示區 -->
          <div style="background:#e8f5e9; border:1.5px solid #81c784; border-radius:8px; padding:16px; margin-top:14px;">
            <div style="font-weight:700; color:#2e7d32; font-size:0.95rem; margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">
              <span>📋 演練三推薦範本文章（點擊直接複製，即可建立您的第一個 Gmail 範本）：</span>
            </div>
            
            <div style="background:white; border:1px solid #c8e6c9; border-radius:6px; padding:14px; font-size:0.88rem; line-height:1.7; color:#202124; font-family:inherit;">
              <strong style="color:#1557b0;">【信件主旨】：</strong>【重要通知】○○國小 ○年○班 校外教學行前準備與注意事項通知<br><br>
              各位家長好：<br><br>
              本學期班級校外教學參訪活動即將於下週舉行，為了讓孩子們能有充實且安全的學習體驗，請家長協助提醒與準備以下事項：<br><br>
              📍 <strong>【活動資訊】</strong><br>
              1. 集合時間：○月○日（星期○）上午 07:50 前於教室集合完畢<br>
              2. 參訪地點：新北市立十三行博物館<br>
              3. 預計返校：下午 15:30（依當天交通路況為準）<br><br>
              🎒 <strong>【必備隨身物品】</strong><br>
              • 穿著學校體育服、運動鞋<br>
              • 輕便雙肩背包（裝水壺、輕便雨衣、個人常備藥品）<br>
              • 健保卡、悠遊卡（請先儲值）<br><br>
              若當天有任何突發狀況需請假，請於 07:30 前透過班級官方管道或撥打學校分機告知導師。<br>
              感謝家長的配合與支持！<br><br>
              導師 敬上
            </div>
            <p style="font-size:0.8rem; color:#5f6368; margin-top:8px; margin-bottom:0;">
              💡 <strong>操作提示</strong>：複製上方整段文章，在 Gmail 點「撰寫」貼上主旨與內文，再點右下角 <code>三點 ➔ 範本 ➔ 將草稿儲存為範本 ➔ 另存為新範本</code> 即可！
            </p>
          </div>
        </div>
'''

# 1. Update gmail_workshop_app.html
p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

# Replace previous brief table with the comprehensive deep dive
target_old = '<!-- 啟用範本截圖與簽名檔 vs 範本觀念對照卡 -->'
idx_old = h_gmail.find(target_old)
if idx_old != -1:
    end_old = h_gmail.find('</div>\n        </div>', idx_old)
    if end_old != -1:
        h_gmail = h_gmail[:idx_old] + signature_template_deep_dive_html + h_gmail[end_old + 15:]
        with open(p_gmail, 'w', encoding='utf-8') as f:
            f.write(h_gmail)
        print("Updated gmail_workshop_app.html with deep dive!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

idx_tasks = h_tasks.find(target_old)
if idx_tasks != -1:
    end_tasks = h_tasks.find('</div>\n        </div>', idx_tasks)
    if end_tasks != -1:
        h_tasks = h_tasks[:idx_tasks] + signature_template_deep_dive_html + h_tasks[end_tasks + 15:]
        with open(p_tasks, 'w', encoding='utf-8') as f:
            f.write(h_tasks)
        print("Updated hands_on_tasks_app.html with deep dive!")

# 3. Update markdown manual
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_deep_dive = '''
##### ⚖️ 關鍵觀念深度解析：【✍️ 簽名檔 (Signature)】vs【📋 範本 (Templates)】
> **一句話辨析**：「每封信結尾自動帶入的叫『簽名檔』；整篇完整信件內容重複叫出的叫『範本』！」

| 比較面向 | ✍️ 簽名檔 (Signature) | 📋 範本 (Templates / 舊稱罐頭回應) |
| :--- | :--- | :--- |
| **📍 設定路徑** | `設定 ➔ 一般設定 ➔ 簽名` | `設定 ➔ 進階 ➔ 啟用範本`<br>（撰寫時：右下角三點 ➔ 範本） |
| **⚡ 觸發方式** | **自動產生**：按撰寫或回覆時自動附加於信末 | **手動插入 / 規則觸發**：手動套用或由篩選器自動回信 |
| **📝 內容性質** | **名片資訊**：姓名、職稱、分機、Logo、問候語 | **整篇完整文章**：主旨、正文、條列事項、常見問答 |
| **🏫 學校應用** | 行政名片、導師聯絡資訊、免責聲明 | 校外教學通告、請假補課流程、家長會常態詢問 |

##### 📋 演練三推薦範本文章（校外教學行前準備通告）：
- **主旨**：`【重要通知】○○國小 ○年○班 校外教學行前準備與注意事項通知`
- **內文**：
  > 各位家長好：<br>
  > 本學期班級校外教學參訪活動即將於下週舉行，為了讓孩子們能有充實且安全的學習體驗，請家長協助提醒與準備以下事項：<br><br>
  > 📍 **【活動資訊】**<br>
  > 1. 集合時間：○月○日（星期○）上午 07:50 前於教室集合完畢<br>
  > 2. 參訪地點：新北市立十三行博物館<br>
  > 3. 預計返校：下午 15:30（依當天交通路況為準）<br><br>
  > 🎒 **【必備隨身物品】**<br>
  > • 穿著學校體育服、運動鞋<br>
  > • 輕便雙肩背包（裝水壺、輕便雨衣、個人常備藥品）<br>
  > • 健保卡、悠遊卡（請先儲值）<br><br>
  > 若當天有任何突發狀況需請假，請於 07:30 前透過班級官方管道或撥打學校分機告知導師。<br>
  > 感謝家長的配合與支持！<br><br>
  > 導師 敬上
'''

if '⚖️ 關鍵觀念深度解析：【✍️ 簽名檔 (Signature)】vs【📋 範本 (Templates)】' not in h_md:
    target_md_old = '> 💡 **重要觀念辨析：每封信結尾的「自我介紹/簽名」是用範本嗎？**'
    idx_md_old = h_md.find(target_md_old)
    if idx_md_old != -1:
        end_md_old = h_md.find('- **🎯 實務情境課題**', idx_md_old)
        if end_md_old != -1:
            h_md = h_md[:idx_md_old] + md_deep_dive + '\n' + h_md[end_md_old:]
            with open(p_md, 'w', encoding='utf-8') as f:
                f.write(h_md)
            print("Updated markdown manual with deep dive!")

print("All signature vs template comparisons and template text updated!")
