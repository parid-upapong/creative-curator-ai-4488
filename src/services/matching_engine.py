import numpy as np
from typing import List, Dict
from src.schemas.json_c import JSONC_Portfolio
from src.models.employment import JobOpening

class MatchingEngine:
    """
    Core service to calculate compatibility between Creative Portfolios (JSON-C)
    and Job Requirements.
    """

    @staticmethod
    def calculate_cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
        a = np.array(vec_a)
        b = np.array(vec_b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def compute_match(self, portfolio: JSONC_Portfolio, job: JobOpening) -> Dict:
        # 1. Style Alignment (30% weight)
        style_score = 1.0 if portfolio.metadata.primary_style == job.target_style else 0.5
        if job.target_style in portfolio.metadata.secondary_styles:
            style_score = 0.8

        # 2. Tag/Skill Fit (30% weight)
        matched_tags = set(portfolio.metadata.tags).intersection(set(job.required_tags))
        skill_score = len(matched_tags) / len(job.required_tags) if job.required_tags else 1.0

        # 3. AI Quality Benchmarks (40% weight)
        # We prioritize Commercial Viability for Employment matching
        quality_score = (
            portfolio.aggregated_scores.commercial * 0.5 +
            portfolio.aggregated_scores.technical * 0.3 +
            portfolio.aggregated_scores.innovation * 0.2
        )

        # Total Weighted Score
        total_score = (style_score * 0.3) + (skill_score * 0.3) + (quality_score * 0.4)

        return {
            "score": round(total_score, 4),
            "breakdown": {
                "style": style_score,
                "skills": skill_score,
                "quality": quality_score
            },
            "reasoning": f"Matches {len(matched_tags)} key skills with a {portfolio.metadata.primary_style} aesthetic focus."
        }