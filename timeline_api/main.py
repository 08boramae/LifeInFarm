from fastapi import FastAPI
from router import router

app = FastAPI()

@app.route('/')
def index():
    return {"status":"up"}

app.include_router(router.router)