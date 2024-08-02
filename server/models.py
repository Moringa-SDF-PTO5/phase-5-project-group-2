from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20), default='customer')

    orders = db.relationship('Order', back_populates='user', lazy=True)
    addresses = db.relationship('Address', back_populates='user', lazy=True)

    orders = db.relationship('Order', back_populates='user', lazy=True)
    addresses = db.relationship('Address', back_populates='user', lazy=True)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'role': self.role,
        }

class Staff(db.Model):
    __tablename__ = 'staffs'
    staff_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(20))

    def to_dict(self):
        return {
            'staff_id': self.staff_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'role': self.role,
        }

class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    image = db.Column(db.String(200))
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)

    category = db.relationship('Category', back_populates='products')
    order_items = db.relationship('OrderItem', back_populates='product')

    def to_dict(self):
        return {
            'product_id': self.product_id,
            'name': self.name,
            'image': self.image,
            'description': self.description,
            'price': self.price,
            'category_id': self.category_id,
            'category_name': self.category.category_name,
            'stock_quantity': self.stock_quantity
            
        }

class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(120), nullable=False)
    category_name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)

    products = db.relationship('Product', back_populates='category')

    products = db.relationship('Product', back_populates='category')

    def to_dict(self):
        return {
            'category_id': self.category_id,
            'category_name': self.category_name,
            'category_name': self.category_name,
            'description': self.description,
        }

class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default='pending')

    user = db.relationship('User', back_populates='orders')
    order_items = db.relationship('OrderItem', back_populates='order')
    payments = db.relationship('Payment', back_populates='order')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'total_amount': self.total_amount,
            'status': self.status,
        }
          
class OrderItem(db.Model):
    __tablename__ = 'order_items'
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship('Order', back_populates='order_items')
    product = db.relationship('Product', back_populates='order_items')

    order = db.relationship('Order', back_populates='order_items')
    product = db.relationship('Product', back_populates='order_items')

    def to_dict(self):
        return {
            'order_item_id': self.order_item_id,
            'order_id': self.order_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.price,
        }

class Address(db.Model):
    __tablename__ = 'addresses'
    address_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', back_populates='addresses')

    def to_dict(self):
        return {
            'address_id': self.address_id,
            'user_id': self.user_id,
            'street': self.street,
            'city': self.city,
            'state': self.state,
            'postal_code': self.postal_code,
            'country': self.country,
        }

class Payment(db.Model):
    __tablename__ = 'payments'
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    transaction_id = db.Column(db.String(100), unique=True)

    order = db.relationship('Order', back_populates='payments')

    def to_dict(self):
        return {
            'payment_id': self.payment_id,
            'order_id': self.order_id,
            'amount': self.amount,
            'payment_method': self.payment_method,
            'transaction_id': self.transaction_id,
        }
