import joblib
import pandas as pd
from .feature_engineering import compute_alignment_features

class MatchingInference:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def get_success_probability(self, portfolio_json_c, job_spec):
        """
        API Gateway calls this to rank creatives for an employer.
        """
        # 1. Feature Extraction
        features = compute_alignment_features(portfolio_json_c, job_spec)
        
        # 2. Convert to DataFrame for model
        feature_df = pd.DataFrame([features])
        
        # 3. Predict Probability
        prob = self.model.predict_proba(feature_df)[:, 1]
        
        return float(prob[0])

# Usage example for the Backend Matching Algorithm
# matcher = MatchingInference("models/employment_success_v1.bin")
# score = matcher.get_success_probability(user_portfolio, open_job)