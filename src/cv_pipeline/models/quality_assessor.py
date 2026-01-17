import cv2
import numpy as np
from PIL import Image
import torch
import torch.nn as nn
from torchvision import models, transforms
from src.cv_pipeline.config import CVConfig

class VisualQualityAssessor:
    """
    Assesses technical quality (sharpness, contrast) and aesthetic appeal 
    using a custom MLP head on top of a ResNet backbone.
    """
    def __init__(self):
        self.device = CVConfig.DEVICE
        # Using a pretrained ResNet as a feature extractor for aesthetic scoring
        self.backbone = models.resnet50(pretrained=True)
        self.backbone.fc = nn.Sequential(
            nn.Linear(2048, 512),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(512, 1),
            nn.Sigmoid()
        )
        self.backbone.to(self.device).eval()
        
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

    def get_technical_metrics(self, image: Image.Image):
        cv_img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        
        # Sharpness using Laplacian variance
        sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        # Brightness and Contrast
        brightness = np.mean(gray)
        contrast = gray.std()
        
        # Resolution check
        width, height = image.size
        
        return {
            "sharpness": float(sharpness),
            "brightness": float(brightness),
            "contrast": float(contrast),
            "resolution": f"{width}x{height}",
            "is_hi_res": width >= CVConfig.QUALITY_METRICS["min_resolution"][0]
        }

    def get_aesthetic_score(self, image: Image.Image):
        """Predicts an aesthetic score between 0 and 1."""
        img_tensor = self.transform(image).unsqueeze(0).to(self.device)
        with torch.no_grad():
            score = self.backbone(img_tensor).item()
        return round(score * 10, 2) # Scale to 0-10

    def assess(self, image: Image.Image):
        tech = self.get_technical_metrics(image)
        aesthetic = self.get_aesthetic_score(image)
        
        # Logic for 'Commercial Viability'
        viability = (aesthetic * 0.7) + ((tech['sharpness'] / 1000) * 0.3)
        
        return {
            "technical_score": tech,
            "aesthetic_score": aesthetic,
            "overall_viability": min(10.0, viability)
        }