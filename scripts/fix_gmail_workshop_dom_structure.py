import re

with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\gmail_workshop_app.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect Module 2 clean definition
module2_clean = '''      <!-- MODULE 2 -->
      <div class="module-card" id="module-2" style="display:none;">
        <span class="tag">核心功能演練二</span>
        <h2>建立篩選器 (Filters) 與標籤 (Labels) 讓信件自動歸位</h2>

        <p>Gmail 沒有「資料夾」，只有可以<strong>一封信同時貼多個</strong>的標籤。篩選器則是規則引擎：符合條件的來信可自動貼標籤、自動標為已讀、自動略過收件匣、甚至自動轉寄。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          您同時是導師與研習承辦人，收件匣裡混雜著家長信件、系統通知、各校研習公文與學生作業繳交通知。每天早上要花十分鐘從一堆信裡挑出真正需要回覆的那幾封。
        </div>

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

        <div style="background:#e0f2f1; border:2px solid #00897b; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:#00695c; font-size:1.05rem;">🔨 本單元練習方式：從零自己建一次（不需要範本檔）</strong>
          </div>
          <div style="background:white; border:1px solid #80cbc4; border-radius:8px; padding:12px 16px; margin-top:8px;">
            <div style="font-size:0.95rem; color:#00695c; font-weight:700; line-height:1.6;">🎯 你要做的事：<span style="color:#202124; font-weight:500;">在自己的 Gmail 建立一個「家長來信」標籤與對應篩選器，並勾選「略過收件匣」與「一律標示為重要」，再用「套用至相符的對話」把過去的信一次歸位。</span></div>
            <div style="font-size:0.88rem; color:#5f6368; margin-top:10px; line-height:1.6; border-top:1px dashed #80cbc4; padding-top:10px;">💬 最實用的一招是勾選<strong>「同時套用篩選器至 N 個相符的對話」</strong>——規則建立的當下就把過去幾年的舊信一次分類完，不必手動整理。</div>
          </div>
          <div style="margin-top:10px; font-size:0.82rem; color:#5f6368;">📎 <a href="https://docs.google.com/document/d/1L3tZLVdIW7qo1XRYRUc9w7vHSM0ay--qND3meTxBJVU/preview" target="_blank" rel="noopener" style="color:#5f6368;">情境補充說明文件（唯讀，Task 24）</a></div>
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m2-s1">
            <label for="m2-s1">在搜尋列右側點選<strong>篩選器圖示</strong>，輸入條件（如寄件者網域、主旨含「請假」）。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m2-s2">
            <label for="m2-s2">點選 <strong>「建立篩選器」</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m2-s3">
            <label for="m2-s3">勾選要執行的動作：<strong>套用標籤</strong>（可當場新增）、<strong>略過收件匣</strong>、標示為重要。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m2-s4">
            <label for="m2-s4">勾選 <strong>「同時套用篩選器至 N 個相符的對話」</strong>，讓舊信一併歸位。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m2-s5">
            <label for="m2-s5">驗證：左側標籤列出現該標籤與未讀數，收件匣乾淨許多。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-2')">📋 複製本單元操作步驟</button>
        </div>
      </div>'''

