import os
import torch

# Device configuration: use GPU if available, otherwise CPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
WEIGHTS_DIR = os.path.join(BASE_DIR, "weights")
MODEL_WEIGHTS = os.path.join(WEIGHTS_DIR, "RealESRGAN_x4plus.pth")

# Create directories if missing
os.makedirs(INPUT_DIR, exist_ok = True)
os.makedirs(OUTPUT_DIR, exist_ok = True)
os.makedirs(WEIGHTS_DIR, exist_ok = True)

# Model settings
UPSCALE_FACTOR = 4 # Real-ESRGAN x4