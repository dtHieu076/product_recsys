from pydantic_settings import BaseSettings
from typing import Optional
from datetime import timedelta

class Settings(BaseSettings):
    DB_URL: str
    SECRET_KEY: str = "your-secret-key-change-this-super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = "../.env"

settings = Settings()

