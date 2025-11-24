Coffee Shop Domain Modeling

This project models a Coffee Shop domain using Object-Oriented Programming principles in Python.
It includes three main classes — Customer, Coffee, and Order — implementing a many-to-many relationship through domain modeling, validations, aggregation methods, and test coverage using pytest.

📂 Folder Structure
coffee_shop/
│
├── customer.py
├── coffee.py
├── order.py
├── utils.py
├── debug.py
│
├── tests/
│   ├── test_customer.py
│   ├── test_coffee.py
│   ├── test_order.py
│   └── conftest.py
│
├── Pipfile
├── Pipfile.lock
└── README.md

📘 Project Overview

This project demonstrates:

Designing Python classes from scratch

Implementing instance methods, class methods, and properties

Enforcing data validation and raising exceptions

Avoiding circular imports

Modeling one-to-many and many-to-many relationships

Writing unit tests using pytest

Maintaining clean code following PEP 8 principles

🧱 Domain Model
Customer

Has a validated name (1–15 chars)

Can have many orders

Can access all coffees they have ordered

Can create a new order

Can determine who spent the most on a specific coffee (most_aficionado)

Coffee

Has a validated name (at least 3 chars)

Has many orders

Can list customers who ordered it

Can compute:

number of orders

average price

Order

Belongs to one Customer and one Coffee

Has price validated between 1.0 and 10.0

Exists only when customer & coffee are provided

🚀 Installation & Setup
1. Clone or create your project
mkdir coffee_shop
cd coffee_shop

2. Create virtual environment
pipenv install
pipenv shell

3. Install pytest
pipenv install pytest

🛠 Running the Project
Debug Mode

Use the provided interactive script:

python debug.py


This demonstrates:

Creating customers & coffees

Creating valid & invalid orders

Running queries

Seeing exceptions raised for invalid inputs

🧪 Running Tests

Run all tests:

pytest

✔️ Validations & Exceptions

The app raises exceptions for invalid data:

Examples:

Customer name too long → ValueError

Coffee name too short → ValueError

Price outside range → ValueError

Price not numeric → TypeError

Validation logic is stored in utils.py to avoid duplication.

🔧 Debugging & Development Notes

All circular imports are solved using lazy imports inside methods.

Reusable validation logic is in utils.py

Code follows PEP 8 naming and formatting rules

debug.py resets the system state for each run

⭐ Bonus Features Implemented

Detailed README (this file)

Organized folder structure

Test suite for all classes

Helper validation module

Exception handling throughout the system

📄 License

This project is for educational use at Moringa School – Phase 3 Python OOP.

🙌 Author
Joshua Imbusi
Python Developer – Moringa School