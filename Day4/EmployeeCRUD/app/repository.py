from sqlalchemy import select
from sqlalchemy.orm import Session

from app.model import Employee
from app.schemas import EmployeeInput


class EmployeeRepository:
    def __init__(self, session: Session):
        self.session = session

    def list(self) -> list[Employee]:
        return list(self.session.scalars(select(Employee).order_by(Employee.id)))

    def get(self, employee_id: int) -> Employee | None:
        return self.session.get(Employee, employee_id)

    def create(self, data: EmployeeInput) -> Employee:
        employee = Employee(**data.model_dump())
        self.session.add(employee)
        self.session.commit()
        self.session.refresh(employee)
        return employee

    def update(self, employee: Employee, data: EmployeeInput) -> Employee:
        employee.name = data.name
        employee.salary = data.salary
        employee.department = data.department
        self.session.commit()
        self.session.refresh(employee)
        return employee

    def delete(self, employee: Employee) -> None:
        self.session.delete(employee)
        self.session.commit()