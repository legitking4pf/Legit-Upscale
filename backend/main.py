from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from app.upscaler import Upscaler
from app.config import INPUT_DIR
import os
import uuid

app = FastAPI(title = "Legit-Upscale Backend")

# Initialize the model once
upscaler = Upscaler()

@app.post("/upscale")
async def upscale_image(file: UploadFile = File(...)):
# Generate unique input filename
uid = str(uuid.uuid4())
input_path = os.path.join(INPUT_DIR, f" {
  uid
}.png")

# Save uploaded file
with open(input_path, "wb") as f:
f.write(await file.read())

# Run upscaling
output_path = upscaler.upscale(input_path)

# Return the upscaled image
return FileResponse(output_path, media_type = "image/png", filename = "upscaled_8k.png")