import torch

class CVConfig:
    # Device Configuration
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Model checkpoints
    CLIP_MODEL = "openai/clip-vit-base-patch32"
    AESTHETIC_MODEL = "laion/CLIP-ViT-H-14-laion2B-s32B-b79K" # Reference for quality scoring
    
    # Tagging Thresholds
    TAG_CONFIDENCE_THRESHOLD = 0.25
    
    # Predefined Creative Categories for Zero-Shot Tagging
    CREATIVE_STYLES = [
        "minimalist", "brutalist", "bauhaus", "cyberpunk", "flat design", 
        "3d abstract", "skeuomorphic", "neomorphism", "vintage", "corporate-modern"
    ]
    
    CREATIVE_MEDIUMS = [
        "vector illustration", "oil painting", "digital photography", 
        "3d render", "ui/ux layout", "motion graphics", "typography", "branding"
    ]

    # Quality Assessment Benchmarks
    QUALITY_METRICS = {
        "sharpness_threshold": 500, # Laplacian variance
        "min_resolution": (1080, 1080)
    }