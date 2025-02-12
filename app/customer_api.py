from fastapi import APIRouter
import requests
from app.config import FRAPPE_URL, HEADERS

customer_router = APIRouter()

@customer_router.post("/create/")
def create_customer(name: str, email: str, phone: str):
    """Frappe ERP'ye yeni bir müşteri ekler."""
    data = {
        "doctype": "Customer",
        "customer_name": name,
        "email_id": email,
        "mobile_no": phone,
        "customer_type": "Individual",
        "customer_group": "Commercial",
        "territory": "All Territories"
    }

    response = requests.post(f"{FRAPPE_URL}/api/resource/Customer", json=data, headers=HEADERS)
    return response.json()
