import re

path_html = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包\study_guide_app.html'
with open(path_html, 'r', encoding='utf-8') as f:
    app_html = f.read()

# 1. Add top tab button and sidebar button for Bilingual Alignment
bilingual_alignment_box = '''
        <!-- Bilingual Alignment Card -->
        <div style="background:#e8f0fe; border:1.5px solid #aecbfa; border-radius:12px; padding:20px; margin-bottom:28px;">
          <h3 style="color:#1a73e8; font-size:1.15rem; font-weight:700; margin-bottom:12px; display:flex; align-items:center; gap:8px;">
            🌐 Google 官方中英文架構與關鍵考點術語意同對照 (Bilingual Alignment)
          </h3>
          <p style="font-size:0.92rem; color:#3c4043; line-height:1.6; margin-bottom:16px;">
            正式認證考試為英文/中英雙語題型，而 Google Teacher Center 提供繁體中文培訓頁面。以下為研習必考之<strong>核心專業術語與情境意同對照矩陣</strong>：
          </p>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; background:white; font-size:0.88rem; border-radius:8px; overflow:hidden;">
              <thead>
                <tr style="background:#1a73e8; color:white; text-align:left;">
                  <th style="padding:10px 12px;">英文認證考綱術語 (English Exam Term)</th>
                  <th style="padding:10px 12px;">官方繁體中文術語 (zh-TW Official Term)</th>
                  <th style="padding:10px 12px;">對應講義與 11 單元意同對照</th>
                  <th style="padding:10px 12px;">解題與應試關鍵 (Key Exam Focus)</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid #e0e0e0;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Appointment schedule</td>
                  <td style="padding:10px 12px; font-weight:700;">預約時間表</td>
                  <td style="padding:10px 12px;">Unit 2 / 第 4 單元</td>
                  <td style="padding:10px 12px; color:#137333;">親師面談自動呈現空閒時段與網址</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0; background:#f8f9fa;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Grant access to account</td>
                  <td style="padding:10px 12px; font-weight:700;">授予您帳戶的存取權 (代理)</td>
                  <td style="padding:10px 12px;">Unit 1 / 第 3 單元</td>
                  <td style="padding:10px 12px; color:#137333;">團隊成員免密碼代表主管收發 Email</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Paragraph styles (Headings)</td>
                  <td style="padding:10px 12px; font-weight:700;">段落樣式 (標題1、標題2)</td>
                  <td style="padding:10px 12px;">Unit 3 / 第 6 單元</td>
                  <td style="padding:10px 12px; color:#137333;">Docs 自動生成 Table of Contents 目錄</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0; background:#f8f9fa;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Originality reports</td>
                  <td style="padding:10px 12px; font-weight:700;">原創性比對報告</td>
                  <td style="padding:10px 12px;">Unit 3 / 第 9 單元</td>
                  <td style="padding:10px 12px; color:#137333;">Classroom 學生繳交前自主檢查抄襲</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Conditional Formatting</td>
                  <td style="padding:10px 12px; font-weight:700;">條件式格式設定</td>
                  <td style="padding:10px 12px;">Unit 6 / 第 5 單元</td>
                  <td style="padding:10px 12px; color:#137333;">Sheets 根據分數表現自動變更格子顏色</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0; background:#f8f9fa;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Quiz Assignment & Grade importing</td>
                  <td style="padding:10px 12px; font-weight:700;">測驗作業 與 成績匯入</td>
                  <td style="padding:10px 12px;">Unit 3 / 第 11 單元</td>
                  <td style="padding:10px 12px; color:#137333;">Forms 測驗分數自動同步進入成績冊</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Smart Chips (@People / @Date)</td>
                  <td style="padding:10px 12px; font-weight:700;">智慧晶片 (@人員 / @日期)</td>
                  <td style="padding:10px 12px;">Unit 1 / 第 1 單元</td>
                  <td style="padding:10px 12px; color:#137333;">Docs 議程指派任務與設定截止日</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0; background:#f8f9fa;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Join by phone</td>
                  <td style="padding:10px 12px; font-weight:700;">透過電話撥號加入</td>
                  <td style="padding:10px 12px;">Unit 4 / 第 8 單元</td>
                  <td style="padding:10px 12px; color:#137333;">Meet 網路不穩定時之備援通話</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Marketplace Add-ons</td>
                  <td style="padding:10px 12px; font-weight:700;">Workspace Marketplace 外掛程式</td>
                  <td style="padding:10px 12px;">Unit 5 / 第 3 單元</td>
                  <td style="padding:10px 12px; color:#137333;">在 Docs 給予非同步語音回饋 (Mote)</td>
                </tr>
                <tr style="border-bottom:1px solid #e0e0e0; background:#f8f9fa;">
                  <td style="padding:10px 12px; font-weight:700; color:#1a73e8;">Hyperlink Slides to each other</td>
                  <td style="padding:10px 12px; font-weight:700;">投影片互相建立超連結</td>
                  <td style="padding:10px 12px;">Unit 4 / 第 7 單元</td>
                  <td style="padding:10px 12px; color:#137333;">Slides 製作單字記憶卡與選擇板</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
'''

if '🌐 Google 官方中英文架構與關鍵考點術語意同對照' not in app_html:
    app_html = app_html.replace('<div id="full-handout-view">', '<div id="full-handout-view">\n' + bilingual_alignment_box)

with open(path_html, 'w', encoding='utf-8') as f:
    f.write(app_html)

print("Successfully integrated Bilingual Alignment into study_guide_app.html!")
