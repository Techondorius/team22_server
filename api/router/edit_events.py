from fastapi import APIRouter, Depends
from schema.create_event import CreateEventSchema
from db import get_db
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
