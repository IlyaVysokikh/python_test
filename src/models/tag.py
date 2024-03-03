from pydantic import BaseModel, Field


class Tag(BaseModel):
    term: str
    aat_url: str = Field(..., alias="AAT_URL")
    wikidata_URL: str = Field(..., alias="Wikidata_URL")

