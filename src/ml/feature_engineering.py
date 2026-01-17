import pandas as pd
import numpy as np
from typing import Dict, Any

def compute_alignment_features(portfolio_data: Dict[str, Any], job_data: Dict[str, Any]) -> Dict[str, float]:
    """
    Calculates the delta between Creative JSON-C metadata and Job Requirements.
    This is the core logic for the 'Matching' part of the training data.
    """
    # 1. Style Alignment (Cosine Similarity proxy)
    style_match = 1.0 if portfolio_data['primary_style'] == job_data['required_style'] else 0.0
    
    # 2. Score Deltas
    # If a job requires a technical score of 0.8 and creative has 0.9, delta is positive.
    tech_delta = portfolio_data['aggregated_scores']['technical'] - job_data['min_technical_req']
    
    # 3. Tag Intersection
    portfolio_tags = set(portfolio_data['metadata']['tags'])
    job_tags = set(job_data['required_tags'])
    tag_overlap = len(portfolio_tags.intersection(job_tags)) / max(len(job_tags), 1)
    
    return {
        "style_match_score": style_match,
        "technical_alignment": tech_delta,
        "tag_overlap_ratio": tag_overlap,
        "commercial_viability": portfolio_data['aggregated_scores']['commercial'],
        "innovation_index": portfolio_data['aggregated_scores']['innovation']
    }

def preprocess_training_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw interaction logs into a feature matrix for XGBoost.
    """
    # Convert categorical strings to codes
    for col in ['primary_style', 'job_category']:
        if col in df.columns:
            df[col] = df[col].astype('category').cat.codes
            
    return df