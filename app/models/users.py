from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum as SQLEnum, bool, DateTime
from datetime import datetime, timedelta
from enum import Enum
from app.config.dbConfig import Base

#now
now = datetime.utcnow()

plus_hour = now + timedelta(hours=1)

# user role class
class UserRole(str, Enum):
    ADMIN:"admin"
    USER:"user"

#user class
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str] = mapped_column(String, required=True)
    email:Mapped[str] = mapped_column(String, unique=True, required=True, index=True)
    hashed_password:Mapped[str] = mapped_column(String, required=True)
    role:Mapped[UserRole] = mapped_column(SQLEnum , nullable=False, default=UserRole.USER)
    verified:Mapped[bool] = mapped_column(bool, default=False)
    verifiedToken:Mapped[str] = mapped_column(String, required=True)
    verifiedTokenExpiry:Mapped[datetime] = mapped_column(DateTime, default = lambda: plus_hour)
    passwordToken:Mapped[str] = mapped_column(String, required=True)
    passwordTokenExpiry:Mapped[datetime] = mapped_column(DateTime, default = lambda: plus_hour)

    
    

