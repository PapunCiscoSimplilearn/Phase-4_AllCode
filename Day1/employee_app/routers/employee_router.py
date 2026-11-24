from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from models.employee import EmployeeCreate, EmployeeResponse, EmployeeUpdate
from services.employee_service import EmployeeService


router = APIRouter(prefix="/employees", tags=["employees"])
employee_service = EmployeeService()


@router.post("/", response_model=EmployeeResponse, status_code=201)
def create_employee(
	employee: EmployeeCreate,
	db: Session = Depends(get_db),
):
	try:
		return employee_service.create_employee(db, employee)
	except ValueError as error:
		raise HTTPException(status_code=400, detail=str(error)) from error


@router.get("/", response_model=List[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
	return employee_service.get_all_employees(db)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
	try:
		return employee_service.get_employee_by_id(db, employee_id)
	except ValueError as error:
		raise HTTPException(status_code=404, detail=str(error)) from error


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
	employee_id: int,
	employee: EmployeeUpdate,
	db: Session = Depends(get_db),
):
	try:
		return employee_service.update_employee(db, employee_id, employee)
	except ValueError as error:
		status_code = 404 if str(error) == "Employee not found" else 400
		raise HTTPException(status_code=status_code, detail=str(error)) from error


@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
	try:
		return employee_service.delete_employee(db, employee_id)
	except ValueError as error:
		raise HTTPException(status_code=404, detail=str(error)) from error
