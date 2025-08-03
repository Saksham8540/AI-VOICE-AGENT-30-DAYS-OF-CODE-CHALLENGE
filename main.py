from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import requests
import os

# Load environment variables
load_dotenv()
MURF_API_KEY = os.getenv("MURF_API_KEY")

app = FastAPI()

class TTSRequest(BaseModel):
    text: str

@app.post("/generate-audio")
def generate_audio(request_data: TTSRequest):
    headers = {
        "Authorization": f"Bearer {MURF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "text": request_data.text,
        "voice": "en-US-Wavenet-D",  # Replace with the correct Murf voice ID if needed
        "speed": 1.0,
        "pitch": 1.0
    }

    response = requests.post("https://api.murf.ai/v1/tts/generate", headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return {"audio_url": result.get("audio_url")}
    else:
        return {"error": response.json()}