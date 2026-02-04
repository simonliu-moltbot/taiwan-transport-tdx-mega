# 🚀 Taiwan Transport TDX Mega (台灣交通大聯盟)

這是一個基於 **Model Context Protocol (MCP)** 的重裝級交通數據伺服器，直接串接 **交通部 TDX (Transport Data eXchange) 平台**。

## 🏗️ 專案特色
- **100% 官方數據**：嚴格遵守合規性，不使用爬蟲，資料皆來自交通部官方 API。
- **DevOps 規格**：模組化邏輯架構，內建 Dockerfile 與 Makefile。
- **全方位覆蓋**：包含公車、台鐵、高鐵、捷運、自行車、航空與渡輪數據。
- **Streamable HTTP**：支援 FastMCP 串流模式，可遠端呼叫。

## 📂 工具分類 (70+ Tools)
1. **公車動態 (Bus)**：全台各縣市即時到站預估、路線查詢。
2. **軌道運輸 (Rail)**：台鐵即時看板、高鐵時刻表、捷運站點狀態。
3. **微移動 (Bike)**：YouBike 2.0 即時車位與站點資訊。
4. **航空與渡輪 (Aviation & Ferry)**：航班起降狀態、航運即時動態。
5. **生活機能 (Living)**：全台路邊/停車場即時剩餘車位查詢。

## 🛠 Dive Configuration
- **Type**: `stdio`
- **Command**: `python`
- **Args**: `src/taiwan_transport_tdx_mega/server.py`

## 🛡️ 數據來源聲明
數據源：[交通部 TDX 運輸資料流通服務](https://tdx.transportdata.tw/)。
請確保在使用進階功能時，於 `.env` 中設定您的 `TDX_CLIENT_ID` 與 `TDX_CLIENT_SECRET`。
