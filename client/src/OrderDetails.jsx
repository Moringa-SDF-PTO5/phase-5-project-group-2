import React from 'react';
import './OrderDetails.css';
import Navbar from './NavBar';
import Footer from './footer';

const OrderDetails = () => {
  const orderItems = [
    { id: 1, name: 'Item 1', quantity: 1, price: '$10' },
    { id: 2, name: 'Item 2', quantity: 2, price: '$20' },
  ];

  return (
    <div>
      <Navbar />
      <div className="order-details">
        <h1>Order Details</h1>
        <ul>
          {orderItems.map(item => (
            <li key={item.id}>
              <span>{item.name}</span> - <span>{item.quantity}</span> x <span>{item.price}</span>
            </li>
          ))}
        </ul>
      </div>
      <footer />
    </div>
  );
};

export default OrderDetails;
