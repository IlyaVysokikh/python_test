from pydantic import BaseModel, Field

from typing import List, Optional

from src.models.element_measurements import ElementMeasurements


class Element(BaseModel):
    element_name: str = Field(..., alias="elementName")
    element_description: str = Field(..., alias="elementDescription")
    element_measurements: Optional[ElementMeasurements] = Field(..., alias="elementMeasurements")
