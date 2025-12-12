from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # 🌍 Project Identity
    PROJECT_ID: str = "metodo-activa-cerebro"
    LOCATION: str = "us-central1"
    
    # 🔐 Security
    # 🔐 Security
    ALLOWED_ORIGINS: list = [
        "https://project-c465bc45-299b-470d-8b6.web.app", 
        "https://metodo-activa.web.app", 
        "http://localhost:5173"
    ]
    
    # 🧠 AI Config
    VERTEX_REGION: str = "us-central1"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
