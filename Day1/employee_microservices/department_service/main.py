from fastapi import FastAPI, HTTPException

app = FastAPI(title="Department Service")

departments = {
    10: {"id": 10, "name": "IT"},
    20: {"id": 20, "name": "Finance"},
}


@app.get("/")
def home():
    return {"message": "Department Service Running"}


@app.get("/departments/{department_id}")
def get_department(department_id: int):
    department = departments.get(department_id)
    if department is None:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@app.get("/departments")
def get_all_departments():
    return list(departments.values())