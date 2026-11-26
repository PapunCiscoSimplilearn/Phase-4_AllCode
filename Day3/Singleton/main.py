from fastapi import FastAPI


app = FastAPI()


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Database manager created")
        return cls._instance

    def get_connection(self):
        return "Database connection successful"


@app.get("/employees")
def get_employees():
    db = DatabaseConnection()
    return {
        "service": "Employee Service",
        "connection": db.get_connection(),
        "object_id": id(db),
    }


@app.get("/departments")
def get_departments():
    db = DatabaseConnection()
    return {
        "service": "Department Service",
        "connection": db.get_connection(),
        "object_id": id(db),
    }