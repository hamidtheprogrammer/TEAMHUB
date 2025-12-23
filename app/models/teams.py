from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from config.dbConfig import Base

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
        back_populates="teams",
        cascade="all, delete"
    )

    users: Mapped[list["Team"]] = relationship(
        "Team",
        secondary="team_membership",
        back_populates="teams"
    )