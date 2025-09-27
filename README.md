# Employee Management API

This project is a simple Employee Management API built with FastAPI. It allows you to add, view, update, and delete employee records, with data stored in a JSON file for persistence. The entire project is contained in a single file, making it easy to run on mobile or PC. It also includes interactive API documentation available at `/docs`.

## Features
- Add new employees
- View all employees or a single employee by ID
- Update employee details
- Delete employees
- Persistent storage using `employees.json`
- Interactive API documentation via FastAPI Swagger UI

## Requirements
- Python 3.9+
- FastAPI
- Uvicorn
- Pydantic

## Installation & Usage
1. Copy this folder to your device.
2. Install dependencies:
   
```bash
pip install -r requirements.txt

3. Run the server:
uvicorn main:app --reload

4.Open your browser at:
http://127.0.0.1:8000/docs

API Endpoints
Method    	Endpoint             	Description
GET	      /employees         	Get all employees
GET	      /employees/{id}    	Get employee by ID
POST    	/employees	        Add new employee
PUT	      /employees/{id}    	Update employee
DELETE	  /employees/{id}   	Delete employee

```bash
pip install -r requirements.txt
