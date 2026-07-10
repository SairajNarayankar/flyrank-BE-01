# FlyRank Backend - API Endpoint (BE-01)

A minimal FastAPI backend implementation providing foundational REST API endpoints for the FlyRank project.

## 📋 Overview

This is the first backend service in the FlyRank ecosystem, featuring two JSON endpoints:
- A health check endpoint for service status
- A time endpoint returning current UTC timestamp information

Built with [FastAPI](https://fastapi.tiangolo.com/) for high performance and automatic API documentation.

## ✨ Features

- **FastAPI Framework** — Fast, modern Python web framework
- **JSON Endpoints** — RESTful JSON API responses
- **Auto Documentation** — Automatic interactive API docs (Swagger UI, ReDoc)
- **Easy Setup** — Minimal dependencies and quick startup

## 📦 Prerequisites

- Python 3.7+
- pip (Python package manager)

## 🚀 Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SairajNarayankar/flyrank-BE-01.git
   cd flyrank-BE-01
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server:**
   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`

## 📡 API Endpoints

### Root Endpoint
- **Method:** `GET`
- **URL:** `/`
- **Response:**
  ```json
  {
    "message": "Hello from FlyRank BE-01",
    "status": "ok"
  }
  ```

### Time Endpoint
- **Method:** `GET`
- **URL:** `/time`
- **Response:**
  ```json
  {
    "utc": "2026-07-10T12:34:56.789123",
    "epoch": 1784274896
  }
  ```

## 🧪 Testing

### Using cURL

```bash
# Test the root endpoint
curl http://127.0.0.1:8000/

# Test the time endpoint
curl http://127.0.0.1:8000/time
```

### Using FastAPI Interactive Docs

Once the server is running, visit:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## 📁 Project Structure

```
flyrank-BE-01/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 📦 Dependencies

- **fastapi** — Web framework for building APIs
- **uvicorn** — ASGI server for running FastAPI applications

## 🔧 Development

### Hot Reload
The `--reload` flag enables automatic server restart on file changes (useful during development).

To run without hot reload:
```bash
uvicorn main:app
```

### Production Deployment
For production, use a production-grade ASGI server:
```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker
```

## 📝 License

This project is currently unlicensed. Consider adding a LICENSE file for clarity.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## 📞 Contact

For questions or issues, reach out to the repository owner or open a GitHub issue.

---

**Status:** Initial API setup  
**Last Updated:** 2026-07-10
