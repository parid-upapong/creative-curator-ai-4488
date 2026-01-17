import hmac
import hashlib
import time
import os
from typing import Optional
from PIL import Image, ImageDraw, ImageFont

class MediaSecurityProvider:
    """
    Handles Intellectual Property protection via dynamic watermarking
    and signed URL generation.
    """
    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def generate_signed_asset_url(self, asset_id: str, expiry: int = 3600) -> str:
        """
        Generates a time-limited HMAC signature for asset access.
        """
        expiration_timestamp = int(time.time()) + expiry
        message = f"{asset_id}:{expiration_timestamp}"
        signature = hmac.new(
            self.secret_key.encode(),
            message.encode(),
            hashlib.sha256
        .hexdigest()
        
        return f"/api/v1/assets/{asset_id}?expires={expiration_timestamp}&signature={signature}"

    def apply_watermark(self, input_path: str, output_path: str, user_id: str):
        """
        Applies a dynamic, semi-transparent watermark to creative assets
        to deter IP theft and trace leaks.
        """
        with Image.open(input_path) as img:
            watermark = Image.new("RGBA", img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark)
            
            # Text: "Protected for [User_ID] - Creative Unlock AI"
            text = f"Protected for {user_id} - Creative Unlock AI"
            
            # Simple tiling logic for watermark
            width, height = img.size
            margin = 50
            draw.text((width - 300, height - margin), text, fill=(255, 255, 255, 128))
            
            out = Image.alpha_composite(img.convert("RGBA"), watermark)
            out.convert("RGB").save(output_path, "JPEG", quality=85)

# Example Usage
# provider = MediaSecurityProvider(os.getenv("ASSET_SECRET"))
# provider.apply_watermark("raw_portfolio.jpg", "protected_portfolio.jpg", "user_99")