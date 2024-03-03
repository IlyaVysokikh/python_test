from typing import List

from pydantic import BaseModel

from src.models.Department import Department


class DepartmentsList(BaseModel):
    departments: List[Department]
