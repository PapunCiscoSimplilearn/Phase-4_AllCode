from logging_config import logger


class EmployeeRepository:
    def __init__(self):
        self.employees = {
            101: {"id": 101, "name": "Rahul", "salary": 50000},
            102: {"id": 102, "name": "Priya", "salary": 60000},
            103: {"id": 103, "name": "Amit", "salary": 70000},
        }

    def get_employee(self, employee_id):
        logger.debug("Repository received employee ID: %s", employee_id)

        if employee_id == 999:
            logger.critical("Database infrastructure is unavailable")
            raise ConnectionError("Database infrastructure unavailable")

        if employee_id == 500:
            raise RuntimeError("Database query execution failed")

        logger.info("Fetching employee from repository")
        return self.employees.get(employee_id)