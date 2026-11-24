from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Payroll Service")


class PayrollRequest(BaseModel):
    employee_id: int
    basic_salary: float = Field(gt=0)


@app.get("/")
def home():
    return {"message": "Payroll Service is running"}


@app.post("/payroll/calculate")
def calculate_salary(request: PayrollRequest):
    basic = request.basic_salary
    hra = basic * 0.20
    allowance = basic * 0.10
    gross_salary = basic + hra + allowance
    tax = gross_salary * 0.10
    net_salary = gross_salary - tax

    return {
        "employee_id": request.employee_id,
        "basic_salary": basic,
        "hra": hra,
        "allowance": allowance,
        "gross_salary": gross_salary,
        "tax": tax,
        "net_salary": net_salary,
    }
