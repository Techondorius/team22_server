from fastapi import APIRouter

router = APIRouter()

@router.get('/api/events')
async def index():
    return {
        'events': [
            {
                'id': 1,
                'title': '技育CAMP',
                'owner': 'サポーターズ',
                'date': '2022-06-05 15:00:00'
            },
            {
                'id': 2,
                'title': '技育展',
                'owner': 'サポーターズ',
                'date': '2022-10-13 15:00:00'
            }
        ]
    }

@router.get('/api/events/{event_id}')
async def index(event_id: int):
    return {
                'id': 2,
                'title': '技育展',
                'owner': 'サポーターズ',
                'date': '2022-10-13 15:00:00'
            }