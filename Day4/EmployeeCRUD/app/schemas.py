from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

EmployeeText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]
Salary = Annotated[Decimal, Field(ge=0, max_digits=12, decimal_places=2, allow_inf_nan=False)]


class EmployeeInput(BaseModel):
    name: EmployeeText
    salary: Salary
    department: EmployeeText


class EmployeeOutput(EmployeeInput):
    model_config = ConfigDict(from_attributes=True)

    id: int