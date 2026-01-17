import torch

class TrainingConfig:
    # Model Hyperparameters
    MODEL_TYPE = "xgboost_ranker"
    SEED = 42
    TEST_SIZE = 0.2
    
    # Feature Configuration
    NUMERIC_FEATURES = [
        'technical_score', 'commercial_score', 'innovation_score', 
        'style_consistency', 'complexity_score', 'budget_alignment'
    ]
    CATEGORICAL_FEATURES = [
        'primary_style', 'job_category', 'creative_region'
    ]
    
    # Target Column: 1 if hired, 0 otherwise
    TARGET = "employment_outcome"
    
    # Optimization Params (Optuna)
    N_TRIALS = 50
    MODEL_SAVE_PATH = "models/employment_success_v1.bin"