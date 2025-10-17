from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()  

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./taskmanager.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")

settings = Settings()
