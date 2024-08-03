import React, { useContext } from 'react';
import { AppContext } from './AppContext';
import './OrderDetails.css';
import Navbar from './NavBar';
import Footer from './footer';

const OrderDetails = () => {
    const { cartItems } = useContext(AppContext);
    console.log(cartItems)
    const calculateSubtotal = () => {
        return cartItems.reduce((acc, item) => acc + item.price * item.quantity, 0);
    };
    

    return (
        <div>
            <Navbar />
            <div className="order-details">
                <h2>Order Details</h2>
                <table className="order-details-table">
                    <thead>
                        <tr>
                            <th>Product Image</th>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Price</th>
                        </tr>
                    </thead>
                    <tbody>
                        {cartItems.map((item, index) => (
                            <tr key={index}>
                                <td><img src={item.image} alt={item.name} /></td>
                                <td>{item.name}</td>
                                <td>{item.quantity}</td>
                                <td>${(item.price * item.quantity).toFixed(2)}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                <div className="order-summary">
                    <p>Subtotal: ${calculateSubtotal().toFixed(2)}</p>
                    <p>Shipping: Free</p>
                    <p>Total: ${calculateSubtotal().toFixed(2)}</p>
                </div>
            </div>
            <footer />
        </div>
    );
};

export default OrderDetails;
