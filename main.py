from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Message(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(message: Message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message.prompt}],
        )
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        return {"error": str(e)}