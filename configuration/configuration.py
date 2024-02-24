from pydantic_settings import BaseSettings
from pydantic import Field


class AppConfig(BaseSettings):
    APP_PORT: int = Field(env="APP_PORT", default="8000", description="port of the microservice")
    APP_HOST: str = Field(env="APP_HOST", default="0.0.0.0", description="host of the microservice")


class DataBaseConfig(BaseSettings):
    DB_NAME: str = Field(default="waves_user_profiling_db", description="Name of the database", env="DB_NAME")
    DB_USER: str = Field(default="root", description="User of the database", env="DB_USER")
    DB_PASSWORD: str = Field(default="root", description="Password of the database", env="DB_PASSWORD")
    DB_HOST: str = Field(default="0.0.0.0", description="Host of the database", env="DB_HOST")
    DB_PORT: int = Field(default=5432, description="Port of the database", env="DB_PORT")

data_base_config=DataBaseConfig()
app_config=AppConfig()
