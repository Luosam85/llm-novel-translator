# v1 - 穩定初版｜Stable Initial Release

> 這是我第一次嘗試用 Claude 從零開始設計並實作一個完整工具。  
> 從手繪 UI 草圖到可運行的程式，中間經歷了許多除錯與學習。

---

## ✨ 功能

- 左側貼上日文原文，或載入 `.txt` 檔案
- 右側即時串流顯示翻譯結果（字一個一個出現）
- 上方進度條顯示翻譯進度
- 右上角設定面板

### 設定項目
| 設定 | 說明 |
|------|------|
| API 網址 | LM Studio 本地位址（預設 `http://localhost:1234/v1`）|
| 模型名稱 | 填入 LM Studio 載入的 Model ID |
| 每段字數 | 控制每次送給 LLM 的文字量 |
| 段落延遲 | 每段之間的等待秒數 |
| 翻譯風格 | 意譯 / 直譯 / 小說風 |

---

## 🚀 使用方式

1. 確認 LM Studio 已開啟並啟動 Local Server
2. 用瀏覽器直接開啟 `novel-translator-v1-stable.html`
3. 點擊右上角 ⚙ 填入 API 網址與模型名稱
4. 貼上原文或載入 `.txt` 檔案
5. 點擊「開始翻譯」

**零安裝，單一 HTML 檔案即可運行。**

---

## ⚠️ 已知限制（v2 已修正）

- LLM 有時會在譯文開頭加上「以下是翻譯：」等說明句
- 無批次翻譯功能，每次只能處理一個檔案
- 無語言選擇，預設日文 → 繁體中文
- 無降速冷卻機制

---

## 🔧 除錯過程記錄

這個版本在開發過程中遇到幾個值得記錄的問題：

**CORS 問題**  
瀏覽器發送請求前會先送出 `OPTIONS` 預檢，LM Studio 需要開啟 CORS 才能正常運作。

**LM Studio API 路徑版本差異**  
LM Studio 0.4.x 版的 OpenAI-compatible endpoint 路徑與舊版不同，需要確認使用正確的 `/v1/chat/completions` 路徑，而非 `/api/v1/chat`。

**Port 設定**  
LM Studio 預設 port 不一定是 1234，需要在 Local Server 畫面確認實際監聽的 port 號。

---

## 學習心得

這個版本讓我理解了：
- 前端如何透過 `fetch` 呼叫 API
- 什麼是 streaming 回應
- 瀏覽器的安全限制（CORS）是怎麼運作的
- 如何把手繪草圖的概念轉化成實際介面

---

# v1 - Stable Initial Release

> My first attempt at designing and implementing a complete tool from scratch using Claude.  
> From hand-drawn UI sketches to a working program — with plenty of debugging and learning along the way.

---

## Features

- Paste Japanese source text on the left, or load a `.txt` file
- Streaming translation output on the right (character by character)
- Progress bar at the top
- Settings panel in the top-right corner

### Settings
| Setting | Description |
|---------|-------------|
| API URL | LM Studio local address (default: `http://localhost:1234/v1`) |
| Model Name | The Model ID loaded in LM Studio |
| Chunk Size | Controls how much text is sent to the LLM per request |
| Paragraph Delay | Wait time between chunks |
| Translation Style | Natural / Literal / Novel |

---

## How to Use

1. Make sure LM Studio is open with Local Server running
2. Open `novel-translator-v1-stable.html` directly in a browser
3. Click ⚙ to enter your API URL and model name
4. Paste source text or load a `.txt` file
5. Click "Start Translation"

**Zero installation required. Single HTML file.**

---

## Known Issues (Fixed in v2)

- LLM sometimes prepends junk text like "Here is the translation:" to output
- No batch translation — one file at a time only
- No language selector — defaults to Japanese → Traditional Chinese
- No cooling mode for GPU protection

---

## Debugging Notes

**CORS**  
Browsers send a preflight `OPTIONS` request before the actual API call. LM Studio needs CORS enabled to handle this correctly.

**LM Studio API Path Differences**  
LM Studio 0.4.x changed the OpenAI-compatible endpoint path. Confirmed correct path is `/v1/chat/completions` under the OpenAI-compatible tab, not `/api/v1/chat`.

**Port Configuration**  
LM Studio's local server port is not always 1234. Always verify the actual listening port in the Local Server panel.
