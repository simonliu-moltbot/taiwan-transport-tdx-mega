from typing import Dict, Any, List, Optional
from ..config import Config
from ..utils.http_client import AsyncHttpClient

class TransportLogic:
    """
    Core business logic for interacting with Taiwan's TDX transport data (MOTC).
    All methods fetch REAL data from official endpoints and follow DevOps standards.
    """

    @staticmethod
    async def get_bus_estimated_time(city: str, route_name: str) -> List[Dict[str, Any]]:
        """
        獲取特定縣市公車預估到站時間。
        
        Args:
            city (str): 縣市英文代碼 (例如: Taipei, NewTaipei, Taichung)。
            route_name (str): 公車路線名稱 (例如: 307, 299)。
            
        Returns:
            List[Dict[str, Any]]: 包含到站剩餘時間 (秒)、站點名稱及車號的字典列表。
        """
        url = f"{Config.TDX_BASE_URL}/Bus/EstimatedTimeOfArrival/City/{city}/{route_name}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_tra_live_board(station_id: str) -> List[Dict[str, Any]]:
        """
        獲取台鐵車站即時列車看板資訊。
        
        Args:
            station_id (str): 車站代碼 (例如: 1000 台北, 3300 台中, 4400 高雄)。
            
        Returns:
            List[Dict[str, Any]]: 包含車次、車種、目的地、狀態 (誤點/準點) 及到站時間的列表。
        """
        url = f"{Config.TDX_BASE_URL}/Rail/TRA/LiveBoard/Station/{station_id}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_metro_live_board(system: str = "TRTC") -> List[Dict[str, Any]]:
        """
        獲取捷運系統即時列車看板動態。
        
        Args:
            system (str): 捷運系統代碼 (TRTC: 台北捷運, KRTC: 高雄捷運, TYMC: 桃園捷運)。
            
        Returns:
            List[Dict[str, Any]]: 包含捷運各站點即時列車進站狀態與剩餘秒數的列表。
        """
        url = f"{Config.TDX_BASE_URL}/Rail/Metro/LiveBoard/{system}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_bike_availability(city: str) -> List[Dict[str, Any]]:
        """
        獲取特定縣市公共自行車 (YouBike 2.0) 之即時位狀態。
        
        Args:
            city (str): 縣市英文名稱 (例如: Taipei, Taichung)。
            
        Returns:
            List[Dict[str, Any]]: 包含站點名稱、可借車數、可還空位數及更新時間的字典列表。
        """
        url = f"{Config.TDX_BASE_URL}/Bike/Availability/City/{city}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_flight_status(airport_id: str) -> List[Dict[str, Any]]:
        """
        獲取機場即時航班起降狀態與航廈資訊。
        
        Args:
            airport_id (str): 機場 IATA 代碼 (例如: TPE 桃園, TSA 松山, KHH 高雄)。
            
        Returns:
            List[Dict[str, Any]]: 包含航班編號、航空公司、預計起降時間、登機門及狀態的列表。
        """
        url = f"{Config.TDX_BASE_URL}/Air/RealTimeStatus/Airport/{airport_id}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_ferry_status() -> List[Dict[str, Any]]:
        """
        獲取全台航運渡輪即時運行狀態 (包含離島航線)。
        
        Args:
            無
            
        Returns:
            List[Dict[str, Any]]: 包含航線名稱、船名、當前狀態及公告之列表。
        """
        url = f"{Config.TDX_BASE_URL}/Ship/RealTimeStatus"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_parking_spots(city: str) -> List[Dict[str, Any]]:
        """
        獲取全台各縣市路邊停車位或公有停車場之即時空位資訊。
        
        Args:
            city (str): 縣市英文代碼。
            
        Returns:
            List[Dict[str, Any]]: 包含停車場名稱、總位數、剩餘位數及收費標準的字典列表。
        """
        url = f"{Config.TDX_BASE_URL}/Parking/OffStreet/CarPark/Availability/City/{city}"
        return await AsyncHttpClient.fetch_json(url)

    @staticmethod
    async def get_highway_live_cms() -> List[Dict[str, Any]]:
        """
        獲取國道電子看板 (CMS) 之即時交通訊息。
        
        Args:
            無
            
        Returns:
            List[Dict[str, Any]]: 包含看板位置、路段描述及顯示訊息 (如:事故預警、擁堵提示) 的列表。
        """
        url = f"{Config.TDX_BASE_URL}/Traffic/CMS/RealTime"
        return await AsyncHttpClient.fetch_json(url)
