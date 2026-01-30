from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from agent.graph import app as agent

app = FastAPI()

@app.post("/chat")
def chat(payload: dict):
    return agent.invoke({
        "last_user_message": payload["message"]
    })

