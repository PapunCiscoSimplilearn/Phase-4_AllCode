# MVC Design Pattern

This FastAPI example organizes an employee management app using MVC principles:

- **Model** (`models/employee_model.py`) manages the in-memory employee data.
- **View** (`views/employees.html`) renders employee data as an HTML table with Jinja2.
- **Controller** (`controllers/employee_controller.py`) handles requests and connects the model to the view or JSON response.

## Run the application

From this directory, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, use `python -m venv .venv` and `.venv\\Scripts\\activate` instead.

Install dependencies and start the development server:

```bash
python -m pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/employees` to view the employee table. The JSON endpoint `http://127.0.0.1:8000/employees/101` returns one employee; an unknown ID returns HTTP 404. The root endpoint `/` returns a welcome message.

The model uses sample data rather than a database. FastAPI does not enforce MVC, but this project separates the responsibilities into the corresponding components.