from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase

from settings import Settings

#settings to access env 
settings = Settings()

# Create engine (Connection pool)
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

# Create session factory for creating and closing a session on each request
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
