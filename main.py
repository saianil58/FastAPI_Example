from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

app = FastAPI()

# routes

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.get("/predict/{input_msg}")
def get_prediction(input_msg: str):
    loaded_model = pickle.load(open('nlp.model', 'rb'))
    return(loaded_model.predict([input_msg])[0])