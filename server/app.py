from fastapi import FastAPI
from inference import run_step

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Healthcare OpenEnv Running"}

@app.post("/step")
def step(action: dict):
    return run_step(action)

@app.post("/reset")
def reset():
    return {"status": "reset done"}

@app.get("/state")
def state():
    return {"state": "running"}


def main():
    return app

if __name__ == "__main__":
    main()