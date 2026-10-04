from fastapi import FastAPI, HTTPException
import httpx
from pydantic import BaseModel

app = FastAPI(title="Hacktoberfest 2026 Local RAG Engine")

OLLAMA_URL = "http://localhost:11434/api/generate"


class QueryRequest(BaseModel):
  prompt: str


@app.get("/")
def read_root():
  return {
      "status": "online",
      "project": "Resilient Local RAG Backend Engine",
      "event": "Hacktoberfest 2026 DEV Challenge",
  }


@app.post("/generate")
async def generate_response(request: QueryRequest):
  payload = {
      "model": "llama3.2",
      "prompt": request.prompt,
      "stream": False,
  }
  async with httpx.AsyncClient(timeout=60.0) as client:
    try:
      response = await client.post(OLLAMA_URL, json=payload)
      if response.status_code == 200:
        return {"response": response.json().get("response", "")}
      else:
        raise HTTPException(
            status_code=500, detail="Ollama service returned an error."
        )
    except Exception as e:
      return {
          "response": (
              f"Local RAG Engine Received Prompt: '{request.prompt}'. "
              "Ollama fallback active."
          ),
          "note": str(e),
      }