from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    port:int
    DATABASE_URL:str
    MAILERSEND_API_KEY:str
    MAIL_FROM_EMAIL:str
    MAIL_FROM_NAME:str
    FRONTEND_VERIFY_URL:str
    env:str
    SECRET_KEY:str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"

settings = Settings()