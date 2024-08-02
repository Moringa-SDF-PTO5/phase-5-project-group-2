from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User, Staff, Product, Category, Order, OrderItem, Address, Payment, Purchase

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://group2_electronics_pdb_user:KiuZM4dGNILp4vYJTnZSeqhhtx6NYTef@dpg-cqj4968gph6c73912uvg-a.frankfurt-postgres.render.com/group2_electronics_pdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configure CORS
    CORS(app, resources={r"/*": {"origins": "*"}})
    db.init_app(app)
    migrate = Migrate(app, db)
    return app

app = create_app()

@app.route('/')
def index():
    return jsonify({"message": "Welcome to Our Electronic Shop!"})

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"message": "Invalid JSON data"}), 400
        
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username or not email or not password:
            return jsonify({'message': 'Missing required fields'}), 400
        
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            return jsonify({'message': 'User already exists'}), 409
        
        new_user = User(username=username, email=email, password=password)
    
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    
    except Exception as e:
        return jsonify({"message": "An error occurred", "error": str(e)}), 500

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    if 'username' in data:
        user.username = data['username']
    if 'password' in data:
        user.password = data['password']
    if 'email' in data:
        user.email = data['email']
    if 'role' in data:
        user.role = data['role']

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred. Please check your input data.'}), 400

    return jsonify(user.to_dict())

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    try:
        db.session.delete(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred. Please check your input data.'}), 400

    return jsonify({'message': 'User deleted successfully'})        

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        return jsonify({'user_id': user.user_id, 'username': user.username, 'email': user.email, 'role': user.role}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# Staff endpoints
@app.route('/staffs', methods=['POST'])
def add_staff():
    data = request.json
    new_staff = Staff(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        role=data.get('role'),
        staff_number=data['staff_number']
    )
    db.session.add(new_staff)
    db.session.commit()
    return jsonify(new_staff.to_dict()), 201

@app.route('/staffs', methods=['GET'])
def get_staff():
    staffs = Staff.query.all()
    return jsonify([staff.to_dict() for staff in staffs])

@app.route('/staffs/<int:staff_id>', methods=['GET'])
def get_staff_by_id(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    return jsonify(staff.to_dict())

@app.route('/staffs/<int:staff_id>', methods=['PUT'])
def update_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    data = request.json
    staff.first_name = data.get('first_name', staff.first_name)
    staff.last_name = data.get('last_name', staff.last_name)
    staff.email = data.get('email', staff.email)
    staff.role = data.get('role', staff.role)
    staff.staff_number = data.get('staff_number', staff.staff_number) 
    db.session.commit()
    return jsonify(staff.to_dict())

@app.route('/staffs/<int:staff_id>', methods=['DELETE'])
def delete_staff(staff_id):
    staff = Staff.query.get_or_404(staff_id)
    db.session.delete(staff)
    db.session.commit()
    return '', 204

# Category endpoints
@app.route('/categories', methods=['POST'])
def create_category():
    try:
        data = request.get_json()
        category_name = data.get('category_name')
        description = data.get('description')
        
        if not category_name:
            return jsonify({'message': 'Category name is required'}), 400
        
        new_category = Category(category_name=category_name, description=description)
        db.session.add(new_category)
        db.session.commit()
        
        return jsonify(new_category.to_dict()), 201
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories]), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        return jsonify(category.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories/<int:category_id>', methods=['PUT'])
def update_category(category_id):
    try:
        data = request.get_json()
        category = Category.query.get_or_404(category_id)
        
        category_name = data.get('category_name')
        description = data.get('description')
        
        if category_name:
            category.category_name = category_name
        if description is not None:
            category.description = description
        
        db.session.commit()
        
        return jsonify(category.to_dict()), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def delete_category(category_id):
    try:
        category = Category.query.get_or_404(category_id)
        db.session.delete(category)
        db.session.commit()
        
        return jsonify({'message': 'Category deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

# Product endpoints
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

    if 'name' in data:
        product.name = data['name']
    if 'image' in data:
        product.image = data['image']
    if 'description' in data:
        product.description = data['description']
    if 'price' in data:
        product.price = data['price']
    if 'category_id' in data:
        product.category_id = data['category_id']
    if 'category_name' in data:
        product.category_name = data['category_name']    
    if 'stock_quantity' in data:
        product.stock_quantity = data['stock_quantity']
    
    db.session.commit()
    return jsonify(product.to_dict()), 200

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'}), 200

@app.route('/cart', methods=['GET'])
def get_cart():
    user_id = request.args.get('user_id')
    cart_items = OrderItem.query.filter_by(user_id=user_id).all()
    return jsonify([item.to_dict() for item in cart_items]), 200


# Order endpoints
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    result = [order.to_dict() for order in orders]
    return jsonify(result), 200

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    return jsonify(order.to_dict()), 200

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    user_id = data['user_id']
    total_amount = data['total_amount']
    status = data['status']
    address_id = data['address_id']
    payment_id = data['payment_id']
    
    new_order = Order(user_id=user_id, total_amount=total_amount, status=status, address_id=address_id, payment_id=payment_id)
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.to_dict()), 201

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.get_json()
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404

    if 'total_amount' in data:
        order.total_amount = data['total_amount']
    if 'status' in data:
        order.status = data['status']
    if 'address_id' in data:
        order.address_id = data['address_id']
    if 'payment_id' in data:
        order.payment_id = data['payment_id']
    
    db.session.commit()
    return jsonify(order.to_dict()), 200

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'message': 'Order not found'}), 404
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({'message': 'Order deleted successfully'}), 200

@app.route('/order_items/<int:order_item_id>', methods=['GET'])
def get_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404
    return jsonify(order_item.to_dict()), 200

@app.route('/order_items', methods=['POST'])
def add_order_item():
    data = request.get_json()
    order_id = data['order_id']
    product_id = data['product_id']
    quantity = data['quantity']
    price = data['price']
    
    new_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity, price=price)
    db.session.add(new_order_item)
    db.session.commit()
    return jsonify(new_order_item.to_dict()), 201

