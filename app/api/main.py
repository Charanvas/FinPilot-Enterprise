from fastapi import FastAPI

app = FastAPI(
    title="FinPilot AI",
    description="Enterprise Invoice Auditor Agent",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to FinPilot AI 🚀"
    }