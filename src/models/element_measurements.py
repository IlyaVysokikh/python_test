from pydantic import BaseModel, Field

from typing import Optional


class ElementMeasurements(BaseModel):
    depth: Optional[float] = Field(..., alias="Depth")
    height: Optional[float] = Field(..., alias="Height")
    width: Optional[float] = Field(..., alias="Width")