from pydantic import BaseModel, Field
from typing import List


class ArtObjectsList(BaseModel):
    total: int
    object_IDs: List[int] = Field(..., alias="objectIDs")


