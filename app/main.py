from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title= "AI Doctor Recommendation System")

class DoctorRequest(BaseModel):
    symptoms: str
    location: str

@app.get("/")
def home():
    return {"message": "Doctor AI Agent System Running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/find-doctor")
def find_doctor(request: DoctorRequest):
    return {
        "message": "Request recieved",
        "symptoms": request.symptoms,
        "location": request.location
    }