from fastapi import APIRouter, Form
from database.handle_database import *
from model.model import *
from typing import Annotated

router = APIRouter()

@router.post('/login')
async def login(data: Annotated[LoginRequest, Form()]):
    if login(data.id, data.password):
        return {"status": "success"}
    else:
        return {"status": "fail"}

@router.post('/register')
async def register():
    # TODO
    return 0

@router.get('/oauth2/authorize')
async def authorize():
    # TODO
    return 0

@router.post('/oauth2/authorize')
async def post_authorize():
    # TODO
    return 0

@router.get('/oauth2/token')
async def get_token():
    # TODO
    return 0

@router.delete('/oauth2/token')
async def delete_token():
    # TODO
    return 0

@router.patch('/oauth2/token')
async def patch_token():
    # TODO
    return 0

@router.get('/@me')
async def get_me():
    # TODO
    return 0