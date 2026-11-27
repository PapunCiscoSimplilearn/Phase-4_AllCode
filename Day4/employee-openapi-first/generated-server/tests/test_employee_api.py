import unittest

from fastapi.testclient import TestClient

from openapi_server.impl.employee_api_impl import employees
from openapi_server.main import app
from openapi_server.models.employee import Employee


class EmployeeApiTests(unittest.TestCase):
    def setUp(self):
        employees[:] = [
            Employee(id=101, name="Rahul", department="IT", salary=50000),
            Employee(id=102, name="Priya", department="HR", salary=60000),
        ]
        self.client = TestClient(app)

    def test_list_employees(self):
        response = self.client.get("/employees")
        self.assertEqual(response.status_code, 200)
        self.assertEqual([employee["id"] for employee in response.json()], [101, 102])

    def test_create_employee(self):
        response = self.client.post(
            "/employees", json={"name": "Alex", "department": "IT", "salary": 45000}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            "id": 103, "name": "Alex", "department": "IT", "salary": 45000
        })
        self.assertEqual(len(self.client.get("/employees").json()), 3)

    def test_invalid_employee(self):
        for payload in (
            None,
            {"name": "", "department": "IT", "salary": 1},
            {"name": "Alex", "department": "IT", "salary": -1},
            {"name": "Alex", "department": "IT"},
        ):
            with self.subTest(payload=payload):
                self.assertEqual(self.client.post("/employees", json=payload).status_code, 422)

