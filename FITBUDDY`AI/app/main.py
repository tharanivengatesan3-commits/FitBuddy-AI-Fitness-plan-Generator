from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FitBuddy AI is running"}

class Settings(BaseSettings):
    app_name: str = "FitBuddy - AI Fitness Plan Generator"

    environment: str = "development"

    database_url: str = "sqlite:///./fitbuddy.db"

    gemini_api_key: str = ""

    # Keep model names configurable through .env
    gemini_workout_model: str = "gemini-3.1-pro-preview"
    gemini_tip_model: str = "gemini-3.8-flash"

    admin_token: str = "change-me"

    max_feedback_length: int = 1000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict

