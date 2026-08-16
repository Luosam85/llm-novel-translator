# LLM Novel Translator｜本地 LLM 小說翻譯器

> 這是我練習使用 Claude 進行 AI 協作開發的學習專案。  
> 從需求討論、UI 設計、除錯到部署，全程透過與 Claude 對話完成。

---

## 📖 專案簡介

一款運行在瀏覽器的日文小說翻譯工具，對接本地 LM Studio 運行的 LLM 模型，不需要雲端 API、不消耗付費額度，完全在自己的電腦上翻譯。

### 為什麼做這個？

我本身的背景是 CNC 加工與 CAM 程式設計，並非軟體工程師。這個專案的目標是透過實際需求驅動學習，練習：

- 與 AI 進行需求溝通與規劃
- 理解前端（HTML/JS）與後端（Python）的基本架構
- 學習如何除錯與迭代改版
- 練習使用 GitHub 管理版本

---

## 🗂️ 版本紀錄

### v1 - 穩定初版
- 單檔翻譯（貼上或載入 .txt）
- 串流輸出（字一個一個出現）
- 設定面板：API 網址、模型名稱、每段字數、翻譯風格
- 對接 LM Studio 本地 API

### v2 - 功能擴充版
- ✅ 修正 LLM 回應出現廢話前言的 Bug
- ✅ 新增批次翻譯（整個資料夾一次翻完）
- ✅ 新增原文／目標語言選擇
- ✅ 新增降速冷卻機制（保護 GPU）
- ✅ Prompt 可外部編輯，附重設按鈕
- ✅ Python Embeddable 可攜式環境（零安裝）

---

## 🛠️ 使用技術

| 項目 | 技術 |
|------|------|
| 前端介面 | HTML + Vanilla JavaScript |
| 本地伺服器 | Python 3（標準函式庫，零套件安裝）|
| LLM 對接 | LM Studio OpenAI-compatible API |
| 版本管理 | GitHub |

---

## 📁 專案結構

```
llm-novel-translator/
├── v1/    # 初版，單一 HTML 檔案即可運行
└── v2/    # 擴充版，需搭配 server.py 使用批次功能
```

---

## 🔗 開發工具

- **LM Studio** - 本地 LLM 運行環境
- **Claude (Anthropic)** - AI 協作開發夥伴
- **Python Embeddable Package** - 可攜式 Python 環境

---

*這個 README 和所有程式碼都是在與 Claude 的對話過程中逐步產出的。  
學習重點不只是程式本身，而是如何把需求清楚表達給 AI，並審核、迭代結果。*

---

# LLM Novel Translator

> A learning project where I practice AI-assisted development using Claude.  
> From requirements discussion, UI design, debugging to deployment — all done through conversation with Claude.

---

## About This Project

A browser-based Japanese novel translation tool that connects to a locally running LLM via LM Studio. No cloud API, no paid quota — everything runs on your own machine.

### Why Build This?

My background is in CNC machining and CAM programming, not software engineering. This project is driven by a real personal need, and serves as a learning exercise in:

- Communicating requirements clearly to an AI
- Understanding basic frontend (HTML/JS) and backend (Python) architecture
- Debugging and iterating across versions
- Using GitHub for version control

---

## Version History

### v1 - Stable Initial Release
- Single-file translation (paste or load .txt)
- Streaming output
- Settings panel: API URL, model name, chunk size, translation style
- Connects to LM Studio local API

### v2 - Feature Expansion
- ✅ Fixed LLM response junk-prefix bug
- ✅ Batch translation (entire folder at once)
- ✅ Source / target language selector
- ✅ Cooling mode to protect GPU during long sessions
- ✅ Editable prompt with one-click reset to default
- ✅ Portable Python Embeddable environment (zero install)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML + Vanilla JavaScript |
| Local Server | Python 3 (stdlib only, no pip install needed) |
| LLM Integration | LM Studio OpenAI-compatible API |
| Version Control | GitHub |

---

*All code and documentation in this repository were produced collaboratively with Claude.  
The learning focus is not just the code itself, but how to clearly express requirements to an AI and review, iterate on the results.*
