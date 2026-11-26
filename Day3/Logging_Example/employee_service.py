from logging_config import logger
from employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self, repository=None):
        self.repository = repository or EmployeeRepository()

    def get_employee(self, employee_id):
        logger.debug("Service processing employee ID: %s", employee_id)
        employee = self.repository.get_employee(employee_id)

        if employee is None:
            logger.warning("Employee not found: %s", employee_id)
            return None

        logger.info("Employee retrieved successfully: %s", employee_id)
        return employee