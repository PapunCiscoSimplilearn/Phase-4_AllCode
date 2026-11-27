from openapi_server.apis.employee_api_base import BaseEmployeeApi
from openapi_server.models.employee import Employee
from openapi_server.models.employee_create import EmployeeCreate


employees = [
    Employee(id=101, name="Rahul", department="IT", salary=50000),
    Employee(id=102, name="Priya", department="HR", salary=60000),
]


class EmployeeApiImpl(BaseEmployeeApi):
    async def get_employees(self) -> list[Employee]:
        return employees

    async def create_employee(self, employee_create: EmployeeCreate) -> Employee:
        new_employee = Employee(
            id=len(employees) + 101,
            name=employee_create.name,
            department=employee_create.department,
            salary=employee_create.salary,
        )
        employees.append(new_employee)
        return new_employee