class EmployeeModel:
    def __init__(self):
        self.employees = [
            {
                "id": 101,
                "name": "Rahul",
                "department": "IT",
                "salary": 50000,
            },
            {
                "id": 102,
                "name": "Priya",
                "department": "HR",
                "salary": 60000,
            },
            {
                "id": 103,
                "name": "Amit",
                "department": "Finance",
                "salary": 70000,
            },
        ]

    def get_all_employees(self):
        return self.employees

    def get_employee_by_id(self, employee_id):
        for employee in self.employees:
            if employee["id"] == employee_id:
                return employee
        return None