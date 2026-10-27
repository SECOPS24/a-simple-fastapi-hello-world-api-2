# Hello World FastAPI

A simple, production-ready FastAPI Hello World API for the team.

## Features

- Root greeting endpoint
- Personalized greeting by name
- Team-specific greeting with endpoint listing
- Health check endpoint
- Auto-generated Swagger UI docs

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Root Hello World response |
| GET | `/hello/{name}` | Personalized greeting |
| GET | `/team` | Team greeting with all endpoints listed |
| GET | `/health` | Health check (returns `{"status": "ok"}`) |
| GET | `/docs` | Swagger UI interactive documentation |
| GET | `/redoc` | ReDoc documentation |

## Running Locally

### With Python

```bash
pip install -r requirements.txt
python main.py
```

The API will be available at: http://localhost:3000

### With Docker

```bash
# Build the image
docker build -t hello-world-api .

# Run the container
docker run -p 3000:3000 hello-world-api
```

The API will be available at: http://localhost:3000

## Example Requests

```bash
# Health check
curl http://localhost:3000/health

# Root greeting
curl http://localhost:3000/

# Personalized greeting
curl http://localhost:3000/hello/Alice

# Team greeting
curl http://localhost:3000/team
```

## Example Responses

**GET /**
```json
{
  "message": "Hello, World!",
  "timestamp": "2024-01-01T12:00:00.000000",
  "version": "1.0.0"
}
```

**GET /hello/Alice**
```json
{
  "message": "Hello, Alice!",
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

**GET /health**
```json
{"status": "ok"}
```
