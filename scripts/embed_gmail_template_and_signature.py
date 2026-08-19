import os

p_gmail = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'gmail_workshop_app.html')
with open(p_gmail, 'r', encoding='utf-8') as f:
    h_gmail = f.read()

template_guide_html = '''
        <!-- 啟用範本截圖與簽名檔 vs 範本觀念對照卡 -->
        <div style="background:#ffffff; border:1.5px solid #1a73e8; border-radius:12px; padding:20px; margin:20px 0; box-shadow:0 3px 12px rgba(26,115,232,0.08);">
          <h3 style="color:#1557b0; margin-top:0; font-size:1.15rem; display:flex; align-items:center; gap:8px;">
            ⚙️ 步驟前置作業：在「進階」設定中啟用【範本 (Templates)】
          </h3>
          
          <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:14px; margin-bottom:16px; text-align:center;">
            <p style="font-weight:700; font-size:0.88rem; color:#1a73e8; margin-bottom:8px;">📷 進入【設定 ➔ 進階】將「範本」勾選為【啟用】，並點選最下方「儲存變更」：</p>
            <img src="images/gmail_advanced_templates_enable.png" alt="Gmail 進階設定啟用範本功能" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            <p style="font-size:0.8rem; color:#5f6368; margin-top:6px;">⚠️ 務必記得捲動到畫面最底部點擊<strong>「儲存變更」</strong>，重新載入 Gmail 後撰寫信件時才會出現範本選單！</p>
          </div>

          <div style="background:#fef7e0; border-left:4px solid #f9ab00; border-radius:0 8px 8px 0; padding:14px; font-size:0.9rem; line-height:1.7;">
            <div style="font-weight:700; color:#b06000; margin-bottom:6px;">💡 重要觀念辨析：每封信結尾的「自我介紹/簽名」是用範本嗎？</div>
            <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:0.88rem; background:white; border-radius:6px; overflow:hidden;">
              <tr style="background:#f1f3f4;">
                <th style="padding:8px 10px; text-align:left; width:22%;">功能類型</th>
                <th style="padding:8px 10px; text-align:left; width:33%;">設定路徑</th>
                <th style="padding:8px 10px; text-align:left;">最佳使用情境與效果</th>
              </tr>
              <tr style="border-top:1px solid #e8eaed;">
                <td style="padding:8px 10px; font-weight:700; color:#137333;">✍️ 簽名 (Signature)</td>
                <td style="padding:8px 10px; color:#5f6368;">設定 ➔ 一般設定 ➔ 簽名</td>
                <td style="padding:8px 10px; color:#202124;"><strong>每封信自動帶入結尾！</strong> 用於個人職稱、學校電話、分機、問候語與個人簡介。</td>
              </tr>
              <tr style="border-top:1px solid #e8eaed;">
                <td style="padding:8px 10px; font-weight:700; color:#1a73e8;">📋 範本 (Templates)</td>
                <td style="padding:8px 10px; color:#5f6368;">設定 ➔ 進階 ➔ 啟用範本<br>撰寫郵件 ➔ 右下角三點 ➔ 範本</td>
                <td style="padding:8px 10px; color:#202124;"><strong>整封信完整內文模板！</strong> 用於校外教學通知信、請假回覆、家長會通告，手動插入或搭配篩選器自動回信。</td>
              </tr>
            </table>
          </div>
        </div>
'''

target_m3 = '<h2>範本 (Templates) 與排程傳送 (Schedule send) 處理重複性回信</h2>'
if target_m3 in h_gmail and 'gmail_advanced_templates_enable.png' not in h_gmail:
    h_gmail = h_gmail.replace(target_m3, target_m3 + '\n' + template_guide_html)
    with open(p_gmail, 'w', encoding='utf-8') as f:
        f.write(h_gmail)
    print("Embedded template enable guide in gmail_workshop_app.html!")

# Update hands_on_tasks_app.html Task 25
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

target_task25 = '<span class="task-num">25</span>'
if target_task25 in h_tasks and 'gmail_advanced_templates_enable.png' not in h_tasks:
    # insert before <h3>▶️ 實作步驟導引清單
    idx = h_tasks.find(target_task25)
    step_idx = h_tasks.find('<h3>▶️ 實作步驟導引清單', idx)
    if step_idx != -1:
        h_tasks = h_tasks[:step_idx] + template_guide_html + '\n' + h_tasks[step_idx:]
        with open(p_tasks, 'w', encoding='utf-8') as f:
            f.write(h_tasks)
        print("Embedded template enable guide in hands_on_tasks_app.html!")
