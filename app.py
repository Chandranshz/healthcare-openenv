from fastapi import FastAPI
from inference import run

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Healthcare OpenEnv Running"}

@app.post("/run")
def execute():
    return run()