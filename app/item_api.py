from fastapi import APIRouter
import requests
from app.config import FRAPPE_URL, HEADERS

item_router = APIRouter()

@item_router.post("/create/")
def create_item(item_name: str, item_code: str, price: float, stock: int):
    """Frappe ERP'ye yeni bir ürün ekler."""
    data = {
        "doctype": "Item",
        "item_name": item_name,
        "item_code": item_code,
        "standard_rate": price,
        "stock_uom": "Unit",
        "is_stock_item": 1,
        "opening_stock": stock
    }

    response = requests.post(f"{FRAPPE_URL}/api/resource/Item", json=data, headers=HEADERS)
    return response.json()
