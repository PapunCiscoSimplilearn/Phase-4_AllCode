from fastapi import FastAPI, HTTPException

app = FastAPI(title="Department Service")

departments = {
    101: {"id": 101, "name": "IT"},
    102: {"id": 102, "name": "HR"},
    103: {"id": 103, "name": "Finance"},
}


@app.get("/")
def home():
    return {"message": "Department Service is running"}


@app.get("/departments/{department_id}")
def get_department(department_id: int):
    department = departments.get(department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@app.get("/departments")
def get_departments():
    return list(departments.values())
