from fastapi import FastAPI
from app.customer_api import customer_router
from app.item_api import item_router
from app.sales_api import sales_router

app = FastAPI(title="Frappe API Examples")

# API Modüllerini Dahil Et
app.include_router(customer_router, prefix="/customers", tags=["Customers"])
app.include_router(item_router, prefix="/items", tags=["Items"])
app.include_router(sales_router, prefix="/sales", tags=["Sales"])

@app.get("/")
def home():
    return {"message": "Frappe API ile FastAPI Örnekleri"}