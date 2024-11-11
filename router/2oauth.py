from fastapi import APIRouter

router = APIRouter()

@router.post('/login')
async def login():
    # TODO
    return 0

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