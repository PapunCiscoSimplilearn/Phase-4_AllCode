from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Employee Service")

employees = {
    101: {
        "id": 101,
        "name": "Irfan",
        "department_id": 10,
        "salary": 50000,
    },
    102: {
        "id": 102,
        "name": "Rahul",
        "department_id": 20,
        "salary": 60000,
    },
}


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1)
    department_id: int
    salary: float = Field(gt=0)


@app.get("/")
def home():
    return {"message": "Employee Service Running"}


@app.post("/employees", status_code=201)
def create_employee(employee: EmployeeCreate):
    employee_id = max(employees, default=100) + 1
    new_employee = {
        "id": employee_id,
        "name": employee.name,
        "department_id": employee.department_id,
        "salary": employee.salary,
    }
    employees[employee_id] = new_employee
    return new_employee


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employee = employees.get(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@app.get("/employees")
def get_all_employees():
    return list(employees.values())