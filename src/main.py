from fastapi import FastAPI
from src.api.v1.employment import router as employment_router

app = FastAPI(
    title="Creative Unlock AI - Employment Services",
    description="Backend API for high-precision creative matching and employment lifecycle management.",
    version="1.0.0"
)

# Include Routers
app.include_router(employment_router)

@app.get("/health")
def health_check():
    return {"status": "operational", "service": "matching-engine"}