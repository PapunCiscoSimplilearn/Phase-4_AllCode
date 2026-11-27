# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import List
from openapi_server.models.employee import Employee
from openapi_server.models.employee_create import EmployeeCreate


class BaseEmployeeApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseEmployeeApi.subclasses = BaseEmployeeApi.subclasses + (cls,)
    async def create_employee(
        self,
        employee_create: EmployeeCreate,
    ) -> Employee:
        ...


    async def get_employees(
        self,
    ) -> List[Employee]:
        ...
