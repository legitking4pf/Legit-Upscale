# backend/app/config.py

import os

# Directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "input")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
WEIGHTS_DIR = os.path.join(BASE_DIR, "weights")

# Model weights
MODEL_WEIGHTS = os.path.join(WEIGHTS_DIR, "RealESRGAN_x4plus.pth")

# Upscale options
UPSCALE_FACTORS = {
    "4K": 2,   # 1080 -> 4K
    "8K": 4    # 1080 -> 8K
}

# Device
DEVICE = "cuda"  # GPU