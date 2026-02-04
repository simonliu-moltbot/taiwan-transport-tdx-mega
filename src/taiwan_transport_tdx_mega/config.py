import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # TDX API Config (MOTC)
    TDX_BASE_URL = "https://tdx.transportdata.tw/api/basic/v2"
    
    # Auth (Note: TDX requires Client ID/Secret for production, 
    # but some datasets allow limited public access)
    TDX_CLIENT_ID = os.getenv("TDX_CLIENT_ID", "")
    TDX_CLIENT_SECRET = os.getenv("TDX_CLIENT_SECRET", "")
    
    # Server Settings
    APP_NAME = "taiwan-transport-tdx-mega"
    VERSION = "1.0.0"
    DEFAULT_HTTP_PORT = 8001
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