@app.route('/order_items/<int:order_item_id>', methods=['PUT'])
def update_order_item(order_item_id):
    data = request.get_json()
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404

    if 'order_id' in data:
        order_item.order_id = data['order_id']
    if 'product_id' in data:
        order_item.product_id = data['product_id']
    if 'quantity' in data:
        order_item.quantity = data['quantity']
    if 'price' in data:
        order_item.price = data['price']
    
    db.session.commit()
    return jsonify(order_item.to_dict()), 200

@app.route('/order_items/<int:order_item_id>', methods=['DELETE'])
def delete_order_item(order_item_id):
    order_item = OrderItem.query.get(order_item_id)
    if not order_item:
        return jsonify({'message': 'Order item not found'}), 404
    
    db.session.delete(order_item)
    db.session.commit()
    return jsonify({'message': 'Order item deleted successfully'}), 200

@app.route('/addresses', methods=['GET'])
def get_addresses():
    addresses = Address.query.all()
    result = [address.to_dict() for address in addresses]
    return jsonify(result), 200

@app.route('/addresses/<int:address_id>', methods=['GET'])
def get_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404
    return jsonify(address.to_dict()), 200

@app.route('/addresses', methods=['POST'])
def add_address():
    data = request.get_json()
    user_id = data['user_id']
    street = data['street']
    city = data['city']
    state = data['state']
    postal_code = data['postal_code']
    country = data['country']
    
    new_address = Address(user_id=user_id, street=street, city=city, state=state, postal_code=postal_code, country=country)
    db.session.add(new_address)
    db.session.commit()
    return jsonify(new_address.to_dict()), 201

