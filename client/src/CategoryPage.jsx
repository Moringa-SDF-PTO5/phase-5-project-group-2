import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Navbar from './NavBar';
import Footer from './footer';

const CategoryPage = () => {
  const { categoryName } = useParams();
  const [products, setProducts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 20;

  useEffect(() => {
    fetch('https://phase-5-project-group-2-server.onrender.com/products')
      .then(response => response.json())
      .then(data => {
        const filteredProducts = data.filter(product => product.category_name === categoryName);
        setProducts(filteredProducts);
      })
      .catch(error => console.error('Error fetching products:', error));
  }, [categoryName]);


  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentProducts = products.slice(indexOfFirstItem, indexOfLastItem);
  const totalPages = Math.ceil(products.length / itemsPerPage);

  const handleClick = (page) => {
    setCurrentPage(page);
  };

  return (
    <div>
      <Navbar />
    
    <div>
      <h1>{categoryName}</h1>
      <div className="category-products">
        {currentProducts.map(product => (
          <div key={product.product_id} className="category-product-card">
            <img src={product.image} alt={product.name} />
            <p>{product.name}</p>
            <p>Ksh {product.price}</p>
          </div>
        ))}
      </div>
      <div className="pagination">
        {Array.from({ length: totalPages }, (_, index) => (
          <button
            key={index}
            onClick={() => handleClick(index + 1)}
            className={index + 1 === currentPage ? 'active' : ''}
          >
            {index + 1}
          </button>
        ))}
      </div>
    </div>
    <Footer />
    </div>
  );
};

export default CategoryPage;
