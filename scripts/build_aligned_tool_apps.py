# -*- coding: utf-8 -*-
"""
將 Slides / Sheets / Classroom / Calendar / Meet / Forms / Sites / Practice Sets
八個工具篇研習 App，全部升級為與 docs_workshop_app.html 相同的版型與資訊密度：

  演練標籤 ➔ 標題 ➔ 功能簡介 ➔ 【實務教學情境】黃框 ➔ 真實 Workspace 檔案綠框（含具體修改任務）
  ➔ 實作步驟勾選清單 ➔ 一鍵複製步驟

情境與步驟文字來源：docs/GCE_Level_2_25個全實作原創教學情境演練手冊.md
真實檔案連結來源：all_25_real_workspace_links.json
"""
import os
import json

ROOT = r'd:\備課ai\研習講義\Google認證_Level2_研習講義與備考工具包'

with open(os.path.join(ROOT, 'all_25_real_workspace_links.json'), 'r', encoding='utf-8') as f:
    LINKS = json.load(f)

TYPE_LABEL = {'Docs': 'Google Docs', 'Slides': 'Google Slides', 'Sheets': 'Google Sheets'}
TYPE_ICON = {'Docs': '📄', 'Slides': '🎨', 'Sheets': '📊'}


# ---------------------------------------------------------------- 各工具篇內容
APPS = [
    {
        'file': 'slides_workshop_app.html',
        'emoji': '🎨',
        'name': 'Google Slides',
        'title': 'Google Slides 互動簡報與協作審閱研習講義',
        'subtitle': '互動教材設計 ‧ 全校統一母版 ‧ 批註任務指派',
        'overview_lead': '歡迎來到 <strong>Google Slides（Google 簡報）</strong>工具篇講義！本單元不談美編技巧，'
                         '而是聚焦在如何把簡報從「單向播放的投影片」，變成<strong>學生可以點、老師可以派任務</strong>的互動教材與團隊協作平台。',
        'goals': [
            '<strong>演練一</strong>：用投影片超連結（Hyperlink Slides）做出可自我檢測的互動單字記憶卡。',
            '<strong>演練二</strong>：用主題建構工具（Theme Builder）建立全校統一母版與圖片預留位置。',
            '<strong>演練三</strong>：內嵌 YouTube 教學影片，並用批註 <code>+Email</code> 指派同仁審閱。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '🔗 演練一：投影片超連結互動記憶卡',
                'title': '物件與文字超連結 (Hyperlink Slides) 製作互動單字記憶卡',
                'intro': '在 Google Slides 中，任何一個文字方塊或圖形都能被設為「連結到本簡報中的某一張投影片」。'
                         '這是把線性簡報改造成<strong>非線性互動教材</strong>最省力的方法，完全不需要任何外掛。',
                'scenario': '您正在為班上準備英檢單字複習教材。您希望學生在自習時，先看到單字題面自己回想意思，'
                            '想好之後再點選畫面上的「看解答」按鈕，直接跳到該單字的解答頁；看完解答還能點「回題目區」返回目錄，反覆自我檢測。',
                'task_key': 'Task 13',
                'doc_inst': '請選取投影片上的單字按鈕，按右鍵點選「連結」，改連結到「簡報中的投影片」對應的解答頁，並在解答頁加上一個連回目錄頁的返回按鈕！',
                'steps': [
                    '開啟簡報，選取題目頁上的單字按鈕（文字方塊或圖形）。',
                    '按滑鼠右鍵選取 <strong>「連結 (Link)」</strong>（或按快捷鍵 <code>Ctrl + K</code>）。',
                    '在彈出視窗選擇 <strong>「簡報中的投影片 (Slides in this presentation)」</strong>，點選目標解答頁碼。',
                    '在解答頁另外插入一個「返回」圖形，同樣設定連結回到題目目錄頁。',
                    '按 <strong>「投影播放 (Present)」</strong> 實測：點按鈕應直接跳頁，而非往下一張前進。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '🖼️ 演練二：主題建構工具與圖片預留位置',
                'title': '使用主題建構工具 (Theme Builder) 插入圖片預留位置 (Placeholder)',
                'intro': '「主題建構工具」就是 Google Slides 的母版編輯區。在這裡改一次字型、顏色或版面配置，'
                         '整份簡報所有套用該版面的投影片會同步更新；而<strong>圖片預留位置</strong>能讓填寫者一鍵上傳照片就自動對齊，不會歪掉。',
                'scenario': '學校要各處室在期末成果發表會上報告，您被指派製作一份「學校簡報標準母版」發給全校同仁套用。'
                            '為了讓大家交回來的簡報格式一致，您需要在母版中預先設定好統一的標題字級與一個固定尺寸的照片框，讓同仁只要點一下就能把活動照片放進正確位置。',
                'task_key': 'Task 14',
                'doc_inst': '請點選「檢視 ➔ 主題建構工具」進入母版編輯區，在版面配置中插入一個「圖片預留位置」，並調整標題字型與色彩後離開母版！',
                'steps': [
                    '點選選單 <strong>「檢視 ➔ 主題建構工具 (Theme Builder)」</strong>。',
                    '在左側選取要修改的<strong>版面配置 (Layout)</strong>（注意：改最上方那張才會全部套用）。',
                    '點選 <strong>「插入 ➔ 預留位置 ➔ 圖片預留位置 (Image placeholder)」</strong>，拖曳出照片框位置與大小。',
                    '調整標題文字的字型、字級與顏色，設定全校統一規格。',
                    '點右上角 <strong>「X」離開主題建構工具</strong>，回到一般頁面驗證：照片框出現一鍵上傳圖示。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '🎬 演練三：內嵌影片與批註指派審閱',
                'title': '簡報內嵌 YouTube 影片與註解 +Email 指派審閱任務',
                'intro': '簡報可直接內嵌 YouTube 影片並設定<strong>起訖播放秒數</strong>，上課時不必切換分頁；'
                         '而在註解中輸入 <code>+對方Email</code> 並勾選「指派」，該同仁會收到一封含任務的 Email，任務完成前註解會一直標示為未處理。',
                'scenario': '您正在製作「校園植物導覽」簡報，想在介紹頁直接播放一段校園實拍影片。'
                            '簡報完成後要送出去給自然科召集人審閱，您希望不是口頭拜託，而是在簡報中明確標記出「請你確認這一頁的植物名稱」這項待辦，讓對方收到通知也追得到進度。',
                'task_key': 'Task 15',
                'doc_inst': '請點選「插入 ➔ 影片」內嵌一段 YouTube 教學影片，再選取該頁物件新增註解，輸入 +同仁Email 並勾選「指派給…」核取方塊！',
                'steps': [
                    '點選選單 <strong>「插入 ➔ 影片 (Video)」</strong>，以關鍵字搜尋或貼上 YouTube 網址內嵌影片。',
                    '選取影片後開啟右側 <strong>「格式選項 ➔ 影片播放」</strong>，設定起始與結束秒數（只播需要的片段）。',
                    '選取要審閱的物件，點選 <strong>「新增註解 (Add comment)」</strong>。',
                    '在註解框輸入 <strong><code>+同仁Email</code></strong>，並<strong>勾選「指派給… (Assign to…)」</strong>核取方塊。',
                    '點選「指派」，確認對方收到 Email 通知且註解顯示為待辦任務。',
                ],
            },
        ],
    },
    {
        'file': 'sheets_workshop_app.html',
        'emoji': '📊',
        'name': 'Google Sheets',
        'title': 'Google Sheets 成績分析與問卷統計研習講義',
        'subtitle': '不及格自動警示 ‧ 樞紐分析 ‧ 資料視覺化',
        'overview_lead': '歡迎來到 <strong>Google Sheets（Google 試算表）</strong>工具篇講義！'
                         '本單元的目標很單純：讓您<strong>不用會寫函數</strong>，也能把成績單與問卷回應變成看得懂、看得快的分析結果。',
        'goals': [
            '<strong>演練一</strong>：用條件式格式設定，讓不及格分數自動跳紅、不必逐格檢查。',
            '<strong>演練二</strong>：用直行統計與樞紐分析表，數秒統計數百筆問卷回應。',
            '<strong>演練三</strong>：用篩選器檢視與資料驗證，讓多人共用的表格不會被改壞。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '🎨 演練一：條件式格式自動警示',
                'title': '條件式格式設定 (Conditional Formatting) 自動變更儲存格外觀',
                'intro': '條件式格式會依照儲存格「內容是否符合條件」自動套用顏色。設定一次之後，'
                         '<strong>之後輸入的新成績會即時自動變色</strong>，是成績追蹤最實用的自動化功能。',
                'scenario': '期中考成績剛登錄完畢，全班 30 位學生、六個科目的分數擠在一張表上。'
                            '您希望一眼就能看出哪些學生哪一科需要補救教學，而不是自己一格一格用眼睛掃描找出低於 60 分的數字。',
                'task_key': 'Task 18',
                'doc_inst': '請選取整個成績欄位範圍，點選「格式 ➔ 條件式格式設定」，將「小於 60」的儲存格設為紅底白字！',
                'steps': [
                    '選取要套用的成績欄位範圍（可整欄選取，含之後才要輸入的空格）。',
                    '點選選單 <strong>「格式 ➔ 條件式格式設定 (Conditional formatting)」</strong>。',
                    '在「格式規則」下拉選單選取 <strong>「小於 (Less than)」</strong>，數值輸入 <code>60</code>。',
                    '在格式設定樣式中設定<strong>紅色背景 + 白色粗體文字</strong>，點選「完成」。',
                    '驗證：隨手把某一格改成 55，該格應立即自動變紅。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '📈 演練二：直行統計與樞紐分析表',
                'title': '直行統計 (Column stats) 與樞紐分析表 (Pivot table) 快速統計回應',
                'intro': '「直行統計」是最快的一眼分析：選取一欄就直接看到分佈長條圖與各值出現次數；'
                         '「樞紐分析表」則能產出可交叉、可再運算的正式統計表格，兩者都<strong>不需要輸入任何函數</strong>。',
                'scenario': '校慶進場服裝的線上投票剛截止，表單回應累積了數百筆資料。'
                            '學務主任下午開會就要知道哪個顏色最高票、各班票數分佈如何，您需要在幾分鐘內生出可以直接投影的統計結果。',
                'task_key': 'Task 19',
                'doc_inst': '請選取「服裝顏色」欄位後點選「資料 ➔ 直行統計」查看分佈，再點選「插入 ➔ 樞紐分析表」，將顏色拉入列、以 COUNTA 統計票數！',
                'steps': [
                    '選取要分析的欄位（如「服裝顏色」整欄）。',
                    '點選選單 <strong>「資料 ➔ 直行統計 (Column stats)」</strong>，右側面板即顯示分佈圖與出現次數。',
                    '選取整份資料範圍，點選 <strong>「插入 ➔ 樞紐分析表 (Pivot table)」</strong>，選擇建立在新工作表。',
                    '在右側編輯器把「服裝顏色」拉入 <strong>「列 (Rows)」</strong>，再把同欄位拉入 <strong>「值 (Values)」</strong> 並選擇 <code>COUNTA</code>。',
                    '（進階）把「班級」拉入 <strong>「欄 (Columns)」</strong>，即產出班級 × 顏色的交叉統計表。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '🔒 演練三：篩選器檢視與資料驗證',
                'title': '篩選器檢視 (Filter views) 與資料驗證 (Data validation) 保護共用表格',
                'intro': '多位教師同時開一張表時，一般「篩選器」會<strong>連別人的畫面一起改掉</strong>；'
                         '「篩選器檢視」則只影響自己。搭配資料驗證做成下拉選單，可從源頭杜絕輸入格式錯亂。',
                'scenario': '學年共用一張「補救教學名單」試算表，六位老師同時在線上編輯。'
                            '常發生的狀況是：您正在篩選自己班級的資料，別的老師一按篩選，您的畫面就跳掉；而「已完成／完成／OK」等各種寫法混雜，事後根本無法統計。',
                'task_key': 'Task 18',
                'doc_inst': '請在同一份成績表上，點選「資料 ➔ 建立新的篩選器檢視」建立只屬於自己的檢視，並對狀態欄位設定「資料驗證 ➔ 下拉式選單」限定填答選項！',
                'steps': [
                    '點選選單 <strong>「資料 ➔ 篩選器檢視 ➔ 建立新的篩選器檢視」</strong>（畫面外框會變成深灰色）。',
                    '在深灰色模式下設定自己要看的篩選條件，命名後關閉；他人畫面完全不受影響。',
                    '選取「狀態」欄位，點選 <strong>「資料 ➔ 資料驗證 (Data validation)」</strong>。',
                    '規則選擇 <strong>「下拉式選單」</strong>，輸入固定選項（如：未開始／進行中／已完成）。',
                    '勾選<strong>拒絕輸入不符合的資料</strong>，驗證：手動輸入其他文字會被擋下。',
                ],
            },
        ],
    },
    {
        'file': 'classroom_workshop_app.html',
        'emoji': '🏫',
        'name': 'Google Classroom',
        'title': 'Google Classroom 課程經營與評量整合研習講義',
        'subtitle': '協同教師 ‧ 主題分頁 ‧ 成績匯入 ‧ 原創性比對',
        'overview_lead': '歡迎來到 <strong>Google Classroom（Google 課堂）</strong>工具篇講義！'
                         '本單元從「開一門課」一路帶到「評量分數自動回到成績冊」，聚焦在 Level 2 最常考、也是實務上最省時的四個設定。',
        'goals': [
            '<strong>演練一</strong>：邀請協同教師（Co-teacher），與夥伴共同管理同一門課程。',
            '<strong>演練二</strong>：用主題（Topics）整理課堂作業，讓學生找得到本週進度。',
            '<strong>演練三</strong>：建立測驗作業並開啟成績匯入，Forms 分數自動帶回成績冊。',
            '<strong>演練四</strong>：開啟原創性比對報告，讓學生自己檢查是否無意間抄襲。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '👥 演練一：協同教師與課程共管',
                'title': '邀請協同教師 (Co-teachers) 共同管理課程',
                'intro': '協同教師擁有<strong>與主教師幾乎相同的權限</strong>：可發布作業、批改、與家長聯繫；'
                         '唯一不能做的是刪除課程或移除主教師。這是雙語協同、實習輔導、學年共備最正確的作法（而不是共用帳號密碼）。',
                'scenario': '本學期您與一位外籍教師共同授課英語會話課。外師需要能自己發布作業、批改學生錄音作業並登錄成績，'
                            '但您不希望把自己的帳號密碼交給對方，也不想每次都由您代為發布。',
                'task_key': 'Task 10',
                'doc_inst': '請開啟課程的「成員 (People)」頁面，在教師區塊點選「邀請教師」，輸入協同教師 Email 並送出邀請！',
                'steps': [
                    '進入課程，點選上方 <strong>「成員 (People)」</strong> 分頁。',
                    '在「教師」區塊右側點選 <strong>「邀請教師 (Invite teachers)」</strong> 圖示。',
                    '輸入協同教師的 Email，點選「邀請」。',
                    '請對方至信箱點選接受；接受後身分列會顯示為 <strong>Co-teacher</strong>。',
                    '驗證：協同教師可自行建立作業與批改，但無法刪除整門課程。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '📚 演練二：主題分頁與課堂作業建置',
                'title': '建立主題 (Topics) 分頁、一般作業與線上閱讀素材',
                'intro': '課堂作業如果不分主題，一學期後會變成一長串無法閱讀的清單。'
                         '「主題」等於課程的目錄章節，可自由拖曳排序，把當週單元<strong>拉到最上方</strong>學生就不會找錯。',
                'scenario': '開學三週後，您的課程「課堂作業」頁面已經累積了十幾則公告、作業與補充教材，全部混在一起。'
                            '學生常在聯絡簿上寫「找不到老師說的那份閱讀資料」，您需要把它整理成依單元分區的結構。',
                'task_key': 'Task 11',
                'doc_inst': '請在「課堂作業」頁面點選「建立 ➔ 主題」建立單元分頁，再建立一則作業並指定歸入該主題，最後拖曳主題調整順序！',
                'steps': [
                    '進入 <strong>「課堂作業 (Classwork)」</strong> 分頁，點選 <strong>「建立 ➔ 主題 (Topic)」</strong>。',
                    '輸入單元名稱（如「第二單元：閱讀理解」）並建立。',
                    '再次點選「建立 ➔ 作業」，填寫標題與說明，於右側 <strong>「主題」下拉選單指定歸入該單元</strong>。',
                    '附加素材時注意右側檔案權限：選擇 <strong>「為每位學生建立副本」</strong>，學生才能各自作答。',
                    '在主題右側三點圖示點選「移至頂端」，把本週單元排到最上方。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '📝 演練三：測驗作業與成績自動匯入',
                'title': '建立測驗作業 (Quiz Assignment) 並開啟成績匯入 (Grade importing)',
                'intro': '「測驗作業」會自動附上一份已設為<strong>測驗模式</strong>的 Google 表單。'
                         '只要開啟「成績匯入」開關，學生作答完成後，Forms 的自動評分結果就能一鍵帶回 Classroom 成績冊，不必人工謄分。',
                'scenario': '您每週上完一個單元都會做一次線上形成性評量。過去的流程是：學生填 Forms、您開試算表看分數、'
                            '再逐一把分數手動輸入 Classroom 成績冊——一個班就要花掉半節課。您希望這段完全自動化。',
                'task_key': 'Task 11',
                'doc_inst': '請在「課堂作業」點選「建立 ➔ 測驗作業」，確認右側「成績匯入 (Grade importing)」開關已開啟，並於附帶的 Blank Quiz 表單設定答案與配分！',
                'steps': [
                    '在「課堂作業」點選 <strong>「建立 ➔ 測驗作業 (Quiz assignment)」</strong>。',
                    '確認右側 <strong>「成績匯入 (Grade importing)」切換開關已開啟</strong>（此為關鍵步驟）。',
                    '點開系統附帶的 <strong>Blank Quiz</strong> 表單，逐題設定「答案」與配分。',
                    '注意：測驗作業僅能附帶一份表單，且表單須與課程同一網域。',
                    '學生作答後回到成績頁，分數旁會出現 <strong>「匯入成績 (Import grades)」</strong> 按鈕，點選即完成登錄。',
                ],
            },
            {
                'tag': '核心功能演練四',
                'menu': '🔍 演練四：原創性比對報告',
                'title': '開啟原創性比對報告 (Originality reports) 培養學術誠信',
                'intro': '原創性比對會將學生作業與全網頁面（教育版另含校內學生作業庫）比對。'
                         '重點在於<strong>學生自己在提交前最多可跑 3 次</strong>——它是自我檢查的教學工具，不是抓作弊的監控工具。',
                'scenario': '高中社會科要求繳交小論文。您發現學生並非刻意抄襲，而是不清楚「引用」與「抄襲」的界線在哪裡。'
                            '您希望學生在按下繳交之前，就能自己看到哪幾段與網路資料雷同，並有機會修改與補上引註。',
                'task_key': 'Task 12',
                'doc_inst': '請在建立作業時，於右側側邊欄勾選「檢查原創性 (Check plagiarism / Originality reports)」，並在說明中告知學生提交前可自行檢查 3 次！',
                'steps': [
                    '在「課堂作業」點選「建立 ➔ 作業」，填寫小論文題目與繳交期限。',
                    '在右側側邊欄<strong>勾選「檢查原創性 (Originality reports)」</strong>。',
                    '留意免費版有<strong>啟用作業數量上限</strong>（教育版 Plus 無限制），請保留給重要的寫作作業。',
                    '在作業說明中告知學生：繳交前可自行執行最多 <strong>3 次</strong>比對並修改。',
                    '學生提交後，教師端亦會自動產生一份比對報告供批閱參考。',
                ],
            },
        ],
    },
    {
        'file': 'calendar_workshop_app.html',
        'emoji': '📅',
        'name': 'Google Calendar',
        'title': 'Google Calendar 時間管理與會議整合研習講義',
        'subtitle': '預約時間表 ‧ 直播串流 ‧ 與會者權限 ‧ 會議紀錄連動',
        'overview_lead': '歡迎來到 <strong>Google Calendar（Google 日曆）</strong>工具篇講義！'
                         '日曆不只是記事本，而是<strong>整個 Workspace 的會議樞紐</strong>——預約、視訊、直播、共筆紀錄與個資保護，都從這裡發動。',
        'goals': [
            '<strong>演練一</strong>：建立預約時間表，讓學生／家長自助預約且絕不撞期。',
            '<strong>演練二</strong>：在活動中新增 Meet 視訊並加開串流直播，容納大型跨校講座。',
            '<strong>演練三</strong>：設定 Email 提醒與與會者權限，避免外部名單個資外洩。',
            '<strong>演練四</strong>：一鍵新增會議紀錄，權限自動同步給所有與會者。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '🗓️ 演練一：預約時間表 (Appointment Schedule)',
                'title': '諮詢／親師面談預約時間表設定與公開網址發布',
                'intro': '「預約時間表」會依您設定的開放時段自動產生一個公開預約頁。對方選走的時段會即時消失，'
                         '而且系統會<strong>自動比對您日曆上既有的行程</strong>，衝突時段不會被預約走。',
                'scenario': '您每週三下午開放 2 小時提供學生課後諮詢。過去用聯絡簿登記，常發生兩位學生登記同一時段、'
                            '或是您臨時要開會卻已經答應學生的窘境。您希望改成學生自己上網選時段，且系統自動避開您的既有會議。',
                'task_key': 'Task 06',
                'doc_inst': '請在 Google Calendar 點選「建立 ➔ 預約時間表」，設定單次 20 分鐘的諮詢時段與每週開放時間，並複製公開預約網址！',
                'steps': [
                    '在 Google Calendar 左上角點選 <strong>「建立 ➔ 預約時間表 (Appointment schedule)」</strong>。',
                    '設定<strong>單次時段長度</strong>（如 20 分鐘）與每週重複的開放時間區間。',
                    '展開設定，勾選<strong>「與行事曆檢查衝突」</strong>，並可設定預約緩衝時間與最大預約數。',
                    '儲存後點選 <strong>「共用 ➔ 複製預約網址」</strong>。',
                    '將網址貼到班網或 Classroom 公告；驗證：他人開啟只會看到尚未被預約的空閒時段。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '📹 演練二：Meet 視訊與串流直播',
                'title': '活動排定、新增 Google Meet 視訊與開啟串流直播 (Live stream)',
                'intro': 'Meet 視訊會議有人數上限，且所有人都能開麥克風；當觀眾多達數百人且只需「觀看」時，'
                         '正確作法是加開<strong>串流直播</strong>——直播網址的觀眾只能看，不會干擾會場，也不佔用會議人數。',
                'scenario': '您負責承辦一場跨校線上講座。主講者與各校代表約 20 人需要互動問答，'
                            '但同時要開放全校數百名師生線上觀看。若全部塞進同一個 Meet，不僅超過人數上限，秩序也會失控。',
                'task_key': 'Task 07',
                'doc_inst': '請建立日曆活動並點選「新增 Google Meet 視訊會議」，再展開視訊下拉選單點選「新增串流直播 (Add live stream)」，取得兩組網址！',
                'steps': [
                    '在 Calendar 建立講座活動，填寫標題、時間與邀請主講者。',
                    '點選 <strong>「新增 Google Meet 視訊會議」</strong>，產生會議網址。',
                    '點選視訊選項旁的<strong>下拉箭頭 ➔ 「新增串流直播 (Add live stream)」</strong>。',
                    '儲存活動，取得<strong>兩組網址</strong>：Meet 會議網址（給講者與代表）、直播觀看網址（給全校師生）。',
                    '注意：直播需由主辦者於會議中手動點選「開始串流」才會正式播出。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '🔒 演練三：Email 提醒與與會者權限',
                'title': '設定活動通知提醒與精確的與會者權限 (Guest permissions) 防護',
                'intro': '日曆活動預設允許與會者<strong>互相看見完整名單，也能自行邀請他人</strong>。'
                         '涉及外部專家、家長或學生時，這等同於把整份 Email 名單公開，必須主動關閉。',
                'scenario': '您要召開一場邀請多位校外專家與家長代表出席的會議。'
                            '您希望所有人在會議前 1 小時收到 Email 提醒，但絕不能讓與會者看到彼此的 Email、也不能讓任何人自行把其他人拉進來。',
                'task_key': 'Task 08',
                'doc_inst': '請在活動設定中新增「Email、1 小時前」通知，並在與會者權限區塊取消勾選「邀請他人」與「查看與會者名單」！',
                'steps': [
                    '開啟活動編輯頁面，於「通知」區塊點選新增，選取 <strong>「Email」</strong>、時間設為 <strong>「1 小時前」</strong>。',
                    '在「與會者權限 (Guest permissions)」區塊，<strong>取消勾選「邀請他人 (Invite others)」</strong>。',
                    '<strong>取消勾選「查看與會者名單 (See guest list)」</strong>，彼此的 Email 即互相隱藏。',
                    '視需要保留或取消「修改活動」權限。',
                    '儲存並驗證：以與會者身分開啟活動，應看不到其他人的名單。',
                ],
            },
            {
                'tag': '核心功能演練四',
                'menu': '📝 演練四：會議紀錄一鍵連動共筆',
                'title': '新增會議紀錄 (Meeting notes) 自動建立共筆並同步權限',
                'intro': '在日曆活動點一下「新增會議紀錄」，系統會自動生成一份 Docs，'
                         '<strong>已預先填好會議標題、日期、與會者與議程欄位，並自動把編輯權限給所有與會者</strong>——不必再手動分享。',
                'scenario': '每次教研會開會，您都要先開一份新文件、貼上與會名單、再一個一個加人共享，'
                            '常常會議都開始了還有人說「我沒有權限」。您希望開會前一秒就能備妥一份大家都打得開的共筆紀錄。',
                'task_key': 'Task 09',
                'doc_inst': '請在日曆活動編輯視窗點選「新增會議紀錄 (Add meeting notes)」自動產生共筆 Docs，並在文件中選取段落新增註解 +成員Email 指派後續追蹤事項！',
                'steps': [
                    '開啟教研會日曆活動，於說明欄位上方點選 <strong>「新增會議紀錄 (Add meeting notes)」</strong>。',
                    '系統自動建立 Docs 並附加於活動；文件已帶入標題、日期與出席者欄位。',
                    '確認<strong>與會者已自動獲得編輯權限</strong>（不需另外分享）。',
                    '會議中共同記錄；結束前選取待辦段落<strong>新增註解輸入 <code>+成員Email</code></strong>。',
                    '<strong>勾選「指派給…」</strong>，把後續追蹤事項直接派給負責同仁。',
                ],
            },
        ],
    },
    {
        'file': 'meet_workshop_app.html',
        'emoji': '📹',
        'name': 'Google Meet',
        'title': 'Google Meet 視訊教學與備援連線研習講義',
        'subtitle': '電話撥號備援 ‧ 檔案內視訊 ‧ 會議主持控制',
        'overview_lead': '歡迎來到 <strong>Google Meet</strong> 工具篇講義！'
                         '本單元聚焦在真實教學現場最容易出狀況的兩件事：<strong>網路不穩時怎麼撐住會議</strong>，'
                         '以及<strong>如何邊看文件邊視訊討論</strong>，另補充主持人必備的秩序控制設定。',
        'goals': [
            '<strong>演練一</strong>：網路訊號不良時，改用電話撥號加入 (Join by phone) 維持參與。',
            '<strong>演練二</strong>：直接在 Docs／Slides 檔案內發起 Meet，邊視訊邊共同編修。',
            '<strong>演練三</strong>：善用主持人控制項與分組討論室，維持線上課堂秩序。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '📞 演練一：電話撥號加入 (Join by phone)',
                'title': '網路不穩時開啟「透過電話撥號加入 (Join by phone)」語音備援',
                'intro': '當頻寬不足以支撐視訊時，關鏡頭往往還是卡。Meet 提供<strong>改走電話語音線路</strong>的備援：'
                         '畫面由電腦顯示、聲音走行動電話網路，只要手機有訊號就能穩定聽與說。',
                'scenario': '您帶學生到山區進行戶外觀察，同一時間校內正在召開臨時教學會議必須出席。'
                            '現場行動網路訊號只有一格，視訊完全連不上，但手機通話仍然正常。',
                'task_key': 'Task 20',
                'doc_inst': '請在 Meet 會議中點選右下角「三點圖示 ➔ 使用電話收聽及發言」，依畫面提示撥打號碼並輸入 PIN 碼完成語音接入！',
                'steps': [
                    '進入 Meet 會議，點選右下角 <strong>「更多選項（三點圖示）」</strong>。',
                    '點選 <strong>「使用電話收聽及發言 (Use a phone for audio)」</strong>。',
                    '選擇<strong>「撥號 (Dial in)」</strong>，記下畫面顯示的電話號碼與 <strong>PIN 碼</strong>。',
                    '用手機撥打該號碼，依語音提示輸入 PIN 碼與 <code>#</code>。',
                    '驗證：電腦端音訊自動靜音，聲音改由電話進出，會議不再斷續。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '💻 演練二：Docs／Slides 檔案內發起 Meet',
                'title': '從 Google Docs/Slides 頂部工具列直接發起或加入 Meet 會議',
                'intro': '檔案內 Meet 整合可讓視訊小窗<strong>浮動在文件右側</strong>，一邊開會一邊即時修改同一份檔案，'
                         '省去「切分頁 ➔ 分享畫面 ➔ 對方看不到游標」的來回。',
                'scenario': '您與學年夥伴要共同修訂一份課程計畫。若用傳統作法，得先開 Meet、再分享畫面，'
                            '對方只能看不能改，改到哪還要口頭說「第三段第二行」。您希望大家能同時在文件裡動手改，視訊就在旁邊。',
                'task_key': 'Task 25',
                'doc_inst': '請開啟共編文件，點選右上角的 Meet 視訊圖示，選擇「在此發起新會議」，並實測在視訊進行中同步編輯文件內容！',
                'steps': [
                    '開啟要共編的 Google Docs／Slides 檔案。',
                    '點選右上角的 <strong>Meet 視訊圖示</strong>。',
                    '選擇 <strong>「在此發起新會議」</strong>（或加入已排定的會議）。',
                    '視訊窗格會固定於文件右側，可將會議<strong>畫面分享改為「分享此分頁」</strong>讓他人同步看到文件。',
                    '驗證：視訊進行中，雙方游標可同時在文件上編輯同一段落。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '🎛️ 演練三：主持人控制項與分組討論',
                'title': '主持人控制項 (Host controls) 與分組討論室 (Breakout rooms)',
                'intro': '主持人控制項能一鍵限制學生的分享畫面、聊天與麥克風權限；'
                         '分組討論室則可把全班自動或手動分到不同小房間，教師可<strong>逐室巡堂</strong>並廣播訊息。',
                'scenario': '線上授課時，常有學生誤按分享畫面打斷課程，或在聊天室洗版。'
                            '同時，這節課要進行小組討論，您需要把 30 位學生分成 6 組各自討論，再逐組去聽他們講得如何。',
                'task_key': 'Task 20',
                'doc_inst': '請於同一場 Meet 會議中開啟「主持人控制項」關閉學生分享畫面與聊天權限，再點選活動面板建立 6 間分組討論室並實測逐室巡堂！',
                'steps': [
                    '在 Meet 右下角點選 <strong>「主持人控制項 (Host controls)」</strong> 盾牌圖示。',
                    '關閉 <strong>「分享畫面」與「傳送聊天訊息」</strong>權限（必要時再逐一開放）。',
                    '點選右下角 <strong>「活動 (Activities) ➔ 分組討論室 (Breakout rooms)」</strong>。',
                    '設定房間數量（如 6 間）與討論時間，可手動拖曳調整成員後點選「開啟」。',
                    '教師端點選各房間 <strong>「加入」逐室巡堂</strong>，並可用「廣播」對全部房間發送提醒。',
                ],
            },
        ],
    },
    {
        'file': 'forms_workshop_app.html',
        'emoji': '📋',
        'name': 'Google Forms',
        'title': 'Google Forms 差異化評量與自動化研習講義',
        'subtitle': '區段跳轉分流 ‧ 測驗自動評分 ‧ 回應統計',
        'overview_lead': '歡迎來到 <strong>Google Forms（Google 表單）</strong>工具篇講義！'
                         '本單元的核心概念是：表單不只是收資料，而是能<strong>依學生的答案給出不同路徑</strong>的差異化評量工具。',
        'goals': [
            '<strong>演練一</strong>：用區段跳轉，讓答對與答錯的學生走向不同的學習路徑。',
            '<strong>演練二</strong>：設定測驗模式的答案、配分與即時回饋，並與 Classroom 成績冊連動。',
            '<strong>演練三</strong>：善用回應摘要圖表與「回應驗證」，收到乾淨可用的資料。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '🔀 演練一：區段跳轉與差異化分流',
                'title': 'Forms 內嵌教學影片與依據回應跳轉區段 (Go to section based on answer)',
                'intro': '在單選題右下角三點選單開啟<strong>「根據答案前往相關部分」</strong>後，'
                         '每個選項都能指定跳到不同區段。這是用一份表單同時做到<strong>補救教學與加深加廣</strong>的關鍵設定。',
                'scenario': '您採翻轉教室模式，課前要學生先看一段影片並回答檢核題。'
                            '答對的學生應直接進入進階挑戰題，答錯的學生則該被導到補充說明與再一次練習，而不是全班看同樣的內容。',
                'task_key': 'Task 23',
                'doc_inst': '請在表單中插入教學影片，建立「進階區段」與「補救區段」，並在檢核題三點選單開啟「根據答案前往相關部分」，逐一指定各選項的去向！',
                'steps': [
                    '點選右側工具列 <strong>「插入影片」</strong>，貼上或搜尋 YouTube 教學影片。',
                    '點選 <strong>「新增區段 (Add section)」</strong>，分別建立「進階挑戰」與「補救說明」兩個區段。',
                    '回到檢核題（須為<strong>單選題</strong>），點選右下角三點圖示。',
                    '勾選 <strong>「根據答案前往相關部分 (Go to section based on answer)」</strong>。',
                    '在每個選項右側指定跳轉區段；並將補救區段結尾設為<strong>「返回檢核題」或「提交表單」</strong>，避免學生誤入進階題。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '💯 演練二：測驗模式自動評分與成績連動',
                'title': '開啟測驗模式 (Make this a quiz)、設定答案配分與即時回饋',
                'intro': '測驗模式能自動評分並<strong>對答錯的學生顯示您預先寫好的解說與參考連結</strong>。'
                         '搭配 Classroom 的「測驗作業」，分數可一鍵匯入成績冊，完全免去謄分。',
                'scenario': '您每週進行一次線上形成性評量。您希望學生一按送出就立刻知道對錯，'
                            '而且答錯時能看到「為什麼錯」的說明與複習連結，而不是等您隔天上課才公布答案。',
                'task_key': 'Task 11',
                'doc_inst': '請於表單「設定 ➔ 測驗」開啟測驗模式，逐題點選「答案」設定正解與配分，並在答錯回饋中加入解說文字與複習連結！',
                'steps': [
                    '點選表單上方 <strong>「設定 (Settings) ➔ 設為測驗 (Make this a quiz)」</strong>。',
                    '設定成績發布方式：<strong>「提交後立即公布」</strong>即為自動評分即時回饋。',
                    '回到題目，點選左下角 <strong>「答案 (Answer key)」</strong>，選取正解並輸入配分。',
                    '點選 <strong>「新增答案意見回饋」</strong>，替<strong>答錯</strong>撰寫解說並附上複習資源連結。',
                    '在 Classroom 以<strong>「測驗作業」</strong>發布此表單，作答後即可一鍵匯入成績。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '📈 演練三：回應驗證與統計分析',
                'title': '回應驗證 (Response validation) 與回應摘要圖表分析',
                'intro': '「回應驗證」可限制填答格式（如必須為數字、必須是 Email、字數上限），'
                         '從源頭確保資料乾淨；「回應」分頁則自動產生統計圖表，並可一鍵匯出至 Sheets 做進一步分析。',
                'scenario': '上次收家長回條時，學生座號欄有人填「5 號」、有人填「五」、有人填「05」，'
                            '導致最後無法排序統計，您花了一小時手動整理。這次您希望資料收進來就是可直接統計的格式。',
                'task_key': 'Task 19',
                'doc_inst': '請對座號題目開啟「回應驗證」限定為數字且介於 1 至 30，再切換到「回應」分頁檢視統計圖表，並點選試算表圖示匯出至 Sheets！',
                'steps': [
                    '點選題目右下角三點圖示，勾選 <strong>「回應驗證 (Response validation)」</strong>。',
                    '設定規則為<strong>「數字 ➔ 介於 ➔ 1 至 30」</strong>，並自訂錯誤提示文字。',
                    '在必填題目開啟<strong>「必填 (Required)」</strong>開關。',
                    '切換至上方 <strong>「回應 (Responses)」</strong> 分頁，檢視自動生成的統計圖表。',
                    '點選右上角<strong>試算表圖示</strong>，將回應連結至 Google Sheets 做樞紐分析。',
                ],
            },
        ],
    },
    {
        'file': 'sites_workshop_app.html',
        'emoji': '🌐',
        'name': 'Google Sites',
        'title': 'Google Sites 學習歷程與成果展示研習講義',
        'subtitle': '子頁面架構 ‧ 發布權限 ‧ 內嵌內容連動',
        'overview_lead': '歡迎來到 <strong>Google Sites（Google 協作平台）</strong>工具篇講義！'
                         '本單元聚焦兩個 Level 2 最容易失分、實務上也最常出包的重點：<strong>網站結構怎麼分層</strong>，'
                         '以及<strong>為什麼外部訪客會看到「無權限」</strong>。',
        'goals': [
            '<strong>演練一</strong>：用子頁面（Subpages）建立各組專題的階層式導覽。',
            '<strong>演練二</strong>：正確設定發布權限，讓校外評審不必登入也能瀏覽全站。',
            '<strong>演練三</strong>：內嵌 Docs／Slides／Forms 並確認其個別權限一致。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '🗂️ 演練一：子頁面與網站導覽架構',
                'title': '建立網站並為各小組新增專屬子頁面 (Subpages)',
                'intro': '子頁面會在頂部導覽列自動形成<strong>下拉式選單</strong>，讓網站從一排平行分頁'
                         '變成有層次的目錄結構。頁面順序也可直接在「頁面」面板中拖曳調整。',
                'scenario': '班級自然科進行 PBL 專題，共有六個小組。您要建立一個成果展示網站，'
                            '希望首頁介紹整體專題，各組則有自己獨立的展演頁面，觀看者能從導覽列直接下拉切換組別。',
                'task_key': 'Task 16',
                'doc_inst': '請在網站右側點選「頁面」面板，於首頁下方新增六個子頁面（第一組～第六組），並拖曳調整排列順序！',
                'steps': [
                    '開啟 Google Sites，點選右側 <strong>「頁面 (Pages)」</strong> 面板。',
                    '將滑鼠移至要作為母頁的頁面，點選其<strong>三點圖示 ➔ 「新增子頁面 (Add subpage)」</strong>。',
                    '輸入頁面名稱（如「第一組」），重複建立各組頁面。',
                    '在面板中<strong>拖曳頁面</strong>調整順序與階層（拖到某頁下方即成為其子頁）。',
                    '驗證：頂部導覽列該項目出現<strong>下拉式選單</strong>，可切換各組頁面。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '🔓 演練二：發布權限與外部公開',
                'title': '發布設定：網站設為 Public 與內嵌文件「發布至網路」',
                'intro': '這是最經典的陷阱：<strong>把網站設為公開，不等於網站裡內嵌的檔案也公開</strong>。'
                         'Sites 權限與 Drive 檔案權限是兩套獨立系統，兩邊都要設定，外部訪客才不會看到一片空白或「你需要存取權」。',
                'scenario': '學生的學習歷程檔案網站要提供給校外大學教授審閱。'
                            '您預覽時一切正常（因為您本來就有權限），但教授回報說網站打得開，裡面內嵌的作品文件卻顯示「你需要存取權」。',
                'task_key': 'Task 17',
                'doc_inst': '請點選右上角「發布」，將管理權限設為「公開 (Public)」，再逐一開啟內嵌的 Docs 檔案點選「檔案 ➔ 共用 ➔ 發布到網路」！',
                'steps': [
                    '點選 Sites 右上角 <strong>「發布 (Publish)」</strong>，設定網址名稱。',
                    '在「可查看的使用者」點選<strong>「管理 ➔ 變更為公開 (Public)」</strong>。',
                    '開啟網站中<strong>每一份內嵌的 Docs／Slides／Sheets</strong>。',
                    '在檔案中點選 <strong>「檔案 ➔ 共用 ➔ 發布到網路 (Publish to the web)」</strong>，或將共用權限設為知道連結者可檢視。',
                    '以<strong>無痕視窗（未登入狀態）</strong>開啟網址驗證：全站與內嵌文件皆能正常瀏覽。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '🧩 演練三：內嵌動態內容與即時更新',
                'title': '內嵌 Drive 檔案、Forms 與 YouTube 打造會自動更新的成果網站',
                'intro': '從「插入」面板嵌入的 Drive 檔案是<strong>即時連動</strong>的：'
                         '原始檔案改了，網站上顯示的內容也跟著更新，不必重新上傳，也不必重新發布網站。',
                'scenario': '專題成果網站上要放各組的簡報、一份回饋表單與一段成果影片。'
                            '各組的簡報在展演前還會持續修改，您不希望每改一次就要您重新上傳一次到網站。',
                'task_key': 'Task 16',
                'doc_inst': '請於同一網站中，用右側「插入」面板分別嵌入一份 Slides 簡報、一份 Forms 回饋表單與一段 YouTube 影片，並實測修改原始簡報後網站是否同步更新！',
                'steps': [
                    '在右側 <strong>「插入 (Insert)」</strong> 面板點選 <strong>「Slides」</strong>，選取各組簡報檔案。',
                    '點選 <strong>「Forms」</strong> 嵌入回饋表單（訪客可直接在網站上填寫送出）。',
                    '點選 <strong>「YouTube」</strong> 嵌入成果影片，調整區塊寬度與版面。',
                    '修改原始簡報內容後，重新整理網站頁面驗證<strong>內容已同步更新</strong>。',
                    '提醒：內嵌檔案的<strong>共用權限仍須另外設定</strong>（見演練二）。',
                ],
            },
        ],
    },
    {
        'file': 'practicesets_workshop_app.html',
        'emoji': '💡',
        'name': 'Practice Sets',
        'title': 'Practice Sets 自主練習與學習鷹架研習講義',
        'subtitle': '額外協助鷹架 ‧ 題組共享 ‧ 學習成效洞察',
        'overview_lead': '歡迎來到 <strong>Practice Sets（練習組）</strong>工具篇講義！'
                         'Practice Sets 與一般測驗最大的差別是：它<strong>在學生卡關的當下就給提示</strong>，'
                         '並自動標示出全班共同的迷思概念，是自主學習與補救教學的利器。',
        'goals': [
            '<strong>演練一</strong>：為題目加上「額外協助」影音資源，建立即時學習鷹架。',
            '<strong>演練二</strong>：開啟連結共用，把自製題組分享給同科備課團隊複製使用。',
            '<strong>演練三</strong>：閱讀學生作答洞察報告，找出需要補救的學生與概念。',
        ],
        'modules': [
            {
                'tag': '核心功能演練一',
                'menu': '🪜 演練一：額外協助 (Extra Help) 學習鷹架',
                'title': '在題目中設定「額外協助 (Extra help)」影音學習資源',
                'intro': 'Practice Sets 允許每題掛上多筆學習資源（YouTube 影片、網頁或自製說明）。'
                         '學生答錯或卡住時可自行點開查看，形成<strong>不必等老師到場的即時鷹架</strong>。',
                'scenario': '國中理化的自主複習題組，班上程度落差大。'
                            '程度好的學生一路做完，卡關的學生則是坐在那裡發呆等您走過去；您無法同時照顧 30 個人，'
                            '希望學生卡住時能自己先看一段解題說明再試一次。',
                'task_key': 'Task 21',
                'doc_inst': '請建立練習組，在題目下方點選「額外協助 (Extra help)」，新增 YouTube 解題影片或教學網頁作為學習資源！',
                'steps': [
                    '在 Google Classroom 點選 <strong>「建立 ➔ 練習組 (Practice sets)」</strong>。',
                    '輸入題目與答案（系統會自動辨識可用的作答型式）。',
                    '在該題下方點選 <strong>「額外協助 (Extra help)」</strong>。',
                    '點選 <strong>「+ 新增資源」</strong>，搜尋內嵌 YouTube 解題影片或貼上教學網頁連結。',
                    '驗證：以學生身分作答，卡關時可點開資源自行觀看後再作答。',
                ],
            },
            {
                'tag': '核心功能演練二',
                'menu': '🔗 演練二：題組連結共享給備課團隊',
                'title': '開啟連結共用 (Turn on link sharing) 分享題組給同科教師',
                'intro': 'Practice Sets 開啟連結共用後，其他教師點選連結即可<strong>複製一份到自己的 Classroom</strong>，'
                         '各自修改不會影響原始版本——這是學年共備最有效率的散播方式。',
                'scenario': '您花了兩個晚上做好一份高品質的理化練習題組。'
                            '同科三位夥伴都想用，但您不希望他們直接在您的原始檔上改動，也不想一份一份重做給他們。',
                'task_key': 'Task 22',
                'doc_inst': '請開啟已建立的練習組，點選右上角「分享」並開啟「連結共用 (Link sharing)」，複製連結傳送給同科備課夥伴！',
                'steps': [
                    '開啟已建立完成的練習組。',
                    '點選右上角 <strong>「分享 (Share)」</strong>。',
                    '點選 <strong>「開啟連結共用 (Turn on link sharing)」</strong>。',
                    '複製連結，透過 Email 或群組發送給同科教師。',
                    '驗證：夥伴點選連結後可<strong>複製題組至自己的 Classroom</strong>，修改不影響您的原始版本。',
                ],
            },
            {
                'tag': '核心功能演練三',
                'menu': '📊 演練三：作答洞察與補救教學決策',
                'title': '閱讀學生作答洞察報告 (Insights) 精準規劃補救教學',
                'intro': 'Practice Sets 會自動彙整全班作答狀況，標示出<strong>「需要協助的學生」與「全班常錯的題目」</strong>，'
                         '並記錄學生是否使用過提示資源——這讓補救教學的對象與內容有客觀依據，不再憑印象。',
                'scenario': '這份複習題組全班都做完了，您需要決定下週補救教學的時段要找誰、要重講哪一個概念，'
                            '而不是憑上課的印象猜「好像是浮力那邊怪怪的」。',
                'task_key': 'Task 22',
                'doc_inst': '請開啟已完成作答的練習組，切換至教師端成效檢視頁面，找出被系統標示為「需要協助」的學生與全班錯誤率最高的題目！',
                'steps': [
                    '在 Classroom 開啟該練習組，切換至<strong>教師端作答成效檢視</strong>。',
                    '查看系統自動標示的 <strong>「需要協助的學生 (Students who may need help)」</strong> 名單。',
                    '檢視<strong>各題錯誤率排序</strong>，找出全班共同的迷思概念。',
                    '確認學生是否曾點開「額外協助」資源，判斷是不懂還是沒去看。',
                    '依據結果排定補救教學名單與重講的概念，並針對高錯誤率題目補充新的學習資源。',
                ],
            },
        ],
    },
]


# ---------------------------------------------------------------- 版型（沿用 Docs 篇）
def build_module_card(idx, m):
    info = LINKS.get(m['task_key'], {})
    url = info.get('url', '#')
    t_title = info.get('title', m['title'])
    f_type = info.get('type', 'Docs')
    type_label = TYPE_LABEL.get(f_type, 'Google Docs')
    type_icon = TYPE_ICON.get(f_type, '📄')

    steps_list = ''
    for s_idx, s in enumerate(m['steps'], 1):
        steps_list += f'''
          <div class="step-item">
            <input type="checkbox" id="m{idx}-s{s_idx}">
            <label for="m{idx}-s{s_idx}">{s}</label>
          </div>'''

    return f'''
      <!-- MODULE {idx} -->
      <div class="module-card" id="module-{idx}" style="display:none;">
        <span class="tag">{m["tag"]}</span>
        <h2>{m["title"]}</h2>
        <p>{m["intro"]}</p>

        <!-- 1. 黃色區塊：實務教學情境 -->
        <div class="scenario-box">
          <strong>【實務教學情境】</strong>：<br>
          {m["scenario"]}
        </div>

        <!-- 2. 綠色區塊：線上真實實作檔案與具體修改任務 -->
        <div style="background:#e6f4ea; border:2px solid #34a853; border-radius:12px; padding:18px; margin:18px 0; box-shadow:0 2px 8px rgba(0,0,0,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; margin-bottom:10px;">
            <strong style="color:#137333; font-size:1.05rem; display:flex; align-items:center; gap:6px;">
              🔗 本單元線上真實 {type_label} 實作檔案：
            </strong>
            <a href="{url}" target="_blank" style="text-decoration:none; background:#137333; color:white; padding:10px 22px; border-radius:20px; font-weight:700; font-size:0.92rem; box-shadow:0 3px 8px rgba(0,0,0,0.15); transition:all 0.2s;">{type_icon} 點此開啟真實 {type_label} 實作檔</a>
          </div>
          <div style="background:white; border:1px solid #a8dab5; border-radius:8px; padding:12px 16px; margin-top:8px;">
            <div style="font-size:0.88rem; color:#5f6368; margin-bottom:4px;">檔名：<strong>{t_title}</strong>（{m["task_key"]}）</div>
            <div style="font-size:0.95rem; color:#137333; font-weight:700; line-height:1.5;">
              🎯 本檔具體修改任務：<span style="color:#202124; font-weight:500;">{m["doc_inst"]}</span>
            </div>
          </div>
        </div>

        <h3>▶️ 實作步驟導引清單：</h3>
        <div class="step-list">
          {steps_list}
        </div>

        <div class="action-bar">
          <button class="btn btn-primary" onclick="copySteps('module-{idx}')">📋 複製本單元操作步驟</button>
        </div>
      </div>
'''


def build_app(app):
    menu_html = f'      <button class="menu-item active" onclick="showModule(0)">🎯 工具篇總覽與研習目標</button>\n'
    for i, m in enumerate(app['modules'], 1):
        menu_html += f'      <button class="menu-item" onclick="showModule({i})">{m["menu"]}</button>\n'

    goals_html = '\n'.join(f'            <li>{g}</li>' for g in app['goals'])

    cards_html = ''
    for i, m in enumerate(app['modules'], 1):
        cards_html += build_module_card(i, m)

    n_word = ['零', '一', '二', '三', '四', '五', '六', '七', '八'][len(app['modules'])]

    return f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{app["title"]} (互動網頁版)</title>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #1a73e8;
      --primary-dark: #1557b0;
      --primary-light: #e8f0fe;
      --secondary: #34a853;
      --text-main: #202124;
      --text-muted: #5f6368;
      --bg-body: #f8f9fa;
      --bg-card: #ffffff;
      --border: #dadce0;
      --shadow: 0 4px 16px rgba(0,0,0,0.06);
      --radius: 12px;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Google Sans', 'Noto Sans TC', sans-serif;
      background: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
    }}

    header {{
      background: var(--primary);
      color: white;
      padding: 24px 32px;
      box-shadow: 0 4px 12px rgba(26,115,232,0.25);
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .header-title h1 {{ font-size: 1.5rem; font-weight: 700; }}
    .header-title p {{ font-size: 0.9rem; opacity: 0.9; margin-top: 4px; }}

    .nav-links {{ display: flex; gap: 8px; flex-wrap: wrap; }}
    .nav-btn {{
      text-decoration: none;
      background: rgba(255,255,255,0.2);
      color: white;
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 600;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{ background: white; color: var(--primary); }}

    .app-layout {{
      max-width: 1200px;
      margin: 28px auto;
      padding: 0 20px;
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 24px;
    }}

    @media (max-width: 900px) {{
      .app-layout {{ grid-template-columns: 1fr; }}
    }}

    .sidebar {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 20px;
      box-shadow: var(--shadow);
      height: fit-content;
      position: sticky;
      top: 100px;
    }}

    .sidebar-heading {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 12px;
    }}

    .menu-item {{
      display: block;
      width: 100%;
      text-align: left;
      border: none;
      background: transparent;
      padding: 12px 14px;
      border-radius: 8px;
      font-size: 0.92rem;
      font-weight: 500;
      color: var(--text-main);
      cursor: pointer;
      margin-bottom: 6px;
      transition: all 0.2s;
    }}

    .menu-item:hover {{ background: var(--bg-body); color: var(--primary); }}
    .menu-item.active {{ background: var(--primary-light); color: var(--primary); font-weight: 700; }}

    .content-area {{
      background: var(--bg-card);
      border-radius: var(--radius);
      padding: 32px;
      box-shadow: var(--shadow);
    }}

    .module-card {{ display: none; }}
    .module-card.active {{ display: block; animation: fadeIn 0.3s ease-in-out; }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .tag {{
      display: inline-block;
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 0.82rem;
      font-weight: 700;
      margin-bottom: 12px;
    }}

    h2 {{ font-size: 1.4rem; font-weight: 700; margin-bottom: 16px; color: var(--primary-dark); }}
    h3 {{ font-size: 1.1rem; font-weight: 700; margin: 20px 0 10px 0; color: var(--text-main); }}
    p {{ margin-bottom: 14px; color: #3c4043; line-height: 1.7; }}

    .scenario-box {{
      background: #fef7e0;
      border-left: 4px solid #f9ab00;
      padding: 16px;
      border-radius: 0 8px 8px 0;
      margin: 20px 0;
    }}

    .scenario-box strong {{ color: #b06000; }}

    .step-list {{
      background: #f8f9fa;
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 20px;
      margin: 20px 0;
    }}

    .step-item {{
      display: flex;
      gap: 12px;
      align-items: flex-start;
      margin-bottom: 12px;
    }}

    .step-item input[type="checkbox"] {{
      margin-top: 5px;
      width: 18px;
      height: 18px;
      cursor: pointer;
    }}

    code {{
      background: #f1f3f4;
      padding: 1px 6px;
      border-radius: 4px;
      font-size: 0.92em;
      color: #c5221f;
    }}

    .action-bar {{
      display: flex;
      gap: 12px;
      margin-top: 24px;
    }}

    .btn {{
      border: none;
      padding: 10px 20px;
      border-radius: 20px;
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .btn-primary {{ background: var(--primary); color: white; }}
    .btn-primary:hover {{ background: var(--primary-dark); }}

    .toast {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #323232;
      color: white;
      padding: 12px 24px;
      border-radius: 8px;
      font-size: 0.9rem;
      display: none;
      z-index: 1000;
    }}
  </style>
</head>
<body>

  <header>
    <div class="header-title">
      <h1>{app["emoji"]} {app["title"]}</h1>
      <p>{app["subtitle"]}</p>
    </div>
    <div class="nav-links">
      <a href="study_guide_app.html" class="nav-btn">📖 回研習主講義</a>
      <a href="docs_workshop_app.html" class="nav-btn" target="_blank">📄 Docs 工具篇</a>
      <a href="quiz_app.html" class="nav-btn" target="_blank">📝 25 題雙語刷題 App</a>
      <a href="hands_on_tasks_app.html" class="nav-btn" target="_blank">🛠️ 25 個實作演練</a>
    </div>
  </header>

  <div class="app-layout">

    <!-- Sidebar Navigation -->
    <nav class="sidebar">
      <div class="sidebar-heading">實務演練章節選單</div>
{menu_html}    </nav>

    <!-- Main Content Area -->
    <main class="content-area">

      <!-- MODULE 0: OVERVIEW -->
      <div class="module-card active" id="module-0" style="display:block;">
        <span class="tag">研習簡介與教學策略</span>
        <h2>{app["name"]} 實務應用總覽</h2>
        <p>{app["overview_lead"]}</p>

        <div style="background:#e8f0fe; border-radius:12px; padding:20px; margin:20px 0;">
          <h3 style="color:#1a73e8; margin-top:0;">💡 本章{n_word}大實務演練目標：</h3>
          <ul style="padding-left:20px; line-height:1.8; color:#3c4043;">
{goals_html}
          </ul>
        </div>

        <div class="scenario-box">
          <strong>【使用方式】</strong>：<br>
          每個演練都附上一份<strong>真實可開啟的 Google Workspace 檔案</strong>。請先讀「實務教學情境」了解為什麼要做，
          再點綠色按鈕開啟檔案，照著「本檔具體修改任務」實際動手改一次，最後用步驟清單逐項打勾確認。
        </div>
      </div>

{cards_html}
    </main>
  </div>

  <div class="toast" id="toast">已複製操作步驟至剪貼簿！</div>

  <script>
    function showModule(idx) {{
      document.querySelectorAll('.menu-item').forEach((btn, i) => {{
        btn.classList.toggle('active', i === idx);
      }});
      document.querySelectorAll('.module-card').forEach((card, i) => {{
        card.style.display = (i === idx) ? 'block' : 'none';
        card.classList.toggle('active', i === idx);
      }});
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function copySteps(modId) {{
      const mod = document.getElementById(modId);
      const title = mod.querySelector('h2').innerText;
      const steps = Array.from(mod.querySelectorAll('.step-item label'))
        .map((l, i) => `${{i + 1}}. ${{l.innerText}}`)
        .join('\\n');

      const text = `【${{title}}】\\n${{steps}}`;
      navigator.clipboard.writeText(text).then(() => {{
        const toast = document.getElementById('toast');
        toast.style.display = 'block';
        setTimeout(() => toast.style.display = 'none', 2500);
      }});
    }}
  </script>
</body>
</html>
'''


if __name__ == '__main__':
    for app in APPS:
        html = build_app(app)
        path = os.path.join(ROOT, app['file'])
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"OK  {app['file']:34s} modules={len(app['modules'])}  size={len(html):,}")
    print('\nAll tool workshop apps rebuilt with Docs-level layout.')
