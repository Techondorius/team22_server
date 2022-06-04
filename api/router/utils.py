from schema.delete_key import DeleteKey
from fastapi import APIRouter, Depends, HTTPException, Response
from db import get_db
from model import Event
from sqlalchemy.orm import Session


router = APIRouter()

@router.put("/api/events/{event_id}/check_key")
async def delete_event(
    event_id: int,
    key: DeleteKey,
    db: Session = Depends(get_db)
):
    model: Event = db.query(Event).get(event_id)
    if model is None:
        raise HTTPException(status_code=404)
    if model.delete_key != key.delete_key:
        raise HTTPException(status_code=401)
    return Response()
    