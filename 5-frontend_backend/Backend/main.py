from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import google.generativeai as genai
import os

app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )
@app.get("/")
def read_root():
    return {"msg": "BackEnd is woring fine"}

class UserInput(BaseModel):
    user_input: str
@app.post("/Agent")
async def Agent(data:UserInput):

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    try:
        response = genai.GenerativeModel("gemini-2.0-flash").generate_content(data.user_input).text
        if response is None:
            raise HTTPException(status_code=500, detail="No response from the model")
        return {"response":response } 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
