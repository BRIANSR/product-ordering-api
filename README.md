# 🛒 Django Product Ordering API

A Django REST API that allows users to sign up, view products, place orders, and view order history. Admin users can add products. Includes a bonus HTML page listing products (login required).

---

## 🚀 Features

- Custom User Model with `is_admin` flag
- Signup and Login APIs (basic auth, no tokens)
- Admin-only Product Creation API
- Product Listing API (with optional search by name)
- Order Placement API with stock validation and price calculation
- Order History API with detailed product info
- HTML product list page (bonus feature)

---

## 🛠️ Tech Stack

- Python 3
- Django 4.2
- Django REST Framework
- SQLite (default DB)
- HTML (via Django templates)
- Postman (for testing)

---

## 🔧 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/BRIANSR/product-ordering-api.git
cd product-ordering-api
```

### 2. Create virtual environment
```bash
python -m venv venv
.env\Scriptsctivate        # On Windows
# or
source venv/bin/activate      # On Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔑 Authentication

This project uses session-based authentication.

- Login is required to place orders and view order history.
- Admins are allowed to add new products.

**Admin sample user:**
```json
{
  "username": "brian",
  "password": "brian123",
  "is_admin": true
}
```

---

## 📦 API Endpoints

### 🔹 Signup
```http
POST /signup/
```
```json
{
  "username": "brian",
  "password": "brian123",
  "is_admin": true
}
```

### 🔹 Login
```http
POST /login/
```
```json
{
  "username": "brian",
  "password": "brian123"
}
```

### 🔹 Get Products
```http
GET /products/
```

### 🔹 Add Product (admin only)
```http
POST /products/
```
```json
{
  "name": "Laptop",
  "price": 999.99,
  "stock_quantity": 10
}
```

### 🔹 Place Order
```http
POST /orders/place/
```
```json
{
  "items": [
    {
      "product": 1,
      "quantity": 2
    }
  ]
}
```

### 🔹 View Order History
```http
GET /orders/history/
```

### 🔹 Product Page (HTML)
```http
GET /products-page/
```

---

## 🧪 Postman Testing

- Collection: [`Django Product Ordering API.postman_collection.json`](./Django%20Product%20Ordering%20API.postman_collection.json)
- Includes: Signup, Login, Add Product, Get Products, Place Order, View Orders

---

## 🧑 Author

**Name**: Brian  
**GitHub**: [@BRIANSR](https://github.com/BRIANSR)
