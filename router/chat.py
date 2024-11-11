from fastapi import APIRouter

router = APIRouter()

@router.get('/chat')
async def get_chat():
    # TODO
    return 0

@router.post('/new_chat')
async def post_new_chat():
    # TODO
    return 0

