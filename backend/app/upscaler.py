import cv2
import torch
from realesrgan import RealESRGAN
from .config import DEVICE, MODEL_WEIGHTS, UPSCALE_FACTOR, INPUT_DIR, OUTPUT_DIR
import os
import uuid

class Upscaler:
def __init__(self):
# Load the model once
self.device = DEVICE
self.model = RealESRGAN(self.device, scale = UPSCALE_FACTOR)
self.model.load_weights(MODEL_WEIGHTS)

def upscale(self, image_path: str) -> str:
"""
        Takes an input image path, upscales it, saves result in OUTPUT_DIR
        Returns the output path
        """
# Load input image
image = cv2.imread(image_path, cv2.IMREAD_COLOR)
if image is None:
raise ValueError(f"Failed to read image: {
  image_path
}")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Run AI inference
with torch.no_grad():
upscaled = self.model.predict(image)

# Convert back to BGR for OpenCV
upscaled = cv2.cvtColor(upscaled, cv2.COLOR_RGB2BGR)

# Save result
filename = f" {
  uuid.uuid4()}_8k.png"
output_path = os.path.join(OUTPUT_DIR, filename)
cv2.imwrite(output_path, upscaled)

return output_path