import React, { useEffect, useState } from 'react';
import Navbar from './NavBar';
import Footer from './footer';
// import './DeliveryConfirmation.css';

const DeliveryConfirmation = () => {
  const [orderItems, setOrderItems] = useState([]);

  useEffect(() => {
<<<<<<< HEAD
    fetch('http://localhost:5000/api/order_items') // Ensure this URL matches your Flask backend URL
=======
    fetch('http://localhost:5000/api/products') 
>>>>>>> e66ba8c929c93b78251d1a4a5b82b0dfd0dd6d9c
      .then(response => response.json())
      .then(data => setOrderItems(data))
      .catch(error => console.error('Error fetching order items:', error));
  }, []);

  return (
    <div>
    <Navbar />
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
    </div>
    <Footer />
    </div>
  );
};

export default DeliveryConfirmation;
