from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

API_URL = "https://api-inference.huggingface.co/models/handler-bird/movie_genre_multi_classification"
headers = {"Authorization": "Bearer Token"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


class ModelInput(BaseModel):
    description: str


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173/movie_genre/",
    "https://handler-bird.github.io/movie_genre/",
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
    output = query({
        "inputs": prediction.description,
    })
    return output[0][0]['label']
