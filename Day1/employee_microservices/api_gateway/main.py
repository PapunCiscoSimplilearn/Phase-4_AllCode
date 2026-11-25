import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Employee API Gateway")

EMPLOYEE_URL = "http://127.0.0.1:8001"
DEPARTMENT_URL = "http://127.0.0.1:8002"
PAYROLL_URL = "http://127.0.0.1:8003"


class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1)
    department_id: int
    salary: float = Field(gt=0)


def forward_request(method: str, url: str, **kwargs):
    try:
        response = requests.request(method, url, timeout=5, **kwargs)
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail="Downstream service unavailable or request failed",
        ) from error

    if not response.ok:
        try:
            detail = response.json().get("detail", "Downstream request failed")
        except ValueError:
            detail = "Downstream request failed"
        raise HTTPException(status_code=response.status_code, detail=detail)
    return response.json()


@app.get("/")
def home():
    return {"message": "API Gateway Running"}


@app.post("/employees", status_code=201)
def create_employee(employee: EmployeeCreate):
    return forward_request(
        "POST",
        f"{EMPLOYEE_URL}/employees",
        json=employee.model_dump(),
    )


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return forward_request("GET", f"{EMPLOYEE_URL}/employees/{employee_id}")


@app.get("/departments/{department_id}")
def get_department(department_id: int):
    return forward_request("GET", f"{DEPARTMENT_URL}/departments/{department_id}")


@app.get("/payroll/{employee_id}")
def get_payroll(employee_id: int):
    return forward_request("GET", f"{PAYROLL_URL}/payroll/{employee_id}")