# Module 3 clean definition
module3_clean = '''      <!-- MODULE 3 -->
      <div class="module-card" id="module-3" style="display:none;">
        <span class="tag">核心功能演練三</span>
        <h2>範本 (Templates) 與排程傳送 (Schedule send) 處理重複性回信</h2>

        <p>範本（舊稱罐頭回應）需先到<strong>「設定 ➔ 進階」啟用</strong>才會出現，啟用後可把常用回覆存起來一鍵插入；排程傳送則讓你在方便的時候寫信、在恰當的時間寄出。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          每學期初，您都要回覆數十封內容幾乎相同的家長詢問信（課後輔導時間、聯絡方式、請假流程）。此外，您常在深夜十一點整理完班務，但不希望信件在那個時間寄到家長手機上。
        </div>

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

          <!-- 8. 實務操作：在信件中儲存與插入範本 -->
          <div style="background:#f8f9fa; border:1.5px solid #1a73e8; border-radius:10px; padding:16px; margin-top:16px;">
            <p style="font-weight:700; font-size:0.92rem; color:#1557b0; margin-bottom:8px;">
              📷 8. 實務操作：撰寫信件時，由右下角【三點選單 ➔ 範本】儲存或套用：
            </p>
            <div style="background:white; border:1px solid #c2e7ff; border-radius:8px; padding:12px; text-align:center; margin-bottom:10px;">
              <img src="images/gmail_save_and_insert_template_menu.png" alt="Gmail 撰寫信件儲存與套用範本選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="font-size:0.9rem; color:#202124; line-height:1.7;">
              🎯 <strong>標準兩步驟</strong>：
              <ul style="padding-left:20px; color:#3c4043; margin-top:4px;">
                <li><strong>儲存為新範本</strong>：草稿打好後 ➔ 點右下角 <code>三點 ➔ 範本 ➔ 將草稿儲存為範本 ➔ 另存為新範本</code>。</li>
                <li><strong>未來一鍵插入</strong>：開新信時 ➔ 點右下角 <code>三點 ➔ 範本 ➔ 點選「校外教學通知」</code> 即可瞬間填滿！</li>
              </ul>
            </div>
          </div>
        </div>

        <div style="background:#e0f2f1; border:2px solid #00897b; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:#00695c; font-size:1.05rem;">🔨 本單元練習方式：從零自己建一次（不需要範本檔）</strong>
          </div>
          <div style="background:white; border:1px solid #80cbc4; border-radius:8px; padding:12px 16px; margin-top:8px;">
            <div style="font-size:0.95rem; color:#00695c; font-weight:700; line-height:1.6;">🎯 你要做的事：<span style="color:#202124; font-weight:500;">啟用「範本」功能，把一段常用的家長回覆存成範本，然後寫一封新信套用該範本，並用「排程傳送」指定明天早上 8:00 寄出。</span></div>
            <div style="font-size:0.88rem; color:#5f6368; margin-top:10px; line-height:1.6; border-top:1px dashed #80cbc4; padding-top:10px;">💬 排程中的信件會待在<strong>「已排程」</strong>資料夾，寄出前都還能取消或修改——這也是避免深夜擾民、又不會忘記寄的最佳作法。</div>
          </div>
          <div style="margin-top:10px; font-size:0.82rem; color:#5f6368;">📎 <a href="https://docs.google.com/document/d/1L3tZLVdIW7qo1XRYRUc9w7vHSM0ay--qND3meTxBJVU/preview" target="_blank" rel="noopener" style="color:#5f6368;">情境補充說明文件（唯讀，Task 24）</a></div>
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m3-s1">
            <label for="m3-s1">點選<strong>齒輪 ➔ 查看所有設定 ➔ 「進階 (Advanced)」</strong>分頁，將 <strong>「範本」設為啟用</strong>並儲存。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m3-s2">
            <label for="m3-s2">撰寫一封信，輸入常用回覆內容，點選右下角<strong>三點圖示 ➔ 「範本 ➔ 將草稿儲存為範本」</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m3-s3">
            <label for="m3-s3">開新信件，由同一選單<strong>插入剛才的範本</strong>，僅修改稱謂與個別內容。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m3-s4">
            <label for="m3-s4">點選「傳送」旁的<strong>下拉箭頭 ➔ 「排程傳送 (Schedule send)」</strong>，指定明天 8:00。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m3-s5">
            <label for="m3-s5">到左側 <strong>「已排程」</strong> 資料夾確認信件在列，並試著取消排程。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-3')">📋 複製本單元操作步驟</button>
        </div>
      </div>'''

# Replace from MODULE 2 to MODULE 4 in html
start_m2 = html.find('<!-- MODULE 2 -->')
start_m4 = html.find('<!-- MODULE 4 -->')

if start_m2 != -1 and start_m4 != -1:
    new_html = html[:start_m2] + module2_clean + '\n\n' + module3_clean + '\n\n      ' + html[start_m4:]
    with open(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\gmail_workshop_app.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Fixed premature closing div tags in gmail_workshop_app.html successfully!")
