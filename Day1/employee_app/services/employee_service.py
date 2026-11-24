from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.employee import Employee, EmployeeCreate, EmployeeUpdate
from repositories.employee_repository import EmployeeRepository


class EmployeeService:
	def __init__(self):
		self.repository = EmployeeRepository()

	def create_employee(self, db: Session, employee: EmployeeCreate):
		if employee.salary <= 0:
			raise ValueError("Salary must be greater than zero")

		try:
			return self.repository.create_employee(db, employee)
		except IntegrityError as error:
			db.rollback()
			raise ValueError("Employee email already exists") from error

	def get_all_employees(self, db: Session):
		return self.repository.get_all_employees(db)

	def get_employee_by_id(self, db: Session, employee_id: int) -> Employee:
		employee = self.repository.get_employee_by_id(db, employee_id)
		if employee is None:
			raise ValueError("Employee not found")
		return employee

	def update_employee(
		self,
		db: Session,
		employee_id: int,
		update_data: EmployeeUpdate,
	):
		employee = self.get_employee_by_id(db, employee_id)
		if update_data.salary is not None and update_data.salary <= 0:
			raise ValueError("Salary must be greater than zero")

		try:
			return self.repository.update_employee(db, employee, update_data)
		except IntegrityError as error:
			db.rollback()
			raise ValueError("Employee email already exists") from error

	def delete_employee(self, db: Session, employee_id: int):
		employee = self.get_employee_by_id(db, employee_id)
		self.repository.delete_employee(db, employee)
		return {"message": "Employee deleted successfully"}
