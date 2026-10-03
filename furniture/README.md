# 🪑 Furniture Management System

A simple internal web-based management system for a furniture business.

The first version of this project is designed to help the business owner manage **employees and customer orders** in one place.

> **Note:** This is an internal management system. Customers will not directly use the website in the initial version.

---

## 🎯 Purpose

The main purpose of this system is to replace manual record keeping with a simple digital system for managing:

* Employees
* Customer orders
* Order prices
* Customer contact information
* Order status
* Order history

The system will be designed to be simple, fast, and easy for the furniture business owner to use.

---

# ✨ Core Features

## 👨‍🔧 Employee Management

The owner/admin can manage employee information.

Each employee can have information such as:

* Employee ID
* Full name
* Phone number
* Address
* Job/position
* Salary
* Joining date
* Employment status

Example:

| Employee  | Position        | Phone      | Status |
| --------- | --------------- | ---------- | ------ |
| Ram Thapa | Carpenter       | 98XXXXXXXX | Active |
| Hari BK   | Furniture Maker | 97XXXXXXXX | Active |

Admin should be able to:

* Add employee
* Edit employee
* Delete employee
* View employee details
* Search employees
* Mark employee as active/inactive

---

# 📋 Order Management

The owner/admin can record and manage customer orders.

Each order can contain:

* Order ID
* Customer name
* Customer phone number
* Customer address
* Furniture/product name
* Quantity
* Price
* Total amount
* Assigned employee
* Order date
* Expected completion date
* Order status
* Additional notes

Example:

| Order ID | Customer   | Product      |      Price | Employee  | Status    |
| -------- | ---------- | ------------ | ---------: | --------- | --------- |
| ORD-001  | Ram Sharma | Wooden Table | Rs. 25,000 | Hari BK   | Pending   |
| ORD-002  | Sita KC    | Double Bed   | Rs. 45,000 | Ram Thapa | Completed |

---

# 💰 Price Management

The system will store the price associated with each order.

For example:

```text
Product: Wooden Dining Table
Quantity: 1
Price: Rs. 25,000
Discount: Rs. 2,000
Final Amount: Rs. 23,000
```

The system should automatically calculate the final amount where applicable.

---

# 📞 Customer Contact

Customers do not need accounts in the first version.

Their information will simply be stored along with their orders.

Example:

```text
Customer Name: Ram Sharma
Phone: 98XXXXXXXX
Address: Kathmandu
```

This allows the owner to contact customers about their orders.

---

# 📌 Order Status

Each order can have a status.

Initial statuses:

```text
Pending
In Progress
Completed
Delivered
Cancelled
```

The owner can update the status as the order progresses.

---

# 👨‍💼 Admin Dashboard

The main dashboard will provide a quick overview of the business.

Example:

```text
-----------------------------------------
        Furniture Management
-----------------------------------------

Employees                 15

Active Employees          13

Total Orders              82

Pending Orders            12

Orders In Progress        18

Completed Orders          52

-----------------------------------------
```

The dashboard may later include sales information and charts.

---

# 🔎 Search and Filtering

The system should make it easy to find records.

### Employee search

Search by:

* Name
* Phone
* Employee ID
* Position

### Order search

Search by:

* Order ID
* Customer name
* Customer phone
* Product name
* Employee
* Order status

Orders can also be filtered by status or date.

---

# 🏗️ Initial Technology Stack

The project will initially use:

### Backend

* Python
* Django

### Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

### Database

* SQLite for development
* PostgreSQL for production

### Version Control

* Git
* GitHub

---

# 📁 Initial Project Structure

```text
furniture-management/
│
├── README.md
├── requirements.txt
├── .gitignore
├── manage.py
│
├── furniture/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── employees/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
├── orders/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   ├── dashboard.html
│   ├── employees/
│   └── orders/
│
├── static/
│   ├── css/
│   └── js/
│
└── media/
```

---

# 🗄️ Initial Database Models

The first version will mainly use these models:

```text
Employee
    ↓
Order
    ↓
Customer information
```

### Employee

```text
Employee
---------
id
name
phone
address
position
salary
joining_date
status
created_at
```

### Order

```text
Order
-----
id
customer_name
customer_phone
customer_address
product_name
quantity
price
discount
total_amount
employee
order_date
expected_date
status
notes
created_at
```

The relationship between an employee and orders will allow the owner to know **which employee is responsible for each order**.

---

# 🔐 Access

The initial version is intended for **internal business use**.

Customers will not have:

* Customer accounts
* Customer dashboards
* Online ordering
* Product browsing
* Online payments

These features may be considered in future versions.

---

# 🔮 Future Features

After the basic employee and order management system is working, the project may be expanded with:

* 📦 Inventory management
* 🪑 Furniture/product management
* 💵 Expense management
* 💳 Payment tracking
* 🧾 Invoice generation
* 📊 Sales reports
* 📈 Business analytics
* 👥 Customer management
* 🔐 Multiple admin accounts
* 📱 Mobile-friendly interface
* ☁️ Online deployment
* 🛒 Customer-facing website

---

# 🚧 Project Status

**Currently in development.**

### Version 1.0

```text
✅ Employee management
✅ Order management
✅ Customer contact information
✅ Order prices
✅ Order status
✅ Admin dashboard

❌ Customer login
❌ Online ordering
❌ Online payment
❌ Inventory management
❌ Public website
```

---

## 👨‍💻 Author

**Milan**

Furniture Management System
