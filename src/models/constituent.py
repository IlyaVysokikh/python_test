from pydantic import BaseModel, Field

from typing import Optional

from src.enums.gender import Gender


class Constituent(BaseModel):
    constituent_id: int = Field(..., alias='constituentID')
    role: str
    name: str
    constituentULAN_URL: Optional[str]
    constituentWikidata_URL: Optional[str]
    gender: Optional[Gender]
