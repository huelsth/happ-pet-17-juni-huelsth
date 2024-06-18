# Happy Pets E-Commerce Project

This project is an e-commerce platform for pet products called "Happy Pets". The application allows users to browse products, add them to a cart, and place orders. Administrators can manage products, orders, and view order history.

## Table of Contents

- [Happy Pets E-Commerce Project](#happy-pets-e-commerce-project)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Steps](#steps)
  - [Usage](#usage)
  - [Admin Site](#admin-site)
  - [Project Structure](#project-structure)

## Features

- Browse products
- Add products to a shopping cart
- Place orders
- View order history
- Admin management of products, orders, and delivery status
- Stock management (prevent ordering when stock is 0)

## Installation

### Prerequisites

- Python 3.8+
- Django 3.2+
- Git

### Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/happy_pets.git
    cd happy_pets
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

- Visit the homepage at `http://127.0.0.1:8000/` to browse products.
- Add products to the cart and proceed to checkout.
- View your order history.

## Admin Site

- Access the admin site at `http://127.0.0.1:8000/admin/`.
- Log in with the superuser credentials created earlier.
- Manage products, view and manage orders, and update delivery statuses.

## Project Structure
happy_pets/
├── happy_pets/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ ├── wsgi.py
├── shop/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ │ ├── shop/
│ │ │ ├── base.html
│ │ │ ├── home.html
│ │ │ ├── product_list.html
│ │ │ ├── product_detail.html
│ │ │ ├── cart.html
│ │ │ ├── order_history.html
├── media/
├── static/
│ ├── css/
│ │ ├── styles.css
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
