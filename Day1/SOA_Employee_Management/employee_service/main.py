import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field

app = FastAPI(title="Employee Service")
employees = []
DEPARTMENT_SERVICE_URL = "http://127.0.0.1:8002"
NOTIFICATION_SERVICE_URL = "http://127.0.0.1:8004"


class EmployeeRequest(BaseModel):
    name: str
    email: EmailStr
    department_id: int
    salary: float = Field(gt=0)


@app.get("/")
def home():
    return {"message": "Employee Service is running"}


@app.post("/employees")
def create_employee(employee: EmployeeRequest):
    try:
        department_response = requests.get(
            f"{DEPARTMENT_SERVICE_URL}/departments/{employee.department_id}",
            timeout=5,
        )
        department_response.raise_for_status()
        department = department_response.json()
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail="Department Service unavailable or request failed",
        ) from error

    new_employee = {
        "id": len(employees) + 1,
        "name": employee.name,
        "email": str(employee.email),
        "department_id": employee.department_id,
        "department_name": department["name"],
        "salary": employee.salary,
    }
    employees.append(new_employee)

    try:
        notification_response = requests.post(
            f"{NOTIFICATION_SERVICE_URL}/notifications",
            json={
                "employee_name": employee.name,
                "email": str(employee.email),
                "message": "Employee registered successfully",
            },
            timeout=5,
        )
        notification_response.raise_for_status()
        notification = notification_response.json()
    except requests.RequestException:
        notification = {
            "status": "FAILED",
            "message": "Employee registered, but notification failed",
        }

    return {
        "message": "Employee registered successfully",
        "employee": new_employee,
        "notification": notification,
    }


@app.get("/employees")
def get_employees():
    return employees
