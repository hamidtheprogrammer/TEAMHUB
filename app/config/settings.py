from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port:int

    class Config:
        env_file = ".env"

settings = Settings()