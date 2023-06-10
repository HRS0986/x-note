from fastapi import APIRouter


router = APIRouter(tags=['categories'], prefix='/categories')


@router.get('/')
async def get_all_categories():
    return {'message': 'Get all categories'}
