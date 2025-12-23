from fastapi import FastAPI
from config.settings import settings

#api server
app = FastAPI()

#test route
@app.get("/")
def home():
    return {"message":"Hello from Teamhub"}

# start the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host= "0.0.0.0", port=8002, reload=True)