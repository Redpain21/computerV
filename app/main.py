from fastapi import FastAPI, UploadFile, File, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from deepface import DeepFace

import cv2
import numpy as np


app = FastAPI()


templates = Jinja2Templates(
    directory="app/templates"
)


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image_array = np.frombuffer(
        image_bytes,
        np.uint8
    )

    img = cv2.imdecode(
        image_array,
        cv2.IMREAD_COLOR
    )


    result = DeepFace.analyze(
        img,
        actions=["emotion"],
        enforce_detection=False
    )


    emotions = result[0]["emotion"]

    dominant = result[0]["dominant_emotion"]


    return {

    "dominant": dominant,
    "emotions": {
        emotion: float(value)
        for emotion, value in emotions.items()
    }

}