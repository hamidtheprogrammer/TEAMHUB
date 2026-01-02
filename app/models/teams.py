from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from app.config.dbConfig import Base
from app.models.projects import Project

team_membership = Table(
    "team_membership",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("team_id", ForeignKey("teams.id", ondelete="CASCADE"), primary_key=True)
)

class Team(Base):
    __tablename__="teams"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String, nullable=False)

    projects:Mapped[list["Project"]] = relationship(
        back_populates="team",
        cascade="all, delete"
    )

    users: Mapped[list["User"]] = relationship(
        "User",
        secondary="team_membership",
        back_populates="teams"
    )