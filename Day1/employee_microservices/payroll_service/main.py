import requests
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Payroll Service")
EMPLOYEE_SERVICE_URL = "http://127.0.0.1:8001"


@app.get("/")
def home():
    return {"message": "Payroll Service Running"}


@app.get("/payroll/{employee_id}")
def calculate_payroll(employee_id: int):
    try:
        response = requests.get(
            f"{EMPLOYEE_SERVICE_URL}/employees/{employee_id}",
            timeout=5,
        )
    except requests.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail="Employee Service unavailable or request failed",
        ) from error

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Employee not found")
    if not response.ok:
        raise HTTPException(status_code=502, detail="Employee Service request failed")

    employee = response.json()
    salary = employee["salary"]
    tax = salary * 0.10
    return {
        "employee_id": employee["id"],
        "employee_name": employee["name"],
        "salary": salary,
        "tax_rate": 0.10,
        "tax": tax,
        "net_salary": salary - tax,
    }