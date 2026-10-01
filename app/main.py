from fastapi import FastAPI

app = FastAPI(
    title="AlnairMind AI",
    description="AI-Powered Document Intelligence Platform",
    version="0.1.0",
)

@app.get("/")
async def root() -> dict[str, str]:
    return {
        "name": "AlnairMind AI",
        "status": "running",
    }


@app.get("/health")
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
