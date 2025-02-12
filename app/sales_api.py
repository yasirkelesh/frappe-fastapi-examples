from fastapi import APIRouter
import requests
from app.config import FRAPPE_URL, HEADERS

sales_router = APIRouter()

@sales_router.post("/create/")
def create_sales_order(customer_name: str, item_code: str, qty: int, price: float):
    """Frappe ERP'ye yeni bir satış siparişi ekler."""
    data = {
        "doctype": "Sales Order",
        "customer": customer_name,
        "items": [
            {
                "item_code": item_code,
                "qty": qty,
                "rate": price
            }
        ]
    }

    response = requests.post(f"{FRAPPE_URL}/api/resource/Sales Order", json=data, headers=HEADERS)
    return response.json()
