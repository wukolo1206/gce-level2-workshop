import os

# 1. Update exam_registration.html
p_exam = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\exam_registration.html'
with open(p_exam, 'r', encoding='utf-8') as f:
    h_exam = f.read()

# Subtitle
h_exam = h_exam.replace('<p>報名步驟 ‧ 認證控制台導覽 ‧ 兩大題型說明</p>', '<p>報名步驟 ‧ 認證控制台導覽 ‧ 測驗架構說明</p>')

# STEP 3
old_step3 = '''          <div class="step-box">
            <div class="step-num">STEP 3</div>
            <div class="step-title">使用兌換碼 (Voucher) 或線上刷卡 ($25 美金)</div>
            <p>若研習有發放免費兌換碼，在 Promotion Code 欄位輸入並點選 Apply。若無兌換碼，請輸入信用卡資訊支付 $25 美金報名費。</p>
          </div>'''

new_step3 = '''          <div class="step-box">
            <div class="step-num">STEP 3</div>
            <div class="step-title">免費報名與確認開通（官方全面免費 $0）</div>
            <p>目前 Google 官方認證平台已開放<strong>免費報名（$0 免付費）</strong>！點選「報名 / Register」後即可直接確認開通測驗，無需輸入信用卡刷卡或購買兌換碼。</p>
          </div>'''

h_exam = h_exam.replace(old_step3, new_step3)
h_exam = h_exam.replace('再次付費補考', '再次報名補考')

with open(p_exam, 'w', encoding='utf-8') as f:
    f.write(h_exam)
print("Updated exam_registration.html for Free Exam policy!")

# 2. Update docs/EXAM_REGISTRATION_GUIDE.md
p_md = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\docs\EXAM_REGISTRATION_GUIDE.md'
if os.path.exists(p_md):
    with open(p_md, 'r', encoding='utf-8') as f:
        h_md = f.read()
    h_md = h_md.replace('使用兌換碼 (Voucher) 或線上刷卡 ($25 美金)', '免費報名與確認開通（官方全面免費 $0）')
    h_md = h_md.replace('若研習有發放免費兌換碼，在 Promotion Code 欄位輸入並點選 Apply。若無兌換碼，請輸入信用卡資訊支付 $25 美金報名費。', '目前 Google 官方已開放免費報名，點選「報名」後即可直接開通測驗，無需輸入信用卡或兌換碼。')
    h_md = h_md.replace('再次付費補考', '再次報名補考')
    with open(p_md, 'w', encoding='utf-8') as f:
        f.write(h_md)
    print("Updated EXAM_REGISTRATION_GUIDE.md!")

# 3. Check all other md and html files
for root, dirs, files in os.walk(r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'):
    if '.git' in root or '.gh_deploy_temp' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.md')):
            p = os.path.join(root, file)
            with open(p, 'r', encoding='utf-8', errors='ignore') as f:
                c = f.read()
            if '$25' in c or '25 美金' in c or '兩大題型說明' in c:
                c = c.replace('兩大題型說明', '測驗架構說明')
                c = c.replace('$25 美金', '免費 $0')
                c = c.replace('$25', '免費')
                with open(p, 'w', encoding='utf-8') as f:
                    f.write(c)
                print(f"Cleaned {file}!")

print("All files updated for Free Exam Policy! Ready to deploy.")
