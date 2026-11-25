# Employee Microservices

A small FastAPI example composed of an API gateway and three services for employee, department, and payroll data. Each service currently stores data in memory, so changes are lost when that service restarts.

## Requirements

- Python 3.10 or later
- pip

## Setup

From this directory, create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## Run

Start each app in a separate terminal from this project directory:

```bash
uvicorn employee_service.main:app --reload --port 8001
```

```bash
uvicorn department_service.main:app --reload --port 8002
```

```bash
uvicorn payroll_service.main:app --reload --port 8003
```

```bash
uvicorn api_gateway.main:app --reload --port 8000
```

The gateway forwards requests to the services at `127.0.0.1` on ports `8001`, `8002`, and `8003`. Start the employee service before using payroll; start all three services before making requests through the gateway.

## API

Interactive API documentation is available at `/docs` for each service:

- Gateway: `http://127.0.0.1:8000/docs`
- Employee service: `http://127.0.0.1:8001/docs`
- Department service: `http://127.0.0.1:8002/docs`
- Payroll service: `http://127.0.0.1:8003/docs`

Gateway endpoints:

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/` | Check that the gateway is running |
| `POST` | `/employees` | Create an employee |
| `GET` | `/employees/{employee_id}` | Get an employee |
| `GET` | `/departments/{department_id}` | Get a department |
| `GET` | `/payroll/{employee_id}` | Calculate payroll using a 10% tax rate |

Example employee request:

```bash
curl -X POST http://127.0.0.1:8000/employees \
  -H 'Content-Type: application/json' \
  -d '{"name":"Alex Morgan","department_id":10,"salary":72000}'
```

The employee service starts with example employees `101` and `102`; the department service starts with departments `10` and `20`.