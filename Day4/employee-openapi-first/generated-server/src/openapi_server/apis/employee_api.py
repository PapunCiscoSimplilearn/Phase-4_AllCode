# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.employee_api_base import BaseEmployeeApi
import openapi_server.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from typing import List
from openapi_server.models.employee import Employee
from openapi_server.models.employee_create import EmployeeCreate


router = APIRouter()

ns_pkg = openapi_server.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/employees",
    status_code=201,
    responses={
        201: {"model": Employee, "description": "Employee created"},
    },
    tags=["Employee"],
    summary="Create employee",
    response_model_by_alias=True,
)
async def create_employee(
    employee_create: EmployeeCreate = Body(..., description=""),
) -> Employee:
    if not BaseEmployeeApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEmployeeApi.subclasses[0]().create_employee(employee_create)


@router.get(
    "/employees",
    responses={
        200: {"model": List[Employee], "description": "List of employees"},
    },
    tags=["Employee"],
    summary="Get all employees",
    response_model_by_alias=True,
)
async def get_employees(
) -> List[Employee]:
    if not BaseEmployeeApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseEmployeeApi.subclasses[0]().get_employees()
