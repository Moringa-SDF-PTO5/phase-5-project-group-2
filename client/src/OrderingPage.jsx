import React, { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AppContext } from './AppContext';
import './OrderingPage.css';
import Navbar from './NavBar';

const OrderingPage = () => {
    const { cartItems, clearCart, removeItem, updateQuantity } = useContext(AppContext);
    const [paymentMethod, setPaymentMethod] = useState('Credit Card');
    const [cardDetails, setCardDetails] = useState({ cardName: '', cardNumber: '', expirationDate: '', cvv: '' });
    const navigate = useNavigate();

    const calculateSubtotal = () => {
        return cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
    };

    const handlePaymentMethodChange = (e) => {
        setPaymentMethod(e.target.value);
    };

    const handleCardDetailsChange = (e) => {
        const { name, value } = e.target;
        setCardDetails(prevDetails => ({ ...prevDetails, [name]: value }));
    };

    const handleCheckout = () => {
        alert('Checkout Successful!');
        
        navigate('/confirmation'); // Replace with your confirmation route
    };

    return (
        <div>
            <Navbar />
            <div className="ordering-page">
                <div className="cart-items">
                    <h2>Shopping Cart</h2>
                    <div className="cart-header">
                    <div className="header-item header-product">Product Image</div>
                        <div className="header-item header-product">Product</div>
                        <div className="header-item header-quantity">Quantity</div>
                        <div className="header-item header-price">Total Price</div>
                        <div className="header-item header-remove">Clear All</div>
                    </div>
                    {cartItems.map((item, index) => (
                        <div key={index} className="cart-item">
                            <div className="item-image">
                                <img src={item.image} alt={item.name} />
                            </div>
                            <div className="item-name">
                                <h3>{item.name}</h3>
                            </div>
                            <div className="item-quantity">
                                <button onClick={() => updateQuantity(item.product_id, item.quantity - 1)}>-</button>
                                <span>{item.quantity}</span>
                                <button onClick={() => updateQuantity(item.product_id, item.quantity + 1)}>+</button>
                            </div>
                            <div className="item-price">
                                <p>${(item.price * item.quantity).toFixed(2)}</p>
                            </div>
                            <div className="item-remove">
                                <button onClick={() => removeItem(item.product_id)}>X</button>
                            </div>
                        </div>
                    ))}
                    
                    <div className="order-summary">
                        <p>Subtotal: ${calculateSubtotal().toFixed(2)}</p>
                        <p>Shipping: Free</p>
                        <p>Total: ${calculateSubtotal().toFixed(2)}</p>
                    </div>
                </div>

                <div className="payment-billing">
    <h2>Payment & Billing</h2>
    <h3>Payment Method</h3>
    <label>
        <input 
            type="radio" 
            value="Google Pay" 
            checked={paymentMethod === 'Google Pay'} 
            onChange={handlePaymentMethodChange} 
        />
        <img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fuxwing.com%2Fgoogle-pay-acceptance-mark-icon%2F&psig=AOvVaw085King9OO0It8AOU0fiPx&ust=1722594769678000&source=images&cd=vfe&opi=89978449&ved=0CA8QjRxqFwoTCPjn3-jL04cDFQAAAAAdAAAAABAE"  /> {/* Add Google Pay icon */}
        Google Pay
    </label>
    <label>
        <input 
            type="radio" 
            value="Credit Card" 
            checked={paymentMethod === 'Credit Card'} 
            onChange={handlePaymentMethodChange} 
        />
        <img src=""  /> {/* Add Credit Card icon */}
        Credit Card
    </label>

    {paymentMethod === 'Credit Card' && (
        <div className="card-details">
            <label>
                Name On Card:
                <input 
                    type="text" 
                    name="cardName" 
                    placeholder="Enter name on card" 
                    value={cardDetails.cardName} 
                    onChange={handleCardDetailsChange} 
                />
            </label>
            <label>
                Card Number:
                <input 
                    type="text" 
                    name="cardNumber" 
                    placeholder="Enter card number" 
                    value={cardDetails.cardNumber} 
                    onChange={handleCardDetailsChange} 
                />
            </label>
            <div className="expiration-cvv">
                <label>
                    Expiration Date:
                    <input 
                        type="text" 
                        name="expirationDate" 
                        placeholder="MM/YY" 
                        value={cardDetails.expirationDate} 
                        onChange={handleCardDetailsChange} 
                    />
                </label>
                <label>
                    CVV:
                    <input 
                        type="text" 
                        name="cvv" 
                        placeholder="CVV" 
                        value={cardDetails.cvv} 
                        onChange={handleCardDetailsChange} 
                    />
                </label>
            </div>
            <button className="button-checkout" onClick={handleCheckout}>Check Out</button>
        </div>
    )}
        

                </div>
            </div>
        </div>
    );
};

export default OrderingPage;
