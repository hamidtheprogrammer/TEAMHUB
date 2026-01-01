from fastapi import FastAPI
from app.config.settings import settings
from app.api.v1.routes import auth



port = settings.port

#api server
app = FastAPI()

app.include_router(auth.router)


#test route
@app.get("/")
def home():
    return {"message":"Hello from Teamhub"}

# start the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host= "0.0.0.0", port=port, reload=True)