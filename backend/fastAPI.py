from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

classifier = pipeline("text-classification", model="handler-bird/movie_genre_multi_classification")


class ModelInput(BaseModel):
    description: str


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

# allows cross-origin access
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/prediction/")
async def create_prediction(prediction: ModelInput):
    output = classifier(prediction.description)
    return output[0]['label']
