import datetime
from typing import Optional
from model import Event as EventModel
from pydantic import BaseModel


class Event(BaseModel):
    title: Optional[str] = None
    owner: Optional[str] = None
    date: Optional[datetime.datetime] = None
    note: Optional[str] = None
    url: Optional[str] = None


class UpdateEventSchema(BaseModel):
    delete_key: str
    event: Event

    def update_model(self, model: EventModel) -> EventModel:
        if self.event is None:
            return model
        model.title = if_present_or(self.event.title, model.title)
        model.owner = if_present_or(self.event.owner, model.owner)
        model.date = if_present_or(self.event.date, model.date)
        model.note = if_present_or(self.event.note, model.note)
        model.url = if_present_or(self.event.url, model.url)
        model.delete_key = if_present_or(self.delete_key, model.delete_key)
        return model


def if_present_or(opt, default):
    return opt if opt is not None else default
