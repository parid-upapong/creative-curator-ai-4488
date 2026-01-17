import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
from src.cv_pipeline.config import CVConfig

class AutoTagger:
    """
    Leverages CLIP (Contrastive Language-Image Pre-training) for zero-shot 
    classification of creative styles and mediums.
    """
    def __init__(self):
        self.device = CVConfig.DEVICE
        self.model = CLIPModel.from_pretrained(CVConfig.CLIP_MODEL).to(self.device)
        self.processor = CLIPProcessor.from_pretrained(CVConfig.CLIP_MODEL)
        self.styles = CVConfig.CREATIVE_STYLES
        self.mediums = CVConfig.CREATIVE_MEDIUMS

    def generate_tags(self, image: Image.Image):
        # Prepare prompts
        style_prompts = [f"This image is in {s} style" for s in self.styles]
        medium_prompts = [f"This image is a {m}" for m in self.mediums]
        all_prompts = style_prompts + medium_prompts

        inputs = self.processor(
            text=all_prompts, 
            images=image, 
            return_tensors="pt", 
            padding=True
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model(**inputs)
            logits_per_image = outputs.logits_per_image
            probs = logits_per_image.softmax(dim=1).cpu().numpy()[0]

        results = []
        for i, prob in enumerate(probs):
            if prob > CVConfig.TAG_CONFIDENCE_THRESHOLD:
                tag_name = all_prompts[i].replace("This image is in ", "").replace("This image is a ", "")
                results.append({
                    "tag": tag_name,
                    "confidence": float(prob),
                    "type": "style" if i < len(self.styles) else "medium"
                })
        
        return sorted(results, key=lambda x: x['confidence'], reverse=True)