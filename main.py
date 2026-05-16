from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return{"message": "Hello World"}

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

