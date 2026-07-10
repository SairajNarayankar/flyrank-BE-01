from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FlyRank BE-01", "status": "ok"}

@app.get("/time")
def get_time():
    return {"utc": datetime.utcnow().isoformat(), "epoch": int(datetime.utcnow().timestamp())}