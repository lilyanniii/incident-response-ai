from fastapi import FastAPI, HTTPException, Request
from vector_storage import get_similar_incidents, store_incidents_in_db
from pydantic  import BaseModel, Field
from rag import claude_response
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import PlainTextResponse


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
store_incidents_in_db()

class UserInput(BaseModel):
    message: str = Field(max_length=1000)

@app.get("/")
def read_root():
    return{"message": "Incident Server (Synthetic data)"}

@app.get("/incidents/{incident_id}")
def get_incident(incident_id: int):
    return {"incident_id": incident_id, "status": "investigating"}

@app.get("/incidents")
def list_incidents(status: str = None or '', severity: int = None or 0, limit: int = 10):
    safe_limit = min(limit, 100)
    return {
        "filters": {"status": status, "severity": severity},
        "limit": safe_limit,
        "incidents": []
    }

@app.post("/analyze")
@limiter.limit("5/minute")
async def create_user(request: Request, user_data: UserInput):
    try:
        similar_incidents = get_similar_incidents(user_data.message)
        (documents, metadatas) = similar_incidents
        results = claude_response(user_data.message, documents)
    except Exception as e:
        raise HTTPException(status_code=500, detail= "Something went wrong when processing your request")
    return PlainTextResponse(results)