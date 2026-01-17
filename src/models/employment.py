from sqlalchemy import Column, String, Float, JSON, ForeignKey, Table, DateTime
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy.orm import relationship
import uuid
import datetime

# Association table for Matches/Applications
class JobOpening(Base):
    __tablename__ = "job_openings"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    employer_id = Column(UUID(as_uuid=True), index=True)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=False)
    
    # Matching Criteria
    required_tags = Column(ARRAY(String))
    target_style = Column(String(100))
    min_score_threshold = Column(Float, default=0.7)
    
    # Budget & Metadata
    budget_range = Column(JSON) # {"min": 5000, "max": 10000, "currency": "USD"}
    status = Column(String, default="open") # open, closed, filled
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class TalentMatch(Base):
    __tablename__ = "talent_matches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("job_openings.id"))
    creative_id = Column(UUID(as_uuid=True), index=True)
    
    # Score Breakdown
    overall_match_score = Column(Float)
    style_alignment = Column(Float)
    skill_fit = Column(Float)
    
    # AI Explanation
    match_reasoning = Column(String) 
    status = Column(String, default="suggested") # suggested, shortlisted, rejected, hired