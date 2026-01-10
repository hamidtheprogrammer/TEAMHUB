from app.repositories import teams
from app.models.users import UserRole
from app.models.teams import Team


# Create team
def create_team(db, user, team_data):
    if not user or user.role != UserRole.ADMIN:
        raise ValueError("Not authorized")
    team = Team(
        name = team_data.name
    )
    new_team = teams.create_team(db, team)
    return new_team