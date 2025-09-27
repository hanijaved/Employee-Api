from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import json
import os

# ---------- Employee Schema ----------
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: float

# ---------- App ----------
app = FastAPI(title="Employee Management API")

FILE = "employees.json"

# ---------- Utility Functions ----------
def read_employees():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump([], f)
    with open(FILE, "r") as f:
        return json.load(f)

def write_employees(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Routes ----------
@app.get("/")
def read_root():
    return {"message": "Welcome to Employee Management API"}

@app.get("/employees", response_model=List[Employee])
def get_employees():
    return read_employees()

@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int):
    employees = read_employees()
    for emp in employees:
        if emp["id"] == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post("/employees", response_model=Employee)
def add_employee(employee: Employee):
    employees = read_employees()
    for emp in employees:
        if emp["id"] == employee.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    employees.append(employee.dict())
    write_employees(employees)
    return employee

@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, updated_employee: Employee):
    employees = read_employees()
    for index, emp in enumerate(employees):
        if emp["id"] == employee_id:
            employees[index] = updated_employee.dict()
            write_employees(employees)
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    employees = read_employees()
    for emp in employees:
        if emp["id"] == employee_id:
            employees.remove(emp)
            write_employees(employees)
            return {"message": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")

# ---------- Run with Python ----------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
