from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Hello World API",
    description="A simple FastAPI Hello World API",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def root():
    return {
        "message": "Hello, World!",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }


@app.get("/hello/{name}")
def hello_name(name: str):
    return {
        "message": f"Hello, {name}!",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/team")
def team_greeting():
    return {
        "message": "Hello, Team! Welcome to our FastAPI service.",
        "timestamp": datetime.utcnow().isoformat(),
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Root hello world"},
            {"path": "/hello/{name}", "method": "GET", "description": "Personalized greeting"},
            {"path": "/team", "method": "GET", "description": "Team greeting"},
            {"path": "/health", "method": "GET", "description": "Health check"},
            {"path": "/docs", "method": "GET", "description": "Swagger UI documentation"},
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
