import datetime
from typing import Optional
from db import idgen
from model import Event
from pydantic import BaseModel


class CreateEventSchema(BaseModel):
    title: str
    owner: str
    date: datetime.datetime
    note: Optional[str] = None
    url: Optional[str] = None
    delete_key: str

    def toSqlModel(self) -> Event:
        return Event(
            id=idgen(),
            title=self.title,
            owner=self.owner,
            date=self.date,
            note=self.note,
            url=self.url,
            delete_key=self.delete_key
        )
