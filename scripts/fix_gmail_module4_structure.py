import os

p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    html = f.read()

module4_perfect_html = '''      <!-- MODULE 4 -->
      <div class="module-card" id="module-4" style="display:none;">
        <span class="tag">核心功能演練四</span>
        <h2>善用搜尋運算子 (Search operators) 撈出多年前的信件與附件</h2>

        <p>把關鍵字丟進搜尋列常常撈出上百封。<strong>搜尋運算子</strong>能精確限定寄件者、時間範圍、是否有附件與檔案類型，是資深教師找回歷史資料最快的方式，也是 Level 2 的常考內容。</p>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          教育局來電索取前年校慶活動的核銷附件，您只記得是某位主任寄來的 Excel 檔，大概在十一月左右。信箱裡有兩萬封信，直接搜「校慶」會跳出幾百筆。
        </div>

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

        <div style="background:#e0f2f1; border:2px solid #00897b; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:#00695c; font-size:1.05rem;">🔨 本單元練習方式：從零自己建一次（不需要範本檔）</strong>
          </div>
          <div style="background:white; border:1px solid #80cbc4; border-radius:8px; padding:12px 16px; margin-top:8px;">
            <div style="font-size:0.95rem; color:#00695c; font-weight:700; line-height:1.6;">🎯 你要做的事：<span style="color:#202124; font-weight:500;">在自己的信箱依序試用下列運算子並記下結果筆數：<code>has:attachment</code>、<code>from:某人</code>、<code>after:2025/11/01 before:2025/12/01</code>、<code>filename:xlsx</code>、<code>larger:5M</code>，最後把它們組合成一條查詢。</span></div>
            <div style="font-size:0.88rem; color:#5f6368; margin-top:10px; line-height:1.6; border-top:1px dashed #80cbc4; padding-top:10px;">💬 運算子可以自由疊加，例如：<br><code>from:主任 has:attachment filename:xlsx after:2025/11/01 before:2025/12/01</code><br>——這一條就能把上面情境的信精準撈出來。找到後可點選<strong>「建立篩選器」</strong>把同類信件永久自動歸檔。</div>
          </div>
          <div style="margin-top:10px; font-size:0.82rem; color:#5f6368;">📎 <a href="https://docs.google.com/document/d/1L3tZLVdIW7qo1XRYRUc9w7vHSM0ay--qND3meTxBJVU/preview" target="_blank" rel="noopener" style="color:#5f6368;">情境補充說明文件（唯讀，Task 24）</a></div>
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m4-s1">
            <label for="m4-s1">在搜尋列輸入 <code>has:attachment</code>，只顯示含附件的信。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m4-s2">
            <label for="m4-s2">加上 <code>from:</code> 限定寄件者（可只打姓名關鍵字）。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m4-s3">
            <label for="m4-s3">加上 <code>after:2025/11/01 before:2025/12/01</code> 限定時間範圍。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m4-s4">
            <label for="m4-s4">加上 <code>filename:xlsx</code> 限定附件類型（或用 <code>larger:5M</code> 找大型檔案）。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m4-s5">
            <label for="m4-s5">（進階）用 <code>-</code> 排除關鍵字、<code>OR</code> 併聯條件，再點「建立篩選器」把規則存起來重複使用。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-4')">📋 複製本單元操作步驟</button>
        </div>
      </div>'''

start_m4 = html.find('<!-- MODULE 4 -->')
end_m4 = html.find('</main>')

if start_m4 != -1 and end_m4 != -1:
    new_html = html[:start_m4] + module4_perfect_html + '\n\n    ' + html[end_m4:]
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Fixed Module 4 completely and cleanly!")
