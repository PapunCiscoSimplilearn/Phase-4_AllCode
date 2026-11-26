# Factory Design Pattern

The Factory design pattern encapsulates object creation so a client can obtain an appropriate object without directly depending on its concrete implementation. Common uses include database implementations, payment gateways, notifications, cloud storage, report formats, and authentication providers.

This example uses an abstract `EmployeeRepository`, three concrete repositories, a `RepositoryFactory`, and an `EmployeeService` that receives its repository through its constructor. The service does not need to change when the selected database changes. This implementation is a Simple Factory; the GoF Factory Method pattern uses a creator abstraction and subclasses that determine which product to instantiate.

The four Python files are `factory_demo.py` (repositories, factory, service, and interactive client), `repositoryfactory.py` and `employee_service.py` (imports for the separate-module example), and `main.py` (FastAPI application).

## Python example

From this directory, run:

```bash
python3 factory_demo.py
```

Enter `sqlite`, `mysql`, or `mongodb` to select the corresponding repository and print its employees.

## FastAPI example

Install the dependencies and start the application from this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs and try `GET /employees/sqlite`, `GET /employees/mysql`, or `GET /employees/mongodb`. An unsupported database such as `oracle` returns HTTP 400.

The repositories return dummy data; no database installation or configuration is required.