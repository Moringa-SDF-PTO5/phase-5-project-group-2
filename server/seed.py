# seed.py
from app import create_app
from models import db, User, Product, Category, Order, OrderItem, Address, Payment

app = create_app()

# Initialize the database and create tables
with app.app_context():
    db.drop_all()  # Drops all tables, useful if you want a clean start
    db.create_all()  # Creates all tables

    # Create sample data

    # Users
    user1 = User(username='john_doe', email='john@example.com', role='customer')
    user1.set_password('password123')  # Set hashed password

    user2 = User(username='jane_smith', email='jane@example.com', role='customer')
    user2.set_password('securepass456')

    # Categories
    category1 = Category(name='Electronics', description='Gadgets and devices')
   

    # Products
    product1 = Product(name='Laptop', image='laptop.jpg', description='High-performance laptop', price=999.99, category=category1, stock_quantity=10)
    product2 = Product(name='Smartphone', image='smartphone.jpg', description='Latest model smartphone', price=699.99, category=category1, stock_quantity=25)
    

    # Orders
    order1 = Order(user=user1, total_amount=1719.97, status='pending')

    # Order Items
    order_item1 = OrderItem(order=order1, product=product1, quantity=1, price=999.99)
    order_item2 = OrderItem(order=order1, product=product2, quantity=1, price=699.99)
    order_item3 = OrderItem(order=order1, product=product3, quantity=1, price=19.99)

    # Addresses
    address1 = Address(user=user1, street='123 Main St', city='Metropolis', state='CA', postal_code='12345', country='USA')
    address2 = Address(user=user2, street='456 Elm St', city='Gotham', state='NY', postal_code='67890', country='USA')

    # Payments
    payment1 = Payment(order=order1, amount=1719.97, payment_method='Credit Card', transaction_id='TX123456789')

    # Add instances to the session
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(category1)

    db.session.add(product1)
    db.session.add(product2)
   
    db.session.add(order1)
    db.session.add(order_item1)
    db.session.add(order_item2)
    db.session.add(order_item3)
    db.session.add(address1)
    db.session.add(address2)
    db.session.add(payment1)

    # Commit the session
    db.session.commit()

    print("Database seeded successfully!")
