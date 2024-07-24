from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from models import db, User, Product, Category, Order, OrderItem, Address, Payment
import os

# Helper function to get an object or return a 404 error
def get_or_404(model, id):
    obj = model.query.get(id)
    if obj is None:
        abort(404, description=f'{model.__name__} not found')
    return obj

def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://group2_electronics_project_user:wYWHOsnDi3EgTzVU0hVb2c7Zt4Fej1wC@dpg-cqch7lmehbks738g4k80-a.frankfurt-postgres.render.com/group2_electronics_project')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        return jsonify({"message": "Hello, World!"})

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 409

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            return jsonify(user.to_dict()), 200
        return jsonify({'message': 'Invalid credentials'}), 401

    # User routes
    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.json
        user = User(username=data['username'], email=data['email'], role=data.get('role', 'customer'))
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201

    @app.route('/users/<int:user_id>', methods=['GET'])
    def read_user(user_id):
        user = get_or_404(User, user_id)
        return jsonify(user.to_dict())

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = get_or_404(User, user_id)
        data = request.json
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        user.role = data.get('role', user.role)
        if 'password' in data:
            user.set_password(data['password'])
        db.session.commit()
        return jsonify(user.to_dict())

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = get_or_404(User, user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204

    # Product routes
    @app.route('/products', methods=['POST'])
    def create_product():
        data = request.json
        product = Product(
            name=data['name'],
            image=data['image'],
            description=data.get('description'),
            price=data['price'],
            category_id=data['category_id'],
            stock_quantity=data['stock_quantity']
        )
        db.session.add(product)
        db.session.commit()
        return jsonify(product.to_dict()), 201

    @app.route('/products/<int:product_id>', methods=['GET'])
    def read_product(product_id):
        product = get_or_404(Product, product_id)
        return jsonify(product.to_dict())

    @app.route('/products/<int:product_id>', methods=['PUT'])
    def update_product(product_id):
        product = get_or_404(Product, product_id)
        data = request.json
        product.name = data.get('name', product.name)
        product.image = data.get('image', product.image)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.category_id = data.get('category_id', product.category_id)
        product.stock_quantity = data.get('stock_quantity', product.stock_quantity)
        db.session.commit()
        return jsonify(product.to_dict())

    @app.route('/products/<int:product_id>', methods=['DELETE'])
    def delete_product(product_id):
        product = get_or_404(Product, product_id)
        db.session.delete(product)
        db.session.commit()
        return '', 204

    # Category routes
    @app.route('/categories', methods=['POST'])
    def create_category():
        data = request.json
        category = Category(name=data['name'], description=data.get('description'))
        db.session.add(category)
        db.session.commit()
        return jsonify(category.to_dict()), 201

    @app.route('/categories/<int:category_id>', methods=['GET'])
    def read_category(category_id):
        category = get_or_404(Category, category_id)
        return jsonify(category.to_dict())

    @app.route('/categories/<int:category_id>', methods=['PUT'])
    def update_category(category_id):
        category = get_or_404(Category, category_id)
        data = request.json
        category.name = data.get('name', category.name)
        category.description = data.get('description', category.description)
        db.session.commit()
        return jsonify(category.to_dict())

    @app.route('/categories/<int:category_id>', methods=['DELETE'])
    def delete_category(category_id):
        category = get_or_404(Category, category_id)
        db.session.delete(category)
        db.session.commit()
        return '', 204

    # Order routes
    @app.route('/orders', methods=['POST'])
    def create_order():
        data = request.json
        order = Order(
            user_id=data['user_id'],
            total_amount=data['total_amount'],
            status=data.get('status', 'pending')
        )
        db.session.add(order)
        db.session.commit()
        return jsonify(order.to_dict()), 201

    @app.route('/orders/<int:order_id>', methods=['GET'])
    def read_order(order_id):
        order = get_or_404(Order, order_id)
        return jsonify(order.to_dict())

    @app.route('/orders/<int:order_id>', methods=['PUT'])
    def update_order(order_id):
        order = get_or_404(Order, order_id)
        data = request.json
        order.user_id = data.get('user_id', order.user_id)
        order.total_amount = data.get('total_amount', order.total_amount)
        order.status = data.get('status', order.status)
        db.session.commit()
        return jsonify(order.to_dict())

    @app.route('/orders/<int:order_id>', methods=['DELETE'])
    def delete_order(order_id):
        order = get_or_404(Order, order_id)
        db.session.delete(order)
        db.session.commit()
        return '', 204

    # OrderItem routes
    @app.route('/order-items', methods=['POST'])
    def create_order_item():
        data = request.json
        order_item = OrderItem(
            order_id=data['order_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            price=data['price']
        )
        db.session.add(order_item)
        db.session.commit()
        return jsonify(order_item.to_dict()), 201

    @app.route('/order-items/<int:order_item_id>', methods=['GET'])
    def read_order_item(order_item_id):
        order_item = get_or_404(OrderItem, order_item_id)
        return jsonify(order_item.to_dict())

    @app.route('/order-items/<int:order_item_id>', methods=['PUT'])
    def update_order_item(order_item_id):
        order_item = get_or_404(OrderItem, order_item_id)
        data = request.json
        order_item.order_id = data.get('order_id', order_item.order_id)
        order_item.product_id = data.get('product_id', order_item.product_id)
        order_item.quantity = data.get('quantity', order_item.quantity)
        order_item.price = data.get('price', order_item.price)
        db.session.commit()
        return jsonify(order_item.to_dict())

    @app.route('/order-items/<int:order_item_id>', methods=['DELETE'])
    def delete_order_item(order_item_id):
        order_item = get_or_404(OrderItem, order_item_id)
        db.session.delete(order_item)
        db.session.commit()
        return '', 204

    # Payment routes
    @app.route('/payments', methods=['POST'])
    def create_payment():
        data = request.json
        payment = Payment(
            order_id=data['order_id'],
            amount=data['amount'],
            payment_method=data['payment_method'],
            transaction_id=data.get('transaction_id')
        )
        db.session.add(payment)
        db.session.commit()
        return jsonify(payment.to_dict()), 201

    @app.route('/payments/<int:payment_id>', methods=['GET'])
    def read_payment(payment_id):
        payment = get_or_404(Payment, payment_id)
        return jsonify(payment.to_dict())

    @app.route('/payments/<int:payment_id>', methods=['PUT'])
    def update_payment(payment_id):
        payment = get_or_404(Payment, payment_id)
        data = request.json
        payment.order_id = data.get('order_id', payment.order_id)
        payment.amount = data.get('amount', payment.amount)
        payment.payment_method = data.get('payment_method', payment.payment_method)
        payment.transaction_id = data.get('transaction_id', payment.transaction_id)
        db.session.commit()
        return jsonify(payment.to_dict())

    @app.route('/payments/<int:payment_id>', methods=['DELETE'])
    def delete_payment(payment_id):
        payment = get_or_404(Payment, payment_id)
        db.session.delete(payment)
        db.session.commit()
        return '', 204

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
