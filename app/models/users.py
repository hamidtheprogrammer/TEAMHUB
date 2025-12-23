from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum as SQLEnum, Boolean, DateTime
from datetime import datetime, timedelta
from enum import Enum
from app.config.dbConfig import Base

#function to return one hour from current time
def one_hour_from_now():
    now = datetime.utcnow()
    plus_hour = now + timedelta(hours=1)
    return plus_hour

# user role class
class UserRole(str, Enum):
    ADMIN:"admin"
    USER:"user"

#user class
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username:Mapped[str] = mapped_column(String, nullable=False)
    email:Mapped[str] = mapped_column(String, unique=True, nullable=False, index=True)
    hashed_password:Mapped[str] = mapped_column(String, nullable=False)
    role:Mapped[UserRole] = mapped_column(SQLEnum(UserRole) , nullable=False, default=UserRole.USER)
    verified:Mapped[bool] = mapped_column(Boolean, default=False)
    verifiedToken:Mapped[str] = mapped_column(String, nullable=False)
    verifiedTokenExpiry:Mapped[datetime] = mapped_column(DateTime, default = lambda: one_hour_from_now)
    passwordToken:Mapped[str] = mapped_column(String, nullable=False)
    passwordTokenExpiry:Mapped[datetime] = mapped_column(DateTime, default = lambda: one_hour_from_now)

    teams: Mapped[list["Team"]] = relationship(
        "Team",
        secondary="team_membership",
        back_populates="users"
    )

    
    

