from fastapi import FastAPI, Request
from pydantic import BaseModel
import openai
import os

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/chat")
async def chat(prompt: Prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt.prompt}]
    )
    return {"response": response['choices'][0]['message']['content']}

@app.get("/")
def read_root():
    return {"message": "It works!"}
