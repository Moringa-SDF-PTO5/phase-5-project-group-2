from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from server import app, db 
import os

# Initialize global objects
db = SQLAlchemy()
migrate = Migrate(app, db)



def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'postgresql://username:password@localhost/dbname')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models within create_app to avoid circular imports
    from models import User, Product, Category, Order, OrderItem, Address, Payment

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

    @app.route('/products', methods=['GET'])
    def get_products():
        products = Product.query.all()
        result = [product.to_dict() for product in products]
        return jsonify(result), 200

    @app.route('/products/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'message': 'Product not found'}), 404
        return jsonify(product.to_dict()), 200

    @app.route('/products', methods=['POST'])
    def add_product():
        data = request.get_json()
        name = data['name']
        image = data['image']
        description = data['description']
        price = data['price']
        category_id = data['category_id']
        stock_quantity = data['stock_quantity']

        new_product = Product(name=name, image=image, description=description, price=price, category_id=category_id, stock_quantity=stock_quantity)
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201

    @app.route('/products/<int:product_id>', methods=['PUT'])
    def update_product(product_id):
        data = request.get_json()
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'message': 'Product not found'}), 404

        product.name = data['name']
        product.image = data['image']
        product.description = data['description']
        product.price = data['price']
        product.category_id = data['category_id']
        product.stock_quantity = data['stock_quantity']
        db.session.commit()
        return jsonify(product.to_dict()), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001, debug=True)
