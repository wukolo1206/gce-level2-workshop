# -*- coding: utf-8 -*-
"""
各工具篇的功能術語中英對照表。

為什麼需要：Level 2 的考題與 Lab 實作是英文出題，介面也可切換語言；
Lab 的自動評分（Check my progress）更是<逐字比對英文字串>。
學員只記中文名稱，考場上會對不起來。

格式：(中文名稱, English, 備註)
備註標記：★ = 核心功能；⚙ = 名稱須完全一致（系統逐字比對）；⚠️ = 容易混淆
"""

GLOSSARY = {
    'docs_workshop_app.html': [
        ('智慧型畫布', 'Smart Canvas', '★ 輸入 @ 觸發的整套功能總稱'),
        ('使用者智慧型方塊', 'People smart chip', '★ 輸入 @ 後直接打姓名或 Email'),
        ('段落樣式', 'Paragraph styles', '★ 標題 1 = Heading 1，自動目錄靠它'),
        ('目錄', 'Table of contents', '插入 ➔ 目錄'),
        ('尋找與取代', 'Find and replace', '★ Ctrl + H'),
        ('全部取代', 'Replace all', ''),
        ('翻譯文件', 'Translate document', '★ 工具 ➔ 翻譯文件，會另存新檔'),
        ('擴充功能／外掛程式', 'Extensions / Add-ons', '★ 來源是 Workspace Marketplace'),
        ('指派給…', 'Assign to…', '⚙ 註解中 +Email 後必須勾選此項才算任務'),
        ('書籤', 'Bookmark', '文件內部跳轉用'),
    ],
    'slides_workshop_app.html': [
        ('超連結投影片', 'Hyperlink slides', '★ 做互動記憶卡的關鍵功能'),
        ('簡報中的投影片', 'Slides in this presentation', '連結對話框中的選項名稱'),
        ('連結', 'Link', '★ 插入選單與右鍵兩條路徑效果相同'),
        ('主題製作工具', 'Theme builder', '★ 查看 ➔ 主題製作工具，即母版編輯區'),
        ('版面配置', 'Layout', ''),
        ('圖片預留位置', 'Image placeholder', '⚙ 命名須完全一致，系統逐字比對'),
        ('內嵌影片', 'Insert video', '⚙ 自製影片走「Google 雲端硬碟」分頁，非 YouTube'),
        ('格式選項 ➔ 影片播放', 'Format options ➔ Video playback', '設定起訖秒數'),
        ('註解者', 'Commenter', '⚙ 送審一律用這一層，原稿才不會被改'),
        ('檢視者／編輯者', 'Viewer / Editor', ''),
    ],
    'sheets_workshop_app.html': [
        ('條件式格式設定', 'Conditional formatting', '★ 讓分數自動變色'),
        ('小於／大於', 'Less than / Greater than', '格式規則的條件名稱'),
        ('資料欄統計資料', 'Column stats', '★ 選一欄就看到分佈與次數'),
        ('樞紐分析表', 'Pivot table', '★ 可交叉統計的正式表格'),
        ('列／欄／值', 'Rows / Columns / Values', '樞紐分析編輯器的欄位'),
        ('篩選器檢視畫面', 'Filter views', '只影響自己，不動到別人畫面'),
        ('資料驗證', 'Data validation', '下拉選單與格式限制'),
        ('資料清理', 'Data cleanup', '⚠️ 清理重複與空白用，不是統計工具'),
    ],
    'classroom_workshop_app.html': [
        ('協同教師', 'Co-teacher', '★ 權限幾乎等同主教師，但不能刪課'),
        ('成員', 'People', '分頁名稱'),
        ('主題', 'Topic', '⚙ 課程的目錄章節，可拖曳排序'),
        ('課堂作業', 'Classwork', '分頁名稱'),
        ('訊息串', 'Stream', '公告發布的位置'),
        ('公告', 'Announcement', '⚙ 發在訊息串，不進成績冊'),
        ('測驗作業', 'Quiz assignment', '★ 會自動附帶一份 Blank Quiz 表單'),
        ('成績匯入', 'Grade importing', '★ 分數帶回成績冊的關鍵開關'),
        ('原創性比對報告', 'Originality reports', '★ 學生提交前最多可自行跑 3 次'),
        ('為每位學生建立副本', 'Make a copy for each student', '附件權限，最多人設錯'),
    ],
    'calendar_workshop_app.html': [
        ('預約時間表', 'Appointment schedule', '★ 讓對方自助預約且不撞期'),
        ('重複／自訂重複', 'Repeat / Custom recurrence', '★ 一次建立整學期／整年系列'),
        ('串流直播', 'Live stream', '⚙ 需 Education Plus；觀眾只看不互動'),
        ('邀請對象權限', 'Guest permissions', '⚙ 最易出包處，關係到個資保護'),
        ('邀請其他使用者', 'Invite others', '⚙ 必須取消勾選'),
        ('查看邀請對象名單', 'See guest list', '⚙ 必須取消勾選'),
        ('建立會議記錄', 'Create meeting notes', '★ 說明欄工具列最左邊的文件圖示'),
        ('通知（電子郵件）', 'Notification (Email)', '⚙ 可選「通知」或「電子郵件」兩種'),
    ],
    'meet_workshop_app.html': [
        ('使用電話收發音訊', 'Use a phone for audio', '★ 網路不穩時的語音備援'),
        ('撥入', 'Dial in', '需與主辦者同網域，管理員亦須啟用'),
        ('主持人控制項', 'Host controls', '盾牌圖示'),
        ('分組討論室', 'Breakout rooms', '在「活動 Activities」裡，需主持人身分'),
        ('抗噪功能', 'Noise cancellation', '⚠️ 只濾背景雜音，解決不了斷線'),
        ('按鍵通話', 'Push to talk', '⚠️ 同樣是誘答選項'),
    ],
    'forms_workshop_app.html': [
        ('新增區段', 'Add section', '分流的前提'),
        ('根據答案前往相關區段', 'Go to section based on answer', '★ 差異化分流的關鍵設定'),
        ('設為測驗', 'Make this a quiz', '設定 ➔ 測驗'),
        ('答案', 'Answer key', '設定正解與配分'),
        ('新增作答意見回饋', 'Answer feedback', '答錯時顯示解說與複習連結'),
        ('回應驗證', 'Response validation', '限制填答格式'),
        ('必填', 'Required', ''),
        ('回覆 (分頁)', 'Responses', '繁中介面是「回覆」不是「回應」'),
    ],
    'sites_workshop_app.html': [
        ('子頁面', 'Subpage', '★ 導覽列自動變成下拉選單'),
        ('頁面面板', 'Pages panel', '右側面板'),
        ('發布', 'Publish', '★ 發布後才有對外網址'),
        ('公開', 'Public / Anyone with the link', '★ 網站本身要設這個'),
        ('發布到網路', 'Publish to the web', '★ 內嵌的文件要另外設這個'),
        ('插入面板', 'Insert panel', '嵌入 Drive 檔案與 YouTube'),
    ],
    'gmail_workshop_app.html': [
        ('授予您帳戶的存取權', 'Grant access to your account', '★ 代理不必給密碼，責任歸屬清楚'),
        ('帳戶與匯入', 'Accounts and Import', '設定分頁名稱'),
        ('篩選器', 'Filter', '規則引擎'),
        ('標籤', 'Label', 'Gmail 沒有資料夾，只有標籤'),
        ('略過收件匣', 'Skip the Inbox', '篩選器動作之一'),
        ('範本', 'Templates', '舊稱罐頭回應；須先在「進階」啟用'),
        ('排程傳送', 'Schedule send', '傳送鈕旁的下拉箭頭'),
        ('搜尋運算子', 'Search operators', 'has:attachment、from:、before:'),
    ],
    'practicesets_workshop_app.html': [
        ('練習題', 'Practice sets', '★ 需 Education Plus / T&L'),
        ('額外協助', 'Extra help', '★ 每題最多可掛 10 個資源'),
        ('允許老師透過連結存取', 'Allow teachers to access via link', '★ 對方拿到的是可複製的副本'),
        ('技能', 'Skills', '⚠️ 與額外協助不同，別搞混'),
        ('匯入', 'Import', '⚠️ 同樣是誘答選項'),
        ('課程深入分析', 'Class insights', '教師端查看全班與個別學生的困難題目'),
    ],
}
