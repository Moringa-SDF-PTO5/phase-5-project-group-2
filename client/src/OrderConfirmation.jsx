import React from 'react';
import './OrderConfirmation.css';
import Navbar from './NavBar';
import Footer from './footer';

const OrderConfirmation = () => {
  return (
    <div>
      <Navbar />
    <div className="order-confirmation">
      <h1>Thank You!</h1>
      <p>We are getting started on your order right away, and you will receive an order confirmation shortly via your email.</p>

      <div className="order-status">
        <h2>ORDER STATUS</h2>
        <p>Delivery pending</p>
      </div>

      <button className="view-order-button">VIEW ORDER CONFIRMATION</button>

    </div>
    <Footer />
    </div>
  );
};

export default OrderConfirmation;
