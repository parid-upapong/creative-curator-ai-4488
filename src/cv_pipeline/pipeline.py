import logging
from PIL import Image
from src.cv_pipeline.models.tagger import AutoTagger
from src.cv_pipeline.models.quality_assessor import VisualQualityAssessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CV_PIPELINE")

class CreativeCVPipeline:
    """
    Main entry point for the Computer Vision Pipeline.
    Integrates tagging and quality assessment into the JSON-C format.
    """
    def __init__(self):
        logger.info("Initializing CV Pipeline Models...")
        self.tagger = AutoTagger()
        self.assessor = VisualQualityAssessor()

    def process_asset(self, image_path: str):
        try:
            image = Image.open(image_path).convert("RGB")
            
            logger.info(f"Processing asset: {image_path}")
            
            # Run parallelizable tasks
            tags = self.tagger.generate_tags(image)
            quality = self.assessor.assess(image)
            
            # Structure into Proprietary JSON-C (Creative Schema)
            cv_metadata = {
                "schema_version": "1.0",
                "asset_analysis": {
                    "tags": tags,
                    "quality_metrics": quality,
                    "dominant_colors": self._extract_dominant_colors(image)
                },
                "standardized_score": quality["overall_viability"]
            }
            
            return cv_metadata

        except Exception as e:
            logger.error(f"Pipeline failure: {str(e)}")
            return {"error": str(e)}

    def _extract_dominant_colors(self, image: Image.Image):
        # Simplified color extraction using small resize
        img = image.resize((50, 50))
        result = img.convert('P', palette=Image.ADAPTIVE, colors=5)
        result = result.convert('RGB')
        main_colors = result.getcolors(50*50)
        
        hex_colors = []
        for count, rgb in main_colors:
            hex_val = '#%02x%02x%02x' % rgb
            hex_colors.append(hex_val)
        return hex_colors

# Example usage for testing
if __name__ == "__main__":
    pipeline = CreativeCVPipeline()
    # result = pipeline.process_asset("portfolio_sample.jpg")
    # print(result)