from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI(title="Notification Service")


class NotificationRequest(BaseModel):
    employee_name: str
    email: EmailStr
    message: str


@app.get("/")
def home():
    return {"message": "Notification Service is running"}


@app.post("/notifications")
def send_notification(request: NotificationRequest):
    print("Sending notification...")
    print("Employee:", request.employee_name)
    print("Email:", request.email)
    print("Message:", request.message)

    return {
        "status": "SUCCESS",
        "message": f"Notification sent to {request.email}",
    }
