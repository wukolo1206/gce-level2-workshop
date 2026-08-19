import shutil, os

src_menu = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787117122861.png'
src_dialog = r'C:\Users\wu\.gemini\antigravity\brain\29c3fdaf-69e0-4303-b0be-7d6e86b5cbb8\.user_uploaded\media_1787117137986.png'

dest_dir = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\images'
os.makedirs(dest_dir, exist_ok=True)

dst_menu = os.path.join(dest_dir, 'meet_use_phone_audio_menu.png')
dst_dialog = os.path.join(dest_dir, 'meet_call_me_dialog_countries.png')

shutil.copy2(src_menu, dst_menu)
shutil.copy2(src_dialog, dst_dialog)
print("Copied Meet phone audio screenshots!")

meet_phone_guide_html = '''
        <!-- 📞 Meet 電話收發音訊實務介面與美加地區限制解析卡片 -->
        <div style="background:#ffffff; border:2px solid #ea4335; border-radius:12px; padding:22px; margin:20px 0; box-shadow:0 4px 16px rgba(234,67,53,0.1);">
          <h3 style="color:#c5221f; margin-top:0; font-size:1.2rem; display:flex; align-items:center; gap:8px;">
            📞 實務介面圖解：Meet「使用電話收發音訊」與國家支援說明
          </h3>
          <p style="font-size:0.93rem; color:#3c4043; line-height:1.7; margin-bottom:14px;">
            當視訊會議進行中遇到網路斷線或頻寬極度不足時，Meet 提供了<strong>「電話音訊備援」</strong>機制：
          </p>

          <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:16px;">
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#c5221f; margin-bottom:8px;">📷 1. 點擊底部三點 ➔「使用電話收發音訊」：</p>
              <img src="images/meet_use_phone_audio_menu.png" alt="Google Meet 更多選項中的使用電話收發音訊" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
            <div style="background:#f8f9fa; border:1px solid #dadce0; border-radius:8px; padding:12px; text-align:center;">
              <p style="font-weight:700; font-size:0.85rem; color:#c5221f; margin-bottom:8px;">📷 2.「打電話給我」彈出視窗（美加地區）：</p>
              <img src="images/meet_call_me_dialog_countries.png" alt="Google Meet 打電話給我國家地區選單" style="max-width:100%; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.1);">
            </div>
          </div>

          <div style="background:#fef7e0; border-left:4px solid #f9ab00; border-radius:0 8px 8px 0; padding:14px; font-size:0.9rem; line-height:1.7;">
            <div style="font-weight:700; color:#b06000; margin-bottom:6px;">💡 為什麼選單裡只有「美國 (+1)」與「加拿大 (+1)」？</div>
            <ul style="padding-left:20px; color:#3c4043;">
              <li><strong>【打電話給我 (Call me)】</strong>：是由 Google 伺服器主動打給您的手機，目前免費撥出服務<strong>僅支援北美地區（美國與加拿大 +1）</strong>。</li>
              <li><strong>【自行撥入 (Dial-in)】</strong>：若是提供電話號碼與會議 PIN 碼由使用者主動撥入，則可支援全球指定撥入號碼接入會議。</li>
              <li><strong>🎯 Google 認證 Level 2 考點精髓</strong>：考題重點在於考核教師能否在<strong>「網路訊號極差、視訊卡頓」時，正確選用「電話音訊備援 (Use a phone for audio / Join by phone)」</strong>來維持通話！</li>
            </ul>
          </div>
        </div>
'''

# 1. Update meet_workshop_app.html
p_meet = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'meet_workshop_app.html')
with open(p_meet, 'r', encoding='utf-8') as f:
    h_meet = f.read()

target_meet_m1 = '<h2>網路不穩時開啟「透過電話撥號加入 (Join by phone)」語音備援</h2>'
if target_meet_m1 in h_meet and 'meet_use_phone_audio_menu.png' not in h_meet:
    h_meet = h_meet.replace(target_meet_m1, target_meet_m1 + '\n' + meet_phone_guide_html)
    with open(p_meet, 'w', encoding='utf-8') as f:
        f.write(h_meet)
    print("Embedded meet phone guide in meet_workshop_app.html!")

# 2. Update hands_on_tasks_app.html
p_tasks = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'hands_on_tasks_app.html')
with open(p_tasks, 'r', encoding='utf-8') as f:
    h_tasks = f.read()

target_task20 = '<h2 class="task-title">戶外教學偏遠地區網路不穩之電話語音備援</h2>'
if target_task20 in h_tasks and 'meet_use_phone_audio_menu.png' not in h_tasks:
    h_tasks = h_tasks.replace(target_task20, target_task20 + '\n' + meet_phone_guide_html)
    with open(p_tasks, 'w', encoding='utf-8') as f:
        f.write(h_tasks)
    print("Embedded meet phone guide in hands_on_tasks_app.html!")

# 3. Update Markdown manual Task 20
p_md = os.path.join(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包', 'docs', 'GCE_Level_2_25個全實作原創教學情境演練手冊.md')
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

md_meet_guide = '''
##### 📞 Meet 實務介面圖解：使用電話收發音訊與地區支援
![Google Meet 更多選項中的使用電話收發音訊](../images/meet_use_phone_audio_menu.png)
*圖 10：點擊底部三點圖示 ➔ 選擇「使用電話收發音訊 (Use a phone for audio)」*

![Google Meet 打電話給我國家地區選單](../images/meet_call_me_dialog_countries.png)
*圖 11：Google Meet 免費「打電話給我」目前僅支援北美地區（美國 +1、加拿大 +1）*

> 💡 **考點與實務解析**：
> - **打電話給我 (Call me)**：Google 伺服器主動撥出，目前僅支援美加地區（+1）。
> - **自行撥入 (Dial-in)**：提供會議號碼與 PIN 碼由使用者手機撥入。
> - **Level 2 核心判斷**：當偏鄉山區或現場網路頻寬不足時，**改走電話語音線路 (Join by phone / Phone audio fallback)** 為標準解法！
'''

if 'meet_use_phone_audio_menu.png' not in h_md and '#### 演練 20' in h_md:
    h_md = h_md.replace('#### 演練 20', '#### 演練 20\n' + md_meet_guide)
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Embedded meet phone guide in markdown manual!")

print("All Meet updates ready for deployment!")
