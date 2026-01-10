from pydantic import BaseModel

class team_response(BaseModel):
    id:int
    name:str
    projects:list
    users:list

class team_create(BaseModel):
    name:str
