from fastapi import FastAPI
from router import timeline

app = FastAPI()

@app.route('/')
def index():
    return {"status":"up"}

app.include_router(timeline.router)