# FlyRank BE-01 — First API Endpoint

Minimal backend with two JSON endpoints.

## Run
pip install -r requirements.txt
uvicorn main:app --reload

## Endpoints
- GET /       → greeting + status
- GET /time   → current UTC time

## Test
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/time