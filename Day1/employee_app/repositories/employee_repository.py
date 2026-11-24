from sqlalchemy.orm import Session

from models.employee import Employee, EmployeeCreate, EmployeeUpdate


class EmployeeRepository:
    def create_employee(
        self,
        db: Session,
        employee: EmployeeCreate,
    ):
        new_employee = Employee(
            name=employee.name,
            email=employee.email,
            department=employee.department,
            salary=employee.salary,
        )
        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)
        return new_employee

    def get_all_employees(self, db: Session):
        return db.query(Employee).all()

    def get_employee_by_id(self, db: Session, employee_id: int):
        return db.query(Employee).filter(Employee.id == employee_id).first()

    def update_employee(
        self,
        db: Session,
        employee: Employee,
        update_data: EmployeeUpdate,
    ):
        data = update_data.model_dump(exclude_unset=True)
        for key, value in data.items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)
        return employee

    def delete_employee(self, db: Session, employee: Employee):
        db.delete(employee)
        db.commit()