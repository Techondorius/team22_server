from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from model.event import Event
from db import get_db
from sqlalchemy.orm import Session

router = APIRouter()
@router.get('/api/events')
async def events_list(db: Session = Depends(get_db)):
    events_list = db.query(Event).filter(Event.date > datetime.now()).all()
    output = []
    for i in events_list:
        model = i.toResultJSON()
        model.pop('note')
        model.pop('url')
        output.append(model)
    return {
        "events": output
    }

@router.get('/api/events/{event_id}')
async def event_detail(
    event_id: int,
    db: Session = Depends(get_db)
):
    event_dict = db.query(Event).filter(Event.id == event_id, Event.date > datetime.now()).first()
    if event_dict is None:
        raise HTTPException(status_code=404, detail="item_not_found")
    else:
        return event_dict.toResultJSON()
