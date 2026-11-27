from app.model import Employee
from app.repository import EmployeeRepository
from app.schemas import EmployeeInput


class EmployeeNotFound(Exception):
    pass


class EmployeeService:
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    def list_employees(self) -> list[Employee]:
        return self.repository.list()

    def get_employee(self, employee_id: int) -> Employee:
        employee = self.repository.get(employee_id)
        if employee is None:
            raise EmployeeNotFound(employee_id)
        return employee

    def create_employee(self, data: EmployeeInput) -> Employee:
        return self.repository.create(data)

    def update_employee(self, employee_id: int, data: EmployeeInput) -> Employee:
        return self.repository.update(self.get_employee(employee_id), data)

    def delete_employee(self, employee_id: int) -> None:
        self.repository.delete(self.get_employee(employee_id))