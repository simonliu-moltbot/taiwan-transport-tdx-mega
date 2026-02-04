import httpx
import logging
from typing import Dict, Any, Optional
from ..config import Config

logging.basicConfig(level=Config.LOG_LEVEL)
logger = logging.getLogger(Config.APP_NAME)

class AsyncHttpClient:
    """
    Standardized Async HTTP Client for TDX API interactions.
    Provides robust error handling and logging.
    """
    _client: Optional[httpx.AsyncClient] = None

    @classmethod
    async def get_client(cls) -> httpx.AsyncClient:
        """Returns a singleton AsyncClient instance."""
        if cls._client is None or cls._client.is_closed:
            cls._client = httpx.AsyncClient(timeout=15.0, follow_redirects=True)
        return cls._client

    @classmethod
    async def fetch_json(cls, url: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Executes a GET request and returns the parsed JSON.
        
        Args:
            url (str): The target endpoint.
            params (Optional[Dict]): Query parameters.
            
        Returns:
            Dict[str, Any]: JSON response or error object.
        """
        client = await cls.get_client()
        try:
            logger.debug(f"Requesting TDX: {url}")
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"TDX API failure: {url} - {str(e)}")
            return {"error": f"TDX_API_ERROR: {str(e)}"}

    @classmethod
    async def close(cls):
        """Closes the underlying client connection."""
        if cls._client:
            await cls._client.aclose()
