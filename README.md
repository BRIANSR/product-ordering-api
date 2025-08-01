# 🛒 Product Ordering API – Django REST Framework

A Django REST API for a basic e-commerce product ordering system. Users can sign up, browse products, place orders, and view their order history. Admins can add products.

---

## 🚀 Features

- User Signup & Login with `is_admin` flag
- Admins can add products
- View and filter products (by name)
- Place orders (validates and updates stock)
- View user's order history with product details
- Bonus: Login-protected HTML product listing page

---

## 🛠️ Tech Stack

- Python 3
- Django 4.2
- Django REST Framework
- SQLite (default database)
- Django templates (for HTML page)
- Tested using Postman

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/BRIANSR/product-ordering-api.git
cd product-ordering-api
```

### 2. Create & Activate Virtual Environment

#### Windows (PowerShell):

```bash
python -m venv venv
.env\Scriptsctivate
```

#### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔐 Admin Panel (optional)

To create a superuser for the admin site:

```bash
python manage.py createsuperuser
```

Then login at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📮 API Endpoints

| Method | Endpoint              | Description                     |
|--------|-----------------------|---------------------------------|
| POST   | `/signup/`            | Register a new user             |
| POST   | `/login/`             | Login with credentials          |
| GET    | `/products/`          | List all products (with filter) |
| POST   | `/products/`          | Add new product (admin only)    |
| POST   | `/orders/place/`      | Place an order (auth required)  |
| GET    | `/orders/history/`    | View user's order history       |
| GET    | `/products-page/`     | HTML product listing (login)    |

---

## 📤 Postman Collection

To test all endpoints via Postman:

### 🗂 Collection File:

- [`Django Product Ordering API.postman_collection.json`](./Django%20Product%20Ordering%20API.postman_collection.json)

### 🧪 Contains requests for:

- Signup
- Login
- Add Product (admin only)
- Get Products
- Place Order
- View Orders

---

## 🧾 Sample Admin User

```json
{
  "username": "brian",
  "password": "brian123",
  "is_admin": true
}
```
## 👤 Author

**Name**: Brian  
**GitHub**: [@BRIANSR](https://github.com/BRIANSR)

### 1. Clone the Repo
```bash
 https://github.com/BRIANSR/BRIANSR-product-ordering-api.git
