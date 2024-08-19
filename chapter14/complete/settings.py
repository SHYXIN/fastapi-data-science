from pydantic import BaseSettings



class Settings(BaseSettings):
    database_url: str
    storage_endpoint: str
    storage_access_key: str
    storage_secret_key: str
    storage_bucket: str

    class Config:
        env_file = "chapter14/complete/.env"

settings = Settings()
