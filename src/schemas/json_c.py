from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from uuid import UUID

class AIScore(BaseModel):
    technical: float = Field(..., ge=0, le=1)
    commercial: float = Field(..., ge=0, le=1)
    innovation: float = Field(..., ge=0, le=1)
    style_consistency: float = Field(..., ge=0, le=1)

class CreativeMetadata(BaseModel):
    tags: List[str]
    primary_style: str
    secondary_styles: List[str]
    dominant_colors: List[str]
    complexity_score: float

class JSONC_Portfolio(BaseModel):
    """
    Proprietary Creative Schema (JSON-C) for AI-driven matching.
    """
    version: str = "1.0.0"
    creative_id: UUID
    assets_count: int
    aggregated_scores: AIScore
    metadata: CreativeMetadata
    vector_embedding: List[float]  # Generated from CLIP/LLM embeddings of the work