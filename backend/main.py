# backend/main.py

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
from app.upscaler import Upscaler
from app.config import UPSCALE_FACTORS, INPUT_DIR

app = FastAPI(title="Legit Upscale Backend")

# Enable CORS for mobile app requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your app domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize default upscaler (can be switched dynamically)
upscaler = Upscaler(scale_factor=4)  # default to 4x

@app.post("/upscale")
async def upscale_image(
    file: UploadFile = File(...),
    target_resolution: str = Form("4K")  # 4K or 8K
):
    if target_resolution not in UPSCALE_FACTORS:
        return {"error": "Invalid target resolution. Choose 4K or 8K."}

    scale = UPSCALE_FACTORS[target_resolution]
    upscaler.scale_factor = scale  # dynamically set scale
    upscaler.model.scale = scale

    os.makedirs(INPUT_DIR, exist_ok=True)
    input_path = os.path.join(INPUT_DIR, file.filename)
    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = upscaler.upscale_image(input_path)

    return {"upscaled_image_path": output_path, "target_resolution": target_resolution}