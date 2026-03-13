from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
from datetime import timedelta
from pathlib import Path

class Settings(BaseSettings):
    DB_URL: str
    SECRET_KEY: str = "your-secret-key-change-this-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_file=str(Path(__file__).parent.parent.parent / ".env"))

settings = Settings()

