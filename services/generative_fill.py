from typing import Dict, Any, Optional
import requests
import base64
import io

def generative_fill(
    api_key: str,
    image_data: bytes,
    mask_data: bytes,
    prompt: str,
    negative_prompt: Optional[str] = None,
    num_results: int = 4,
    sync: bool = False,
    seed: Optional[int] = None,
    content_moderation: bool = False,
    mask_type: str = "manual"
) -> Dict[str, Any]:
    """
    Generate content in a masked area of an image using a text prompt.
    
    Args:
        api_key: Bria AI API key
        image_data: Image data in bytes
        mask_data: Mask image data in bytes
        prompt: Description of what to generate in the masked area
        negative_prompt: Description of what to avoid (optional)
        num_results: Number of variations to generate (1-4)
        sync: Whether to wait for results
        seed: Optional seed for reproducible results
        content_moderation: Whether to enable content moderation
        mask_type: Type of mask ('manual' or 'automatic')
    """
url = "https://engine.prod.bria-api.com/v1/gen_fill"

headers = {
    'api_token': api_key,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# Convert image and mask bytes to base64 data URLs
def bytes_to_data_url(image_bytes):
    """Convert image bytes to a base64 data URL string"""
    base64_str = base64.b64encode(image_bytes).decode()
    return f"data:image/png;base64,{base64_str}"

def pil_image_to_data_url(img):
    """Convert a PIL Image to a base64 data URL string"""
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_data = buf.getvalue()
    base64_str = base64.b64encode(byte_data).decode()
    return f"data:image/png;base64,{base64_str}"