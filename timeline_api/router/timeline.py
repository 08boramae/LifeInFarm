from fastapi import APIRouter, Form
from database.handle_database import *
from model.model import *
from typing import Annotated

router = APIRouter()

@router.get('/timeline')
async def _get_timeline():
    # res = get_timeline_list()
    # return res

    # 정확한 의미 파악이 필요함.
    # 문서상 '배정된 타임라인을 불러온다' 라고 되어있는데, 이게 정확히 무슨 의미인지 파악해야함.
    # TODO
    return 0

@router.get('/timelines')
async def _get_timelines():
    res = get_timeline_list()
    res = {
        "contents": [
            {
                "id": i[0],
                "title": i[1],
                "owner": i[2],
                "thumbnail": i[3],
                "contents": i[4],
                "farm": i[5]
            } for i in res
        ]
    }
    return res

@router.put('/timeline')
async def _put_timeline(data: Annotated[PutTimeline, Form()]):
    # TODO: owner ID, def add_timeline(title, owner, thumbnail, contents, farm):
    # verify via 2oauth.
    owner = 1
    if add_timeline(data.title, owner, data.thumbnail, data.contents, data.farm):
        return {"status": "success"}
    else:
        return {"status": "fail"}


@router.get('/timeline/{UID}')
async def _get_timeline_by_UID(UID: int):
    res = get_timeline_via_UID(UID)
    res = {
        "id": res[0][0],
        "lines": res[0][4]
    }
    return(res)

@router.post('/timeline/{UID}/mento')
async def _mento_routerlication(UID: int):
    # why fucking routerlication zzzzzzzzz
    # maybe app -> router replace then mento_routerlication
    # TODO
    return 0

@router.post('/timeline/{UID}')
async def _post_timeline():
    # TODO
    return 0

@router.post('/timeline/{UID}/{index}')
async def _post_comment():
    #
    return 0