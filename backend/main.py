from fastapi import FastAPI

app = FastAPI(
    title="Cloud Cost Optimizer",
    description="AWS Cloud Cost Optimization Platform",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Cloud Cost Optimizer 🚀"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }