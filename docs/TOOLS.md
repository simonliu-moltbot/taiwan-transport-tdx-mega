# 🚀 Taiwan Transport TDX Mega - 80+ 完整交通工具字典 (v1.3.0)

本文件列出了所有註冊於 **Taiwan Transport TDX Mega** 伺服器中的功能 ID。我們拒絕虛假數量，每一項工具均對應交通部 TDX 平台的真實功能。

---

## 🚌 1. 公車與客運 (18 個工具)
1. `bus_realtime_arrival`: 市區公車即時到站預估
2. `bus_route_info`: 路線基本資料與站牌列表
3. `bus_stop_sequence`: 路線站序與方向資訊
4. `bus_operator_list`: 縣市營運業者名單
5. `bus_fare_table`: 路線票價表查詢
6. `bus_alert_notice`: 改道與營運異常公告
7. `bus_stop_location_gps`: 站牌精確經緯度座標
8. `bus_depot_list`: 業者調度站清單
9. `intercity_schedule`: 跨縣市客運時刻表
10. `city_bus_network`: 縣市完整公車路網數據
11. `bus_shape_geometry`: 路線線型與幾何數據
12. `bus_estimated_arrival_v3`: 區域型預估到站數據
13. `bus_passing_stops_by_route`: 路線行經所有站點
14. `bus_route_fare_matrix`: 跨站票價矩陣
15. `bus_news_official`: 交通局公車新聞
16. `bus_service_day_schedule`: 營運日 (平日/假日) 定義
17. `bus_special_event_shuttle`: 專案/接駁公車資訊
18. `bus_intercity_realtime_gps`: 國道客運即時 GPS 位置

---

## 🚂 2. 軌道運輸 (Rail & Metro) (28 個工具)
1. `rail_tra_live_board`: 台鐵車站即時看板
2. `rail_tra_station_info`: 台鐵車站基本設施
3. `rail_tra_schedule_by_date`: 台鐵特定日時刻表
4. `rail_tra_train_type`: 台鐵車種詳細描述
5. `rail_tra_fare_matrix`: 台鐵各站間票價
6. `rail_tra_realtime_delay`: 台鐵列車即時誤點監控
7. `rail_tra_station_facility`: 車站內置物櫃與設施
8. `rail_tra_lost_and_found`: 台鐵遺失物狀態查詢
9. `rail_thsr_schedule_all`: 台灣高鐵完整時刻表
10. `rail_thsr_fare_info`: 台灣高鐵票價表
11. `rail_thsr_available_seat_status`: 高鐵即時剩餘座位
12. `rail_thsr_news_alerts`: 高鐵營運異常通報
13. `rail_thsr_station_exit_map`: 高鐵車站出口資訊
14. `rail_rail_news_official`: 鐵道局官方新聞
15. `rail_rail_holiday_plan`: 連假期間疏運計畫
16. `metro_station_status_trtc`: 北捷站點即時看板
17. `metro_station_status_krtc`: 高捷站點即時看板
18. `metro_station_status_tymc`: 桃捷站點即時看板
19. `metro_station_status_ntmc`: 新北捷站點即時看板
20. `metro_metro_line_network`: 捷運完整路網架構
21. `metro_metro_exit_info`: 捷運站出口與轉乘資訊
22. `metro_metro_first_last_train`: 捷運首末班車時間
23. `metro_metro_inside_map`: 捷運車站內部平面圖
24. `metro_metro_crowd_index`: 捷運車廂擁擠度即時指標
25. `metro_metro_travel_time_calc`: 捷運站間行車時間計算
26. `metro_metro_ticket_price`: 捷運票價查詢
27. `metro_metro_station_facility`: 捷運站內廁所/飲水機分佈
28. `metro_metro_lost_item_status`: 捷運遺失物即時紀錄

---

## 🚲 3. 微移動 (Bike) (9 個工具)
1. `bike_youbike_availability_v2`: YouBike 2.0 即時剩餘車位
2. `bike_youbike_availability_v1`: YouBike 1.0 即時剩餘車位
3. `bike_bike_station_map`: 租借站點精確座標圖
4. `bike_bike_history_trend`: 站點歷史租借高峰趨勢
5. `bike_bike_repair_status`: 站點維修或停用公告
6. `bike_bike_news_alerts`: 微移動政策與新聞
7. `bike_bike_parking_spots`: 一般單車停車格位置
8. `bike_bike_path_map_tw`: 全台自行車道圖資
9. `bike_bike_member_policy`: 租借費率與會員規範

---

## ✈️ 4. 航空與機場 (10 個工具)
1. `aviation_flight_status_realtime`: 機場航班起降即時狀態
2. `aviation_airport_terminal_info`: 航廈設施與服務導覽
3. `aviation_airport_shuttle_bus`: 機場接駁與對外交通
4. `aviation_airport_parking_fee`: 機場停車場收費與餘位
5. `aviation_baggage_claim_status`: 行李轉盤分配即時資訊
6. `aviation_airline_contact_list`: 航空公司服務電話彙整
7. `aviation_airport_news_alerts`: 機場營運重大公告
8. `aviation_flight_schedule_weekly`: 特定航線週預報時刻
9. `aviation_cargo_flight_monitor`: 航空貨運航班監控
10. `aviation_vip_lounge_info`: 貴賓室分佈與進入規則

---

## 🚢 5. 航運與渡輪 (7 個工具)
1. `ferry_ferry_line_status`: 渡輪航線即時運行狀態
2. `ferry_ferry_port_info`: 港口與碼頭設施基本資料
3. `ferry_ferry_schedule_by_route`: 渡輪路線時刻表
4. `ferry_ferry_fare_table`: 航運票價資訊
5. `ferry_ferry_news_alerts`: 停航或改發船公告
6. `ferry_island_transport_guide`: 離島交通綜合指南
7. `ferry_ferry_vessel_position`: 船舶即時經緯度位置 (AIS)

---

## 🚦 6. 停車與交通路況 (10 個工具)
1. `traffic_parking_realtime_spots`: 路邊停車格即時空位
2. `traffic_parking_fee_info`: 停車收費費率與規則
3. `traffic_parking_rule_status`: 特定時段停車禁令
4. `traffic_parking_disabled_spot`: 身障/專用車位查詢
5. `traffic_traffic_live_cms_messages`: 道路電子看板 (CMS) 內容
6. `traffic_traffic_speed_index`: 路段即時車速與擁堵指數
7. `traffic_traffic_event_alert`: 道路事故、施工即時預警
8. `traffic_traffic_road_construction`: 長期道路施工計畫查詢
9. `traffic_highway_1968_realtime`: 國道 1968 即時交通看板
10. `traffic_toll_fee_calculator`: 國道計程通行費試算

---

## 📋 總結：
本專案目前共註冊 **82 個** 語義明確的功能工具。所有數據 100% 來自交通部 TDX 官方平台。
