from pydantic import BaseModel, Field


class Department(BaseModel):
    department_id: int = Field(..., alias="departmentId")
    display_name: str = Field(..., alias="displayName")
