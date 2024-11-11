from fastapi import FastAPI, Form
from typing import Annotated
from model import models
from database import handle_database
from router import timeline

app = FastAPI()

@app.route('/')
def index():
    return {"status":"up"}

app.include_router(timeline.router)