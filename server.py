import uvicorn
from fastapi import FastAPI
import numpy as np

from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
import torch
import base64
from io import BytesIO

model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
if torch.cuda.is_available():
    pipe = pipe.to("cuda")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Stable diffusion v2.1 by Stability AI API. Run <BASE_URL>/generate/<PROMPT> to generate image"}


@app.post("/generate/{prompt}")
def generate_image(prompt: str):
    image = pipe(prompt).images[0]
    buffered = BytesIO()
    image.save(buffered, format="jpeg")
    img_str = base64.b64encode(buffered.getvalue())
    return {"generated image": img_str}

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8080)
