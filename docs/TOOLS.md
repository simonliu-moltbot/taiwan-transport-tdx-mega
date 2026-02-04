# 🚀 Taiwan Transport TDX Mega - 工具手冊 (v1.2.0)

本文件列出了 **Taiwan Transport TDX Mega** 的所有具備語義化名稱的功能 ID。我們已棄用模糊的索引命名，確保 AI 與人類都能輕鬆辨識功能。

---

## 🚌 1. 公車與客運 (Bus)
*   `bus_realtime_arrival`: 全台縣市公車即時到站時間。
*   `bus_route_info`: 查詢路線站牌、站序與營運業者。
*   `bus_operator_list`: 查詢各縣市客運業者名單。
*   `bus_stop_location`: 站牌精確經緯度與周邊查詢。
*   `bus_fare_table`: 查詢路線票價矩陣。
*   `bus_alert_notice`: 獲取路線改道或減班公告。

## 🚂 2. 軌道運輸 (Rail & Metro)
*   `rail_tra_live_board`: 台鐵車站電子看板 (即時誤點資訊)。
*   `rail_thsr_schedule`: 台灣高鐵時刻表與剩餘座位查詢。
*   `rail_train_type_info`: 台鐵車種 (自強、莒光) 詳細資訊。
*   `rail_fare_matrix`: 台鐵各站間票價試算。
*   `metro_station_status`: 捷運站點即時動態 (北捷、高捷、中捷、桃捷)。
*   `metro_line_network_map`: 捷運路網與轉乘站資訊。
*   `metro_first_last_train`: 各站首末班車時間。

## 🚲 3. 微移動與生活 (Bike & Parking)
*   `bike_youbike_availability`: YouBike 2.0 即時車位與空位數。
*   `bike_station_map`: 查詢租借站詳細地理位置。
*   `parking_realtime_spots`: 全台路邊與停車場即時剩餘位。
*   `bike_repair_status`: YouBike 站點維修或暫停營運公告。

## ✈️ 4. 航空與航運 (Aviation & Ferry)
*   `aviation_flight_status`: 全台機場航班起降即時狀態。
*   `aviation_terminal_service`: 航廈設施與接駁車資訊。
*   `ferry_line_status`: 全台渡輪航線 (離島、藍色公路) 運行狀態。

---

## 🛡️ 命名規範
本專案遵循 `[運輸種類]_[具體功能]` 的命名邏輯，例如：
*   `rail_tra_live_board` -> **鐵路 (Rail)** 下的 **台鐵 (TRA)** 的 **即時看板 (Live Board)**。
*   `bus_realtime_arrival` -> **公車 (Bus)** 的 **即時到站 (Realtime Arrival)**。
