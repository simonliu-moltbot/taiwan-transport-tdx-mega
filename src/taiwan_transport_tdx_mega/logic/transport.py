from typing import Dict, Any, List, Optional
from ..config import Config
from ..utils.http_client import AsyncHttpClient

class TransportLogic:
    """
    Core business logic for interacting with Taiwan's TDX transport data.
    """

    @staticmethod
    async def get_bus_estimated_time(city: str, route_name: str) -> List[Dict[str, Any]]:
        """
        獲取特定縣市公車路線之預估到站時間。
        
        Args:
            city (str): 縣市英文名稱 (例如 Taipei, Taichung)。
            route_name (str): 路線名稱。
            
        Returns:
            List[Dict[str, Any]]: 到站資訊列表。
        """
        url = f"{Config.TDX_BASE_URL}/Bus/EstimatedTimeOfArrival/City/{city}/{route_name}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_tra_live_board(station_id: str) -> List[Dict[str, Any]]:
        """
        獲取台鐵特定車站之即時列車看板資訊。
        
        Args:
            station_id (str): 車站代碼 (例如 1000)。
            
        Returns:
            List[Dict[str, Any]]: 列車看板數據。
        """
        url = f"{Config.TDX_BASE_URL}/Rail/TRA/LiveBoard/Station/{station_id}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_metro_live_board(system: str = "TRTC") -> List[Dict[str, Any]]:
        """
        獲取捷運系統即時列車看板動態。
        
        Args:
            system (str): 系統代碼 (TRTC, KRTC, TYMC)。
            
        Returns:
            List[Dict[str, Any]]: 捷運到站動態。
        """
        url = f"{Config.TDX_BASE_URL}/Rail/Metro/LiveBoard/{system}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_bike_availability(city: str) -> List[Dict[str, Any]]:
        """
        獲取特定縣市 YouBike 2.0 之即時車位狀態。
        
        Args:
            city (str): 縣市英文名稱。
            
        Returns:
            List[Dict[str, Any]]: 租借站位資訊。
        """
        url = f"{Config.TDX_BASE_URL}/Bike/Availability/City/{city}"
        return await AsyncHttpClient.fetch_json(url)
