from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class modelInput(BaseModel):
    description: str


app = FastAPI()

# allows cross-origin access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/prediction/")
async def create_prediction(prediction: modelInput):
    return {'message': f'The prediction to your description: "{prediction.description}" is ...'}
