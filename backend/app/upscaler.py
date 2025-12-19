# backend/app/upscaler.py

import os
from config import DEVICE, MODEL_WEIGHTS, OUTPUT_DIR
from PIL import Image
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGAN
import uuid

class Upscaler:
def __init__(self, scale_factor: int = 4):
self.scale_factor = scale_factor
self.device = DEVICE
self.model = self.load_model()

def load_model(self):
model = RRDBNet(
  num_in_ch = 3, num_out_ch = 3, num_feat = 64, num_block = 23, num_grow_ch = 32, scale = self.scale_factor
)
upscaler = RealESRGAN(model, scale = self.scale_factor)
upscaler.load_weights(MODEL_WEIGHTS, download = False)
upscaler.model.to(self.device)
upscaler.model.half() # Use FP16 to save memory
upscaler.model.eval()
return upscaler

def upscale_image(self, image_path: str) -> str:
image = Image.open(image_path).convert("RGB")
output_filename = f" {
  uuid.uuid4()}_upscaled.png"
output_path = os.path.join(OUTPUT_DIR, output_filename)
os.makedirs(OUTPUT_DIR, exist_ok = True)
result = self.model.enhance(image)
result.save(output_path)
return output_path