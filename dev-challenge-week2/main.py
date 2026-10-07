from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel

app = FastAPI(title="TrailWise AI - Outdoor Activity & Trail Advisor")

OLLAMA_URL = "http://localhost:11434/api/generate"


class TrailQuery(BaseModel):
  activity: str  # e.g., "hiking", "gardening", "run club"
  location_or_climate: str  # e.g., "temperate fall foliage", "frost zone 6"


@app.get("/")
def read_root():
  return {
      "status": "online",
      "project": "TrailWise AI - Touch Grass Assistant",
      "challenge": "Hacktoberfest 2026 Week 1",
  }


@app.post("/advise")
async def get_outdoor_advice(query: TrailQuery):
  system_prompt = (
      f"You are TrailWise AI. Give quick, practical outdoor advice for "
      f"{query.activity} in {query.location_or_climate}. Focus on actionable"
      " safety, gear, or trail tips so the user can get outside quickly."
  )
  payload = {
      "model": "llama3.2",
      "prompt": system_prompt,
      "stream": False,
  }
  async with httpx.AsyncClient(timeout=60.0) as client:
    try:
      res = await client.post(OLLAMA_URL, json=payload)
      if res.status_code == 200:
        return {"advice": res.json().get("response", "")}
      raise HTTPException(status_code=500, detail="Ollama error")
    except Exception as e:
      return {
          "advice": (
              f"TrailWise Active: Pack essential gear for {query.activity} in"
              f" {query.location_or_climate}. Stay hydrated!"
          ),
          "note": str(e),
      }