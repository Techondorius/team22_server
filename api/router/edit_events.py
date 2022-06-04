from fastapi import APIRouter, Depends, HTTPException, Response
from schema.delete_key import DeleteKey
from schema.update_event import UpdateEventSchema
from schema.create_event import CreateEventSchema
from db import get_db
from model import Event
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/api/events")
async def create_event(
    event: CreateEventSchema,
    db: Session = Depends(get_db)
):
    model = event.toSqlModel()
    db.add(model)
    db.commit()
    db.refresh(model)
    return model.toResultJSON()


@router.put("/api/events/{event_id}")
async def update_event(
    event_id: int,
    event: UpdateEventSchema,
    db: Session = Depends(get_db)
):
    model: Event = db.query(Event).get(event_id)
    if model is None:
        raise HTTPException(status_code=404)
    if model.delete_key != event.delete_key:
        raise HTTPException(status_code=404)
    model = event.update_model(model)
    db.add(model)
    db.commit()
    return model.toResultJSON()


@router.put("/api/events/{event_id}/delete")
async def delete_event(
    event_id: int,
    key: DeleteKey,
    db: Session = Depends(get_db)
):
    model: Event = db.query(Event).get(event_id)
    if model is None:
        raise HTTPException(status_code=404)
    if model.delete_key != key.delete_key:
        raise HTTPException(status_code=404)
    db.delete(model)
    db.commit()
    return Response(status_code=204)
