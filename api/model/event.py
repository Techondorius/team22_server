from db import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import String, DateTime, TIMESTAMP, BigInteger
from sqlalchemy.sql.functions import current_timestamp


class Event(Base):
    __tablename__ = 'events'
    id = Column('id', BigInteger, primary_key=True, index=True)
    title = Column('title', String(45), nullable=False)
    owner = Column('owner', String(45), nullable=False)
    url = Column('url', String(2083), nullable=True)
    note = Column('note', String(1000), nullable=True)
    date = Column('date', DateTime, nullable=False)
    delete_key = Column("delete_key", String(45), nullable=False)
    updated_at = Column(
        "updated_at",
        TIMESTAMP,
        default=current_timestamp(),
        onupdate=current_timestamp(),
        nullable=False)
    created_at = Column(
        "created_at",
        TIMESTAMP,
        default=current_timestamp(),
        nullable=False)

    def toResultJSON(self):
        return{
            "id": self.id,
            "title": self.title,
            "owner": self.owner,
            "date": self.date,
            "note": self.note,
            "url": self.url
        }
