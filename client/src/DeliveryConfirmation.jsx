import React, { useEffect, useState } from 'react';
import './DeliveryConfirmation.css';

const DeliveryConfirmation = () => {
  const [orderItems, setOrderItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/order_items') // Ensure this URL matches your Flask backend URL
      .then(response => response.json())
      .then(data => setOrderItems(data))
      .catch(error => console.error('Error fetching order items:', error));
  }, []);

  return (
    <div className="delivery-confirmation">
      <h1>Delivery Confirmation</h1>
      <div className="products">
        {orderItems.map(item => (
          <div key={item.id} className="product">
            <h2>{item.name}</h2>
            <p>{item.description}</p>
            <p>Price: ${item.price}</p>
            <p>
              Seller Confirmation: {item.isConfirmed ? 'Confirmed' : 'Pending'}
            </p>
          </div>
        ))}
      </div>
      <footer className="footer">
        <div className="contact-info">
          <h3>Contact</h3>
          <p>+2547123456789</p>
        </div>
        <div className="address">
          <h3>Physical Address</h3>
          <p>Luthuli Street, Nairobi</p>
          <p>TECH HAVEN</p>
        </div>
      </footer>
    </div>
  );
};

export default DeliveryConfirmation;
