from pydantic import BaseModel


class DeleteKey(BaseModel):
    delete_key: str
