# 🚀 Taiwan Transport TDX Mega (台灣交通大聯盟) v1.1.0

這是一個基於 **Model Context Protocol (MCP)** 的旗艦級交通數據伺服器，採用與「金融大聯盟」同級的 **DevOps 模組化架構**。本專案 100% 串接 **交通部 TDX (Transport Data eXchange)** 平台數據。

## 🏗️ 旗艦級架構特點
- **模組化分層**：核心邏輯 (`logic/`)、通訊組件 (`utils/`)、設定中心 (`config.py`) 徹底分離。
- **Streamable HTTP**：基於 FastMCP，支援遠端串流呼叫與 Cherry Studio 對接。
- **完整文件化**：內建詳細的 Function Docstrings 與 I/O 說明。
- **自動化運維**：內建 `Makefile`、`Dockerfile` 與 `requirements.txt`。

## 📂 工具完整手冊 (70+ 個工具)
詳細的功能 ID 與參數說明，請參閱：
👉 [**docs/TOOLS.md**](./docs/TOOLS.md)

---

## 🛠 Dive Configuration

在 **Dive** 或 AI 客戶端中新增此 Server：

- **Type**: `stdio`
- **Command**: `python`
- **Args**: `src/taiwan_transport_tdx_mega/server.py`

## 🛡️ 數據來源說明
本專案嚴格遵守 **交通部運輸資料流通服務 (TDX)** 使用規範。
請在 `.env` 中填寫您的憑證以確保高頻訪問：
```env
TDX_CLIENT_ID=你的_ID
TDX_CLIENT_SECRET=你的_SECRET
```
