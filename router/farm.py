from fastapi import APIRouter

router = APIRouter()

@router.put('/farm')
async def put_new_farm():
    # TODO
    return 0

@router.get('/farm')
async def get_farm():
    # TODO
    return 0

@router.get('/farms')
async def get_farms():
    # TODO
    return 0

#UPDATE /farm/<uid>

@router.post('/farm/{UID}')
async def post_request_use_farm():
    # 해당 농장 사용 요청
    # TODO
    return 0