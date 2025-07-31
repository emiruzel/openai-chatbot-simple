from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.post("/chat")
async def chat(prompt: Prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt.prompt}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"message": "It works!"}
