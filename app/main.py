from fastapi import FastAPI
from app.config.settings import settings
from app.api.v1.routes import auth, users



port = settings.port

#api server
app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


#test route
@app.get("/")
def home():
    return {"message":"Hello from Teamhub"}

