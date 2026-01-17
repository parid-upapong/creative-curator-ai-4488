from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from src.database import get_db
from src.models.employment import JobOpening, TalentMatch
from src.services.matching_engine import MatchingEngine
from src.schemas.employment import JobCreate, MatchResponse

router = APIRouter(prefix="/api/v1/employment", tags=["Employment"])

@router.post("/jobs", response_model=JobCreate)
def create_job(job_data: JobCreate, db: Session = Depends(get_db)):
    """
    Post a new job and trigger the initial matching background task.
    """
    new_job = JobOpening(**job_data.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    # Background task: trigger_initial_matching(new_job.id)
    return new_job

@router.get("/jobs/{job_id}/matches", response_model=List[MatchResponse])
def get_job_matches(job_id: UUID, min_score: float = 0.7, db: Session = Depends(get_db)):
    """
    Retrieve AI-ranked talent matches for a specific job.
    """
    matches = db.query(TalentMatch).filter(
        TalentMatch.job_id == job_id,
        TalentMatch.overall_match_score >= min_score
    ).order_by(TalentMatch.overall_match_score.desc()).all()
    
    if not matches:
        raise HTTPException(status_code=404, detail="No matches found with current criteria.")
        
    return matches

@router.patch("/matches/{match_id}/status")
def update_match_status(match_id: UUID, status: str, db: Session = Depends(get_db)):
    """
    Update employment lifecycle status (e.g., shortlisting or hiring).
    """
    match = db.query(TalentMatch).filter(TalentMatch.id == match_id).first()
    if not match:
        raise HTTPException(status_code=404, detail="Match record not found")
    
    match.status = status
    db.commit()
    return {"status": "updated", "match_id": match_id}