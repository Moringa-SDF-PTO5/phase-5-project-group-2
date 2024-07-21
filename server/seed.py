from app import create_app
from models import db, User, Product, Category, Order, OrderItem, Address, Payment

app = create_app()

with app.app_context():
    # Drop all tables (optional, use with caution)
    # db.drop_all()

    # Create all tables
    db.create_all()

    # Create sample data
    user1 = User(username='john_doe', email='john@example.com', role='customer')
    user1.set_password('password123')

    db.session.add(user1)
    db.session.commit()

    category1 = Category(name='Electronics', description='Gadgets and devices')
    db.session.add(category1)
    db.session.commit()

    product1 = Product(
        name='Laptop',
        description='A high-performance laptop',
        price=999.99,
        category_id=category1.category_id,  # Use the correct ID
        stock_quantity=10
    )
    db.session.add(product1)
    db.session.commit()

    order1 = Order(user_id=user1.user_id, total_amount=999.99)
    db.session.add(order1)
    db.session.commit()

    order_item1 = OrderItem(order_id=order1.order_id, product_id=product1.product_id, quantity=1, price=999.99)
    db.session.add(order_item1)
    db.session.commit()

    address1 = Address(
        user_id=user1.user_id,
        street='123 Main St',
        city='Anytown',
        state='Anystate',
        postal_code='12345',
        country='USA'
    )
    db.session.add(address1)
    db.session.commit()

    payment1 = Payment(order_id=order1.order_id, amount=999.99, payment_method='Credit Card', transaction_id='txn_123456789')
    db.session.add(payment1)
    db.session.commit()

    print("Database seeded successfully!")
