from fastapi import FastAPI
import uvicorn

from app.api.routes import router

app = FastAPI(
    title="FinPilot API",
    version="1.0.0",
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Welcome to FinPilot API 🚀"
    }
if __name__ == "__main__":
    uvicorn.run(
        "run_api:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
