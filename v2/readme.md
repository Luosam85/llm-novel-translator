# v2 - 功能擴充版｜Feature Expansion

> v2 是在 v1 穩定運行後，根據實際使用經驗提出的改版需求。  
> 這次的重點是：修掉已知 Bug、新增批次處理能力、讓工具真正可以長時間使用。

---

## 🆕 相較 v1 的變更

| 項目 | v1 | v2 |
|------|----|----|
| LLM 廢話前言 | ❌ 會出現 | ✅ 自動過濾 |
| 批次翻譯 | ❌ 無 | ✅ 整個資料夾一次翻 |
| 語言選擇 | ❌ 固定日→中 | ✅ 可自由選擇 |
| Prompt 編輯 | ❌ 無法修改 | ✅ 可編輯，附重設按鈕 |
| 降速冷卻 | ❌ 無 | ✅ 可設定翻X分鐘休息Y分鐘 |
| Python 環境 | — | ✅ Embeddable，零安裝可攜 |

---

## 📁 檔案說明

```
v2/
├── novel-translator-v2-0808.html   # 主程式，瀏覽器開啟
├── server.py                        # 本地伺服器（批次翻譯用）
├── 啟動伺服器.bat                   # 雙擊啟動 server.py
└── README.md                        # 本文件
```

---

## 🚀 使用方式

### 單檔翻譯
1. 確認 LM Studio Local Server 已啟動
2. 用瀏覽器開啟 `novel-translator-v2-0808.html`
3. 點擊 ⚙ 設定 API 網址與模型名稱
4. 選擇語言，貼上原文或載入 `.txt`
5. 點擊「開始翻譯」

### 批次翻譯（需要 Python）

**方法 A：系統已安裝 Python**
直接雙擊 `啟動伺服器.bat`

**方法 B：Python Embeddable（零安裝）**
1. 從 [python.org](https://www.python.org/downloads/windows/) 下載 `Windows embeddable package (64-bit)`
2. 解壓縮到 `v2/python-embed/` 資料夾
3. 雙擊 `啟動伺服器.bat`

伺服器啟動後，切換到「批次翻譯」頁籤，輸入來源資料夾路徑即可。

### 批次翻譯注意事項
- 輸出資料夾自動建立在來源資料夾同層，名稱為 `原資料夾名稱_翻譯`
- 若輸出資料夾已存在，程式會警告並停止，需手動改名後再試

---

## ⚙️ 設定說明

### Prompt 編輯
設定面板中可直接修改送給 LLM 的系統提示詞。支援以下佔位符：

| 佔位符 | 說明 |
|--------|------|
| `{src}` | 原文語言 |
| `{dst}` | 目標語言 |
| `{style}` | 翻譯風格 |

點擊「重設為預設」可還原 v1 穩定版的原始 Prompt。

### 降速冷卻
啟用後，翻譯滿 X 分鐘會自動暫停 Y 分鐘，讓 GPU 降溫後再繼續。  
進度條在冷卻期間會變為橘色，並顯示倒數計時。

---

## 🔧 開發過程遇到的問題

**Python Embeddable 無法執行標準函式庫**  
Embeddable Python 預設不載入 `site` 模組，需要手動編輯 `python3xx._pth` 檔案，將 `#import site` 的註解符號移除。

**Windows 安全性封鎖**  
從網路下載的執行檔會被 Windows 標記為不受信任，需要在檔案內容中手動「解除封鎖」才能正常執行。

**架構決策：為什麼用 Python 伺服器而非純瀏覽器？**  
瀏覽器基於安全性無法直接讀寫本機資料夾，因此批次翻譯需要一個本地伺服器作為中介，負責資料夾掃描與檔案寫入。Python 標準函式庫的 `http.server` 模組不需要任何額外安裝，是最輕量的選擇。

---

## 學習心得

這個版本讓我理解了：
- 前後端分離的基本概念（HTML 做介面，Python 做檔案操作）
- 為什麼瀏覽器不能直接存取本機資料夾（安全沙箱）
- Python Embeddable 與一般安裝版的差異
- 如何用 Prompt 工程改善 LLM 的輸出品質

---

# v2 - Feature Expansion

> v2 was driven by real usage experience after v1 proved stable.  
> Key goals: fix known bugs, add batch processing capability, and make the tool viable for long translation sessions.

---

## What Changed from v1

| Feature | v1 | v2 |
|---------|----|----|
| LLM junk prefix in output | ❌ Appears | ✅ Auto-filtered |
| Batch translation | ❌ None | ✅ Full folder at once |
| Language selector | ❌ Fixed JP→ZH | ✅ Freely configurable |
| Prompt editing | ❌ Not editable | ✅ Editable with reset button |
| Cooling mode | ❌ None | ✅ Configurable work/rest cycle |
| Python environment | — | ✅ Embeddable, portable, zero-install |

---

## File Overview

```
v2/
├── novel-translator-v2-0808.html   # Main app, open in browser
├── server.py                        # Local server for batch translation
├── 啟動伺服器.bat                   # Double-click to start server.py
└── README.md                        # This file
```

---

## How to Use

### Single File Translation
1. Make sure LM Studio Local Server is running
2. Open `novel-translator-v2-0808.html` in a browser
3. Click ⚙ to configure API URL and model name
4. Select languages, paste text or load a `.txt` file
5. Click "Start Translation"

### Batch Translation (requires Python)

**Option A: Python already installed on system**  
Double-click `啟動伺服器.bat`

**Option B: Python Embeddable (zero install)**
1. Download `Windows embeddable package (64-bit)` from [python.org](https://www.python.org/downloads/windows/)
2. Extract to `v2/python-embed/`
3. Double-click `啟動伺服器.bat`

Once the server is running, switch to the "Batch Translation" tab and enter the source folder path.

---

## Development Notes

**Python Embeddable stdlib not loading**  
The embeddable package doesn't load the `site` module by default. Had to edit `python3xx._pth` to uncomment `import site`.

**Windows security block**  
Files downloaded from the internet are flagged by Windows SmartScreen. Required manually unchecking the security block in file properties before execution.

**Why a Python server instead of pure browser?**  
Browsers cannot access the local filesystem for security reasons. A lightweight local server using Python's built-in `http.server` handles folder scanning and file writing — no pip installs required.
