from fastapi import APIRouter, Depends, HTTPException, status
from app.api.v1.schemas.teams import team_create, team_response
from app.config.dbConfig import get_db
from sqlalchemy.orm import Session
from app.utils.auth import get_current_user
from app.api.v1.services import teams

router = APIRouter()

@router.post("/teams", response_model=team_response, status_code=status.HTTP_201_CREATED)
def create_team(team:team_create, db:Session = Depends(get_db), user = Depends(get_current_user)):
    try:
        return teams.create_team(db, user, team)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
