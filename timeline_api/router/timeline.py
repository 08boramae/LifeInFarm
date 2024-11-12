from fastapi import APIRouter
from database import handle_database2
from model import model
from typing import Annotated

router = APIRouter()

@router.get('/timeline')
async def get_timeline():
    res = database.get_timeline_list()
    return 0

@router.get('/timelines')
async def get_timelines():
    # TODO
    return 0

@router.put('/timeline')
async def put_timeline():
    # TODO
    return 0

@router.get('/timeline/{UID}')
async def get_timeline_by_UID(UID: int):
    # TODO
    return 0

@router.post('/timeline/{UID}/mento')
async def mento_routerlication(UID: int):
    # TODO
    return 0

@router.post('/timeline/{UID}')
async def post_timeline():
    # TODO
    return 0

@router.post('/timeline/{UID}/{index}')
async def post_comment():
    # TODO
    return 0