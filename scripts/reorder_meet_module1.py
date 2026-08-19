import os

p_meet = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'meet_workshop_app.html')
with open(p_meet, 'r', encoding='utf-8') as f:
    h_meet = f.read()

perfect_meet_module1_html = '''      <!-- MODULE 1 -->
      <div class="module-card" id="module-1" style="display:none;">
        <span class="tag">核心功能演練一</span>
        <h2>網路不穩時開啟「透過電話撥號加入 (Join by phone)」語音備援</h2>

        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          您帶學生到偏遠山區進行戶外觀察教學，同一時間校內正在召開全校臨時行政/教學重要會議必須出席。現場行動網路頻寬只有一格，視訊會議畫面完全轉圈卡死，但手機通話訊號仍然正常。此時該如何維持會議參與？
        </div>

        <!-- 📞 Meet 電話收發音訊實務介面與美加地區限制解析卡片 -->
        <div style="background:#ffffff; border:2px solid #ea4335; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(234,67,53,0.1);">
          <h3 style="color:#c5221f; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            📞 實務介面圖解：Meet「使用電話收發音訊」與地區支援全解析
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            當視訊會議進行中遇到網路斷線或頻寬極度不足時，Meet 提供了<strong>「電話音訊備援 (Audio Fallback)」</strong>機制：畫面由電腦顯示或僅聽語音，聲音改走傳統行動電話網路，只要手機有通話訊號就能穩定聽與說。
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#c5221f; margin-bottom:8px;">📷 1. 點擊底部三點選單 ➔「使用電話收發音訊」：</p>
              <img src="images/meet_use_phone_audio_menu.png" alt="Google Meet 更多選項中的使用電話收發音訊" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#c5221f; margin-bottom:8px;">📷 2.「打電話給我」彈出視窗（美加地區限定）：</p>
              <img src="images/meet_call_me_dialog_countries.png" alt="Google Meet 打電話給我國家地區選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
          </div>

          <div style="background:#fef7e0; border-left:4px solid #f9ab00; border-radius:0 8px 8px 0; padding:14px; font-size:0.9rem; line-height:1.7; margin-bottom:14px;">
            <div style="font-weight:700; color:#b06000; margin-bottom:6px;">💡 為什麼選單裡只有「美國 (+1)」與「加拿大 (+1)」？（兩種撥號機制差異）</div>
            <table style="width:100%; border-collapse:collapse; margin-top:8px; font-size:0.88rem; background:white; border-radius:6px; overflow:hidden;">
              <tr style="background:#f1f3f4;">
                <th style="padding:8px 10px; text-align:left; width:28%;">電話備援機制</th>
                <th style="padding:8px 10px; text-align:left; width:36%;">運作方式</th>
                <th style="padding:8px 10px; text-align:left;">地區支援與費用說明</th>
              </tr>
              <tr style="border-top:1px solid #e8eaed;">
                <td style="padding:8px 10px; font-weight:700; color:#c5221f;">📞 打電話給我 (Call me)</td>
                <td style="padding:8px 10px; color:#202124;">輸入手機號碼後，由 Google Meet 伺服器<strong>主動撥電話到您的手機</strong>。</td>
                <td style="padding:8px 10px; color:#5f6368;">目前免費撥出<strong>僅限北美地區（美國 +1、加拿大 +1）</strong>。</td>
              </tr>
              <tr style="border-top:1px solid #e8eaed;">
                <td style="padding:8px 10px; font-weight:700; color:#1a73e8;">📱 自行撥入 (Dial-in)</td>
                <td style="padding:8px 10px; color:#202124;">由會議詳細資訊提供專屬電話號碼與 PIN 碼，由<strong>使用者自行撥打電話</strong>接入。</td>
                <td style="padding:8px 10px; color:#5f6368;">支援各國當地指定接入號碼（通話費依電信業者一般通話費率計）。</td>
              </tr>
            </table>
          </div>

          <div style="background:#e8f0fe; border-left:4px solid #1a73e8; border-radius:0 8px 8px 0; padding:12px 14px; font-size:0.88rem; line-height:1.7;">
            <strong style="color:#1557b0;">🎓 Google 認證 Level 2 考點精髓與教學現場提醒：</strong>
            <ul style="padding-left:20px; color:#202124; margin-top:4px;">
              <li><strong>標準考點</strong>：題目考核的是教師能否在「網路訊號極差、視訊頻寬不足」時，正確選用 <code>使用電話收發音訊 (Use a phone for audio / Join by phone)</code> 來維持通話！</li>
              <li><strong>台灣實測</strong>：在台灣現場研習時，老師們重點在於熟悉<strong>功能路徑（底部三點 ➔ 使用電話收發音訊）</strong>與會議 PIN 碼的電話語音備援觀念。</li>
            </ul>
          </div>
        </div>

        <div style="background:#fef7e0; border:2px solid #f9ab00; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:#b06000; font-size:1.05rem;">🎙️ 本單元練習方式：講師開房間，全體進去實測</strong>
          </div>
          <div style="background:white; border:1px solid #fde293; border-radius:8px; padding:12px 16px; margin-top:8px;">
            <div style="border:1px dashed #f9ab00; border-radius:6px; padding:10px 14px; margin-bottom:10px; font-size:0.9rem; color:#b06000;">🔑 <strong>講師現場公布</strong>：會議連結／課程代碼 ＿＿＿＿＿＿＿＿＿＿</div>
            <div style="font-size:0.95rem; color:#b06000; font-weight:700; line-height:1.6;">🎯 你要做的事：<span style="color:#202124; font-weight:500;">進入研習會議室，點選底部三點選單找到「使用電話收發音訊」，認識撥號號碼與 PIN 碼切換電話語音線路之操作。</span></div>
          </div>
          <div style="margin-top:10px; font-size:0.82rem; color:#5f6368;">📎 <a href="https://docs.google.com/document/d/1W99umvavUbQiq0ccu3nkc-DKRP-CaJX0abhMQVUUAE8/preview" target="_blank" rel="noopener" style="color:#5f6368;">情境補充說明文件（唯讀，Task 20）</a></div>
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          <div class="step-item">
            <input type="checkbox" id="m1-s1">
            <label for="m1-s1">用講師公布的會議連結進入 Meet 會議。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m1-s2">
            <label for="m1-s2">點選右下角 <strong>「更多選項（三點圖示）」</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m1-s3">
            <label for="m1-s3">點選 <strong>「使用電話收發音訊 (Use a phone for audio)」</strong>。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m1-s4">
            <label for="m1-s4">查看<strong>「打電話給我 (Call me)」</strong>（支援美加地區）或<strong>「撥入 (Dial in)」</strong>會議 PIN 碼。</label>
          </div>
          <div class="step-item">
            <input type="checkbox" id="m1-s5">
            <label for="m1-s5">掌握備援觀念：當音訊切換為電話線路後，電腦端會自動靜音，改由電話網路進行通話。</label>
          </div>
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-1')">📋 複製本單元操作步驟</button>
        </div>
      </div>'''

