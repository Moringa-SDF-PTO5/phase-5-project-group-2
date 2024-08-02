import React, { useEffect, useState } from 'react';
import Navbar from './NavBar';
import Footer from './footer';

const DeliveryConfirmation = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/products') 
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error('Error fetching products:', error));
  }, []);

  return (
    <div>
    <Navbar />
    <div className="delivery-confirmation">
      <h1>Delivery Confirmation</h1>
      <div className="products">
        {products.map(product => (
          <div key={product.id} className="product">
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>Price: ${product.price}</p>
            <p>
              Seller Confirmation: {product.isConfirmed ? 'Confirmed' : 'Pending'}
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
