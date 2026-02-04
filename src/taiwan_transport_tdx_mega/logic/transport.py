from typing import Dict, Any, List, Optional
from ..config import Config
from ..utils.http_client import AsyncHttpClient

class TransportLogic:
    """
    Core business logic for interacting with Taiwan's TDX transport data (MOTC).
    All methods fetch REAL data from official endpoints.
    """

    @staticmethod
    async def get_bus_estimated_time(city: str, route_name: str) -> List[Dict[str, Any]]:
        """獲取特定縣市公車預估到站時間。"""
        url = f"{Config.TDX_BASE_URL}/Bus/EstimatedTimeOfArrival/City/{city}/{route_name}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_tra_live_board(station_id: str) -> List[Dict[str, Any]]:
        """獲取台鐵車站即時列車看板。"""
        url = f"{Config.TDX_BASE_URL}/Rail/TRA/LiveBoard/Station/{station_id}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_metro_live_board(system: str = "TRTC") -> List[Dict[str, Any]]:
        """獲取捷運系統即時看板。"""
        url = f"{Config.TDX_BASE_URL}/Rail/Metro/LiveBoard/{system}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_bike_availability(city: str) -> List[Dict[str, Any]]:
        """獲取 YouBike 2.0 即時位。"""
        url = f"{Config.TDX_BASE_URL}/Bike/Availability/City/{city}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_flight_status(airport_id: str) -> List[Dict[str, Any]]:
        """獲取機場即時航班起降狀態。機場代碼如: TPE, TSA。"""
        url = f"{Config.TDX_BASE_URL}/Air/RealTimeStatus/Airport/{airport_id}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_ferry_status() -> List[Dict[str, Any]]:
        """獲取全台航運渡輪即時狀態。"""
        url = f"{Config.TDX_BASE_URL}/Ship/RealTimeStatus"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_parking_spots(city: str) -> List[Dict[str, Any]]:
        """獲取全台路邊停車位即時資訊。"""
        url = f"{Config.TDX_BASE_URL}/Parking/OffStreet/CarPark/Availability/City/{city}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_highway_live_cms() -> List[Dict[str, Any]]:
        """獲取國道電子看板即時資訊。"""
        url = f"{Config.TDX_BASE_URL}/Traffic/CMS/RealTime"
        return await AsyncHttpClient.fetch_json(url)
