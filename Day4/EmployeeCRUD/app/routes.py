from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from app.database import get_session
from app.repository import EmployeeRepository
from app.schemas import EmployeeInput, EmployeeOutput
from app.service import EmployeeNotFound, EmployeeService

router = APIRouter(prefix="/employees", tags=["employees"])


def get_employee_service(session: Annotated[Session, Depends(get_session)]) -> EmployeeService:
    return EmployeeService(EmployeeRepository(session))


Service = Annotated[EmployeeService, Depends(get_employee_service)]


@router.post("", response_model=EmployeeOutput, status_code=status.HTTP_201_CREATED)
def create_employee(data: EmployeeInput, service: Service) -> EmployeeOutput:
    return EmployeeOutput.model_validate(service.create_employee(data))


@router.get("", response_model=list[EmployeeOutput])
def list_employees(service: Service) -> list[EmployeeOutput]:
    return [EmployeeOutput.model_validate(employee) for employee in service.list_employees()]


@router.get("/{employee_id}", response_model=EmployeeOutput)
def get_employee(employee_id: int, service: Service) -> EmployeeOutput:
    try:
        return EmployeeOutput.model_validate(service.get_employee(employee_id))
    except EmployeeNotFound:
        raise HTTPException(status_code=404, detail="Employee not found") from None


@router.put("/{employee_id}", response_model=EmployeeOutput)
def update_employee(employee_id: int, data: EmployeeInput, service: Service) -> EmployeeOutput:
    try:
        return EmployeeOutput.model_validate(service.update_employee(employee_id, data))
    except EmployeeNotFound:
        raise HTTPException(status_code=404, detail="Employee not found") from None


@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int, service: Service) -> Response:
    try:
        service.delete_employee(employee_id)
    except EmployeeNotFound:
        raise HTTPException(status_code=404, detail="Employee not found") from None
    return Response(status_code=status.HTTP_204_NO_CONTENT)