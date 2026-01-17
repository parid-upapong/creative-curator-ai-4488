from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from .agents.creative_analyzer import CreativeAnalysisAgent

app = FastAPI(title="Creative Unlock AI - Scoring Engine")

class AnalysisRequest(BaseModel):
    talent_id: str
    asset_urls: List[str]
    job_context: Optional[dict] = None

@app.post("/v1/analyze")
async def perform_analysis(request: AnalysisRequest):
    """
    Endpoint to trigger the AI Agent analysis for a creative portfolio.
    """
    agent = CreativeAnalysisAgent(api_key=os.getenv("OPENAI_API_KEY"))
    
    try:
        report = await agent.analyze_portfolio(
            assets=request.asset_urls, 
            context=request.job_context or {"general": "portfolio review"}
        )
        return {
            "status": "success",
            "data": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/v1/health")
def health_check():
    return {"status": "operational", "version": "1.0.0-beta"}