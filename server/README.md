# Tech Haven

## Description

Tech Haven is a web application designed to enhance electronic gadgets selling through e-commerce. It includes functionalities for user registration, login, ordering and making purchases and payment. The backend of the application is built using Flask, a lightweight Python web framework, and it utilizes PostgreSQL as its database.

## Features

 Backend Url: <https://phase-5-project-group-2-server.onrender.com/>

* User Registration and Login: customers can register and login.
* Ordering: customer can view the product, make an order, delete order.
* Making purchases: Customer can make payment and purchases can be poted into the database.


## Tools

* Flask - Python Framework
* Database - Postgres
* Visual Studio

## Setup and Running Instructions

## 1. Prerequisites

### Install Python

Ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

Verify the installation by running:

```bash
python --version
```

### Install Visual Studio Code

* Visual Studio Code, official website: [VisualStudio.com](https://code.visualstudio.com/download)

## 2. Clone the Repository

Copy and paste the below to the Terminal

git clone <https://github.com/Moringa-SDF-PTO5/phase-5-project-group-2>

## 3. Create a Virtual Environment

Create and activate a virtual environment to manage dependencies:

Mac/Linux users;

```bash
python -m venv venv

source venv/bin/activate  
```

Windows users:

```bash
python3 -m venv venv

venv\Scripts\activate
```

## 4. Install Dependencies

Install the required dependencies using pip:

```bash
pip install psycopg-binary
```

and then install the below:

```bash
pip install -r requirements.txt
```

Then type the below to run the file

```bash
cd server
```

```bash
flask run
```

## API Endpoints

Backend Url: <https://phase-5-project-group-2-server.onrender.com/>

### Sample Usage

GET all users list
<https://phase-5-project-group-2-server.onrender.com/users>
![image](https://github.com/user-attachments/assets/c9f055fb-021b-4ce8-b960-646d7735f46f)


GET a single order_item
<https://phase-5-project-group-2-server.onrender.com/order_items/1>
![image](https://github.com/user-attachments/assets/0757d69b-1908-4a26-9881-c990d5fbb02f)


GET all products
<https://hase-5-project-group-2-server.onrender.com/products>
![image](https://github.com/user-attachments/assets/37093aee-ca3a-4a46-a854-bf24da75344b)


#### POST a purchases
<https://hase-5-project-group-2-server.onrender.com/purchases>
Ensure the body structure is as below
![image](https://github.com/user-attachments/assets/51fea25a-0cd3-43aa-8682-3ea7858d2a27)



### User Authentication

* Register: POST /register
* Login: POST /login

### user managemnt

* Create user: POST /users
* Get All Users : GET /users
* Get User by ID: GET /users/<int:user_id>
* Update User: PUT /users/<int:user_id>
* Delete User: DELETE /users/<int:user_id>

### Order Management 

* Create Order: POST /orders
* Get All Orders: GET /orders
* Get Order by ID: GET /orders/<int:order_id>
* Update Order: PUT /orders/<int:order_id>
* Delete Order: DELETE /orders/<int:order_id>

### Product Management

* Create Product: POST /products
* Get All Products: GET /products
* Get Products by ID: GET /products/<int:product_id>
* Update Product: PUT /products/<int:product_id>
* Delete Product: DELETE /products/<int:product_id>

### Category Management

* Create Category: POST /categories
* Get All Categories: GET /categories
* Get Category by ID: GET /categories/<int:category_id>
* Update Category: PUT /categories/<int:category_id>
* Delete Category: DELETE /categories/<int:category_id>

### OrderItem Management

* Create OrderItem: POST /order_items
* Get OrderItem by ID: GET /order_items/<int:order_item_id>
* Update Category: PUT /order_items/<int:order_item_id>
* Delete Category: DELETE /order_items/<int:order_item_id>

### Payment Management

* Create Payment: POST /payments
* Get All Payments: GET /payments
* Get payment by ID: GET /payments/<int:payment_id>
* Update Payment: PUT /payments/<int:payment_id>
* Delete Payment: DELETE /payments/<int:payment_id>

### Address Management

* Create Address: POST /addresses
* Get All Addresses: GET /addresses
* Get Address by ID: GET /addresses/<int:address_id>
* Update Address: PUT /addresses/<int:address_id>
* Delete Address: DELETE /addresses/<int:address_id>

### Staff Management

* Create Staff: POST /staffs
* Get All Staff: GET /staffs
* Get Staff by ID: GET /staffs/<int:staff_id>
* Update Staff: PUT /staffs/<int:staff_id>
* Delete Staff: DELETE /staffs/<int:staff_id>

### Purchas Management

* Create Purchase: POST /purchases
* Get All Purchases: GET /purchases
* Get Purchase by ID: GET /purchases/<int:purchase_id>
* Update Purchase: PUT /purchases/<int:purchase_id>
* Delete Purchase: DELETE /purchases/<int:purchase_id>


## Project Contributors 
* Rosalia Njoki
* Mary Njoroge 
* George Kiarie
* Alfred Oriri
* Gregory Kago


## License

Copyright © 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
