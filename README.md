# Frappe API ile FastAPI Örnekleri

Bu proje, **Frappe ERP** sistemine REST API üzerinden **müşteri, ürün ve satış siparişi** ekleyen **FastAPI tabanlı** bir uygulamadır. 

## 🚀 Kurulum

### 1️⃣ Gerekli Kütüphaneleri Yükleyin
```sh
pip install -r requirements.txt
```
### 2️⃣ API Sunucusunu Başlatın
```sh
uvicorn app.main:app --reload
```
### 3️⃣ API Kullanımı

####Müşteri Ekleme
```sh
POST http://127.0.0.1:8000/customers/create/
Content-Type: application/json

{
    "name": "Ali Veli",
    "email": "ali@example.com",
    "phone": "+905551234567"
}
```
####Ürün Ekleme
```sh
POST http://127.0.0.1:8000/items/create/
Content-Type: application/json

{
    "item_name": "Laptop",
    "item_code": "LAP123",
    "price": 15000,
    "stock": 20
}
```
####Satış Siparişi Ekleme
```sh
POST http://127.0.0.1:8000/sales/create/
Content-Type: application/json

{
    "customer_name": "Ali Veli",
    "item_code": "LAP123",
    "qty": 2,
    "price": 15000
}
```
