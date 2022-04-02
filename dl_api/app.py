from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import items, upload

from resnet_utils import CatDogModel

import numpy as np

app = FastAPI()  # Create FastAPI instance

# Add routers

app.include_router(items.router)
app.include_router(upload.router)

# region CORS

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# endregion

# Basic demo


@app.get("/")
async def root():
    # model = load_model(None, None)
    # RandomImagePrediction('./catdogs/Bernese.jpg', model)
    model = CatDogModel()
    model('./catdogs/test_dog.jpg')
    return {"message": "Hello World"}
