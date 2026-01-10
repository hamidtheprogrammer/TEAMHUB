from sqlalchemy.orm import Session
from app.models.teams import Team


# create team
def create_team(db:Session, team:Team):
    db.add(team)
    db.commit()
    db.refresh(team)
    return team