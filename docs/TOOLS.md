# 🚀 Taiwan Transport TDX Mega - 工具手冊 (v1.1.0)

本文件詳列了所有對接 **交通部 TDX 平台** 的 70+ 個交通數據工具。

---

## 🚌 1. 公車與客運 (Bus)
*   `get_bus_arrival_prediction`: **[核心]** 全台各縣市公車到站預估。
    *   Input: `city` (英文名), `route` (路線名)。
*   `bus_expert_tool_01`~`20`: 包含路線站牌位置、業者營運概況、票價資訊等專屬查詢。

## 🚂 2. 軌道運輸 (Rail & Metro)
*   `get_tra_station_board`: **[核心]** 台鐵車站即時看板。
    *   Input: `station_id` (4碼代碼)。
*   `get_metro_status`: 捷運站點運行狀態 (TRTC, KRTC)。
*   `rail_expert_tool_01`~`15`: 包含高鐵時刻表查詢、台鐵列車時刻表、票價矩陣等。

## 🚲 3. 微移動 (Bike)
*   `get_youbike_availability`: **[核心]** YouBike 2.0 即時車位/空位查詢。
    *   Input: `city` (英文名)。
*   `bike_expert_tool_01`~`10`: 包含站點位置、歷史租借熱點趨勢、車型統計。

## ✈️ 4. 航空與物流 (Aviation & Logistics)
*   `aviation_expert_tool_01`~`10`: 全台機場航班起降狀態、航廈登機門狀態。
*   `parking_expert_tool_01`~`10`: 各縣市路邊停車格、公有停車場即時空位統計。

---

## 🛠 開發者指南 (DevOps)
*   **啟動方式**:
    *   STDIO: `make run-stdio`
    *   HTTP: `make run-http` (預設 Port 8001)
*   **測試**: `make test`
