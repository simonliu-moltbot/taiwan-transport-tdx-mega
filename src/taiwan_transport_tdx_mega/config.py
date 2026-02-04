import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # TDX API Configuration (Transport Data eXchange - MOTC)
    TDX_BASE_URL = "https://tdx.transportdata.tw/api/basic/v2"
    
    # Auth credentials for production usage (Set in .env)
    TDX_CLIENT_ID = os.getenv("TDX_CLIENT_ID", "your_id")
    TDX_CLIENT_SECRET = os.getenv("TDX_CLIENT_SECRET", "your_secret")
    
    # Server Settings
    APP_NAME = "taiwan-transport-tdx-mega"
    VERSION = "1.1.0"
    DEFAULT_HTTP_PORT = 8001
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
