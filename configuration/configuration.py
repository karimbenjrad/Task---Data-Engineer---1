from pydantic_settings import BaseSettings
from pydantic import Field
from os import getenv


class AppConfig(BaseSettings):
    APP_PORT: int = Field(env="APP_PORT", default="8000", description="port of the microservice")
    APP_HOST: str = Field(env="APP_HOST", default="0.0.0.0", description="host of the microservice")


class DataBaseConfig(BaseSettings):
    DB_NAME: str = Field(default="sales", description="Name of the database", env="DB_NAME")
    DB_USER: str = Field(default="root", description="User of the database", env="DB_USER")
    DB_PASSWORD: str = Field(default="root", description="Password of the database", env="DB_PASSWORD")
    DB_HOST: str = Field(default="0.0.0.0", description="Host of the database", env="DB_HOST")
    DB_PORT: int = Field(default=5432, description="Port of the database", env="DB_PORT")


class CsvConfig(BaseSettings):
    CSV_DATA_PATH: str = Field(default="./files/", description="Port of the database", env="DB_PORT")


class SettingsBlobStorage(BaseSettings):
    ACCOUNT_NAME: str = Field(default='devstoreaccount1', env='AccountName')
    ACCOUNT_KEY: str = Field(
        default="Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==",
        env='AccountKey')
    ACCOUNT_URL: str = Field(
        default='http://azurite:10000/devstoreaccount1',
        env='AccountURL')


setting_blob_storage = SettingsBlobStorage()
csv_config = CsvConfig()
data_base_config = DataBaseConfig()
app_config = AppConfig()
