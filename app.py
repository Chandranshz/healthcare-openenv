from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import HealthcareEnv

app = FastAPI()

env = HealthcareEnv()

class ActionInput(BaseModel):
    action: str


@app.get("/")
def home():
    return {"message": "Healthcare OpenEnv running"}


@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}


@app.post("/step")
def step(input: ActionInput):
    state, reward, done, _ = env.step(input.action)
    return {
        "state": state,
        "reward": reward,
        "done": done
    }


@app.get("/state")
def state():
    return {"state": env.state()}