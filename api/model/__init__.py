from db import Base, engine
from .event import Event

__all__ = [
    "Event",
]

Base.metadata.create_all(engine)
