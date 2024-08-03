import React from 'react';
import { useNavigate } from 'react-router-dom';
import './OrderConfirmation.css';
import Navbar from './NavBar';
import Footer from './footer';

const OrderConfirmation = () => {

  const navigate = useNavigate();

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

      <button className="view-order-button" onClick={() => navigate('/confirmation')}>VIEW ORDER CONFIRMATION</button>
      <div className="confirmation-buttons">
          <button className="continue-shopping-button" onClick={() => navigate('/')}>Continue Shopping</button>
        </div>

    </div>
    <Footer />
    </div>
  );
};

export default OrderConfirmation;
