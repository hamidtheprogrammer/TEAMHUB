from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config.dbConfig import Base


class Project(Base):
    __tablename__ = "projects"

    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    name:Mapped[str] = mapped_column(String, nullable=False)

    team_id:Mapped[int] = mapped_column(ForeignKey("teams.id", ondelete="CASCADE"))
    team: Mapped["Team"] = relationship(back_populates="projects")