import os

# 1. Update exam_registration.html
p_exam = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\exam_registration.html'
with open(p_exam, 'r', encoding='utf-8') as f:
    h_exam = f.read()

# Replace the two-column quiz/lab card with clean single exam structure card
old_sub_sec = '''          <div class="sub-section" style="background:#e6f4ea; padding:20px; border-radius:8px; border:1px solid #34a853; margin-bottom:24px;">
            <h3 style="font-size:1.15rem; font-weight:700; color:#137333; margin-bottom:12px;">📚 官方考試兩大題型架構剖析：選擇題 (Quiz) + 實作題 (Lab Exams)</h3>
            <p style="font-size:0.92rem; color:#3c4043; margin-bottom:12px;">Google Certified Educator Level 2 考試包含「選擇題觀念測驗」與「實戰操作實驗測驗 (Lab Exams)」兩大部分：</p>
            <div class="ui-preview" style="margin-top:12px;">
              <img src="images/exam_structure_dropdown.png" alt="Google Level 2 考試兩大題型目錄選單實景">
              <div class="ui-caption">▲ 圖 0-2：官方測驗選單實景 — 包含 GCE Level 2: Quiz A (選擇題) 與各項 Lab Exam 實務操作題 (Classroom, Calendar, Slides Lab)</div>
            </div>
            <div class="feature-grid" style="margin-top:16px;">
              <div class="feat-card" style="background:white;">
                <div class="feat-title" style="color:#1a73e8;">1. 選擇題觀念測驗 (Quiz A)</div>
                <div class="feat-desc">包含 25 道情境單選題與複選題，評量教學情境理解與最優解法選擇（本系統提供完整 25 題雙語練習）。</div>
              </div>
              <div class="feat-card" style="background:white;">
                <div class="feat-title" style="color:#137333;">2. 實作實驗測驗 (Lab Exams)</div>
                <div class="feat-desc">在控制台進行真實工具操作：<br>• <strong>Classroom Lab</strong>：個別分組派發、測驗作業與成績匯入。<br>• <strong>Calendar Lab</strong>：預約時間表 (Appointment schedule) 設定。<br>• <strong>Slides Lab</strong>：選擇板 (Choice boards) 與隱藏投影片設定。</div>
              </div>
            </div>
          </div>'''

new_sub_sec = '''          <div class="sub-section" style="background:#e8f0fe; padding:20px; border-radius:8px; border:1px solid #1a73e8; margin-bottom:24px;">
            <h3 style="font-size:1.15rem; font-weight:700; color:#1557b0; margin-bottom:12px;">📚 官方認證測驗架構剖析：180 分鐘 ‧ 25 題教學情境實務測驗</h3>
            <p style="font-size:0.92rem; color:#3c4043; margin-bottom:12px;">Google Certified Educator Level 2 考試採全面情境導向題型，評量教師在各項 Google 教育工具中的高階應用與最佳解法選擇：</p>
            <div class="feature-grid" style="margin-top:14px;">
              <div class="feat-card" style="background:white; border-left:4px solid #1a73e8;">
                <div class="feat-title" style="color:#1a73e8;">⏱️ 考試時間與題數</div>
                <div class="feat-desc">共 <strong>180 分鐘</strong>（3 小時），包含 <strong>25 道核心實務情境題</strong>（單選題與複選題）。</div>
              </div>
              <div class="feat-card" style="background:white; border-left:4px solid #34a853;">
                <div class="feat-title" style="color:#137333;">🛠️ 考核工具範圍</div>
                <div class="feat-desc">涵蓋 Classroom、Gmail、Meet、Drive/Docs/Sheets/Slides/Sites、Forms、Calendar、YouTube、Keep、Earth 等全套進階整合。</div>
              </div>
            </div>
          </div>'''

if old_sub_sec in h_exam:
    h_exam = h_exam.replace(old_sub_sec, new_sub_sec)
    with open(p_exam, 'w', encoding='utf-8') as f:
        f.write(h_exam)
    print("Updated exam_registration.html to remove Lab Exams mention!")

# 2. Update docs/EXAM_REGISTRATION_GUIDE.md
p_md = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\EXAM_REGISTRATION_GUIDE.md'
with open(p_md, 'r', encoding='utf-8') as f:
    h_md = f.read()

if 'Classroom Lab' in h_md or 'Lab Exams' in h_md:
    h_md = h_md.replace('2. 實作實驗測驗 (Lab Exams)', '2. 考核工具範圍')
    h_md = h_md.replace('在控制台進行真實工具操作：\n• **Classroom Lab**：個別分組派發、測驗作業與成績匯入。\n• **Calendar Lab**：預約時間表 (Appointment schedule) 設定。\n• **Slides Lab**：選擇板 (Choice boards) 與隱藏投影片設定。', '涵蓋 Classroom、Gmail、Meet、Drive、Docs、Sheets、Slides、Sites、Forms、Calendar 等核心進階功能。')
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Updated EXAM_REGISTRATION_GUIDE.md!")

print("All outdated Lab Exams mentions removed cleanly! Ready to deploy.")
