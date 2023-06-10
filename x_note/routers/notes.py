from fastapi import APIRouter


router = APIRouter(tags=['notes'], prefix='/notes')


@router.get('/')
async def get_all_notes():
    return {'message': 'Get all notes'}