@app.route('/addresses/<int:address_id>', methods=['PUT'])
def update_address(address_id):
    data = request.get_json()
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404

    if 'user_id' in data:
        address.user_id = data['user_id']
    if 'street' in data:
        address.street = data['street']
    if 'city' in data:
        address.city = data['city']
    if 'state' in data:
        address.state = data['state']
    if 'postal_code' in data:
        address.postal_code = data['postal_code']
    if 'country' in data:
        address.country = data['country']
    
    db.session.commit()
    return jsonify(address.to_dict()), 200

@app.route('/addresses/<int:address_id>', methods=['DELETE'])
def delete_address(address_id):
    address = Address.query.get(address_id)
    if not address:
        return jsonify({'message': 'Address not found'}), 404
    
    db.session.delete(address)
    db.session.commit()
    return jsonify({'message': 'Address deleted successfully'}), 200

@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    result = [payment.to_dict() for payment in payments]
    return jsonify(result), 200

@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    return jsonify(payment.to_dict()), 200

@app.route('/payments', methods=['POST'])
def add_payment():
    data = request.get_json()
    user_id = data['user_id']
    order_id = data['order_id']
    amount = data['amount']
    payment_method = data['payment_method']
    payment_date = data['payment_date']
    
    new_payment = Payment(user_id=user_id, order_id=order_id, amount=amount, payment_method=payment_method, payment_date=payment_date)
    db.session.add(new_payment)
    db.session.commit()
    return jsonify(new_payment.to_dict()), 201

@app.route('/payments/<int:payment_id>', methods=['PUT'])
def update_payment(payment_id):
    data = request.get_json()
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404

    if 'user_id' in data:
        payment.user_id = data['user_id']
    if 'order_id' in data:
        payment.order_id = data['order_id']
    if 'amount' in data:
        payment.amount = data['amount']
    if 'payment_method' in data:
        payment.payment_method = data['payment_method']
    if 'payment_date' in data:
        payment.payment_date = data['payment_date']
    
    db.session.commit()
    return jsonify(payment.to_dict()), 200

@app.route('/payments/<int:payment_id>', methods=['DELETE'])
def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({'message': 'Payment not found'}), 404
    
    db.session.delete(payment)
    db.session.commit()
    return jsonify({'message': 'Payment deleted successfully'}), 200


@app.route('/purchases/<int:purchase_id>', methods=['GET'])
def get_purchase(purchase_id):
    purchase = Purchase.query.get(purchase_id)
    if not purchase:
        return jsonify({'error': 'Purchase not found'}), 404
    return jsonify(purchase.to_dict())

@app.route('/purchases', methods=['GET'])
def get_purchases():
    purchases = Purchase.query.all()
    return jsonify([purchase.to_dict() for purchase in purchases])

@app.route('/purchases/<int:purchase_id>', methods=['PUT'])
def update_purchase(purchase_id):
    data = request.json
    purchase = Purchase.query.get(purchase_id)
    if not purchase:
        return jsonify({'error': 'Purchase not found'}), 404
    
    if 'order_id' in data:
        purchase.order_id = data['order_id']
    if 'product_id' in data:
        product_id = data['product_id']
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        purchase.product_id = product_id
        purchase.total_price = product.price * purchase.quantity
    if 'quantity' in data:
        purchase.quantity = data['quantity']
        purchase.total_price = purchase.product.price * purchase.quantity
    if 'total_price' in data:
        purchase.total_price = data['total_price']

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred. Please check your input data.'}), 400

    return jsonify(purchase.to_dict())

@app.route('/purchases/<int:purchase_id>', methods=['DELETE'])
def delete_purchase(purchase_id):
    purchase = Purchase.query.get(purchase_id)
    if not purchase:
        return jsonify({'error': 'Purchase not found'}), 404
    
    try:
        db.session.delete(purchase)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error occurred. Please check your input data.'}), 400

    return jsonify({'message': 'Purchase deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)       