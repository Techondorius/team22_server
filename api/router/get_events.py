from fastapi import APIRouter, Depends, HTTPException
from model.event import Event
from db import engine, SessionLocal, get_db
from sqlalchemy.orm import Session, sessionmaker
from starlette.requests import Request

router = APIRouter()
@router.get('/api/events')
async def index(db: Session = Depends(get_db)):
    events_list = db.query(Event).all()
    return events_list

@router.get('/api/events/{event_id}')
async def index(event_id: int, db: Session = Depends(get_db)):
    event_list = db.query(Event).filter(Event.id == event_id).first()
    if event_list is None:
        raise HTTPException(status_code=404, detail="item_not_found")
    else:
        return event_list