# Find module 1 bounds in meet_workshop_app.html
start_m1 = h_meet.find('<!-- MODULE 1 -->')
end_m1 = h_meet.find('<!-- MODULE 2 -->')
if start_m1 != -1 and end_m1 != -1:
    h_meet = h_meet[:start_m1] + perfect_meet_module1_html + '\n\n      ' + h_meet[end_m1:]
    with open(p_meet, 'w', encoding='utf-8') as f:
        f.write(h_meet)
    print("Reordered and perfected Meet Module 1 in meet_workshop_app.html!")

# Update hands_on_tasks_app.html Task 20
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

# Update Markdown manual Task 20
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_task20_rich = '''#### 演練 20
> 🔗 **雲端真實線上 Docs 實作檔案網址**：[https://docs.google.com/document/d/1W99umvavUbQiq0ccu3nkc-DKRP-CaJX0abhMQVUUAE8/preview](https://docs.google.com/document/d/1W99umvavUbQiq0ccu3nkc-DKRP-CaJX0abhMQVUUAE8/preview)
：戶外教學偏遠地區網路不穩之電話語音備援 (Meet 電話收發音訊)

- **🎯 實務教學情境課題**：帶學生到山區進行戶外觀察教學，同一時間校內正在召開臨時教學會議必須出席。現場行動網路頻寬只有一格，視訊完全連不上，但手機通話仍然正常，需切換至電話語音線路備援。
- **🛠️ 指定工具功能**：Google Meet **使用電話收發音訊 (Use a phone for audio / Join by phone)**

##### 📞 Meet 實務介面圖解：使用電話收發音訊與地區支援全解析
![Google Meet 更多選項中的使用電話收發音訊](../images/meet_use_phone_audio_menu.png)
*圖 10：點擊底部三點選單 ➔ 選擇「使用電話收發音訊 (Use a phone for audio)」*

![Google Meet 打電話給我國家地區選單](../images/meet_call_me_dialog_countries.png)
*圖 11：Google Meet 免費「打電話給我」目前僅支援北美地區（美國 +1、加拿大 +1）*

| 電話備援機制 | 運作方式 | 地區支援與費用說明 |
| :--- | :--- | :--- |
| **📞 打電話給我 (Call me)** | 輸入手機號碼後，由 Google Meet 伺服器**主動撥電話到手機**。 | 目前免費撥出**僅限北美地區（美國 +1、加拿大 +1）**。 |
| **📱 自行撥入 (Dial-in)** | 由會議詳細資訊提供專屬電話號碼與 PIN 碼，由**使用者自行撥打電話**接入。 | 支援各國當地指定接入號碼（依一般通話費率計費）。 |

- **🎓 Google 認證 Level 2 考點精髓**：題目重點考核教師能否在「網路訊號極差、視訊卡頓」時，正確選用 `使用電話收發音訊 (Use a phone for audio / Join by phone)` 改走電話線路維持會議進行！
- **▶️ 手把手實操步驟**：
  1. 進入 Google Meet 視訊會議。
  2. 點選底部控制列右下角「更多選項（三點圖示 $\\vdots$）」。
  3. 點選「使用電話收發音訊 (Use a phone for audio)」。
  4. 認識「打電話給我 (Call me)」與「自行撥入 (Dial in)」之運作機制。
- **✨ 成果驗證點**：成功開啟電話語音備援視窗，確認電腦端自動靜音改由電話音訊進出。
'''

if '#### 演練 20' in h_md:
    idx_t20 = h_md.find('#### 演練 20')
    idx_t21 = h_md.find('#### 演練 21')
    if idx_t20 != -1 and idx_t21 != -1:
        h_md = h_md[:idx_t20] + md_task20_rich + '\n---\n\n' + h_md[idx_t21:]
        with open(p_md, 'w', encoding='utf-8') as f:
            f.write(h_md)
        print("Updated Task 20 in markdown manual!")

print("All Meet documentation updated! Ready to deploy.")
