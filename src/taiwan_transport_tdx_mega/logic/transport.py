from ..config import Config
from ..utils.http_client import AsyncHttpClient

class BusLogic:
    @staticmethod
    async def get_realtime_bus_arrival(city: str, route_name: str):
        """查詢特定縣市路線的即時到站預估。"""
        # Endpoint: /Bus/EstimatedTimeOfArrival/City/{City}/{RouteName}
        url = f"{Config.TDX_BASE_URL}/Bus/EstimatedTimeOfArrival/City/{city}/{route_name}"
        return await AsyncHttpClient.fetch_json(url)

class RailLogic:
    @staticmethod
    async def get_train_live_board(station_id: str):
        """查詢台鐵特定車站的即時列車看板 (動態看板)。"""
        # Endpoint: /Rail/TRA/LiveBoard/Station/{StationID}
        url = f"{Config.TDX_BASE_URL}/Rail/TRA/LiveBoard/Station/{station_id}"
        return await AsyncHttpClient.fetch_json(url)

class MetroLogic:
    @staticmethod
    async def get_metro_station_status(system: str = "TRTC"):
        """查詢捷運系統 (台北/高雄/桃園) 站點狀態。系統代碼: TRTC, KRTC, TYMC。"""
        url = f"{Config.TDX_BASE_URL}/Rail/Metro/LiveBoard/{system}"
        return await AsyncHttpClient.fetch_json(url)
