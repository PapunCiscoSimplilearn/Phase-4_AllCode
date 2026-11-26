from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates

from models.employee_model import EmployeeModel


router = APIRouter()
templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parent.parent / "views")
)
model = EmployeeModel()


@router.get("/employees")
def get_employees(request: Request):
    employees = model.get_all_employees()
    return templates.TemplateResponse(
        request=request,
        name="employees.html",
        context={"employees": employees},
    )


@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employee = model.get_employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee