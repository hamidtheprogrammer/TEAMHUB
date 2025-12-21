from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port:int
    DATABASE_URL:str

    class Config:
        env_file = ".env"

settings = Settings()