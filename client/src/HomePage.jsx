import React, { useEffect, useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from './NavBar';
import Footer from './footer';
import { Carousel } from 'react-responsive-carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css'; // Ensure the styles are imported
import options from './assets/options.png';
import { AppContext } from './AppContext';

const HomePage = () => {
  const [categories, setCategories] = useState([]);
  const [originalCategories, setOriginalCategories] = useState([]);
  const [carouselProducts, setCarouselProducts] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [showAdvancedSearch, setShowAdvancedSearch] = useState(false);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [minPrice, setMinPrice] = useState('');
  const [maxPrice, setMaxPrice] = useState('');

  const { addToCart } = useContext(AppContext);
  
  const navigate = useNavigate();

  useEffect(() => {
    fetch('https://phase-5-project-group-2-server.onrender.com/products')
      .then((response) => response.json())
      .then((data) => {
        const categorizedProducts = data.reduce((acc, product) => {
          if (!acc[product.category_name]) {
            acc[product.category_name] = [];
          }
          acc[product.category_name].push(product);
          return acc;
        }, {});
        setCategories(Object.entries(categorizedProducts));
        setOriginalCategories(Object.entries(categorizedProducts)); // Store original categories
        setCarouselProducts(data.slice(0, 10));
      })
      .catch((error) => console.error('Error fetching products:', error));
  }, []);

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredCategories = categories.map(([categoryName, products]) => {
    const filteredProducts = products.filter((product) =>
      product.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
    return [categoryName, filteredProducts];
  });

  const handleProductClick = (product) => {
    setSelectedProduct(product);
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
    setSelectedProduct(null);
  };

  const handleViewAll = (categoryName) => {
    navigate(`/category/${categoryName}`);
  };

  const handleAdvancedSearchClick = () => {
    setShowAdvancedSearch(true);
  };

  const handleAdvancedSearchSubmit = () => {
    setShowAdvancedSearch(false);

    const min = minPrice ? parseFloat(minPrice) : 0;
    const max = maxPrice ? parseFloat(maxPrice) : Infinity;

    const filteredCategories = originalCategories.map(([categoryName, products]) => {
      const filteredProducts = products.filter((product) => {
        const matchesName = product.name.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesCategory = selectedCategory ? product.category_name === selectedCategory : true;
        const matchesPrice = product.price >= min && product.price <= max;

        return matchesName && matchesCategory && matchesPrice;
      });

      return [categoryName, filteredProducts];
    });

    setCategories(filteredCategories);
  };

  const handleClearFilters = () => {
    setSearchTerm('');
    setSelectedCategory('');
    setMinPrice('');
    setMaxPrice('');
    setCategories(originalCategories); 
    setShowAdvancedSearch(false);
  };

  const handleAddToCart = (product) => {
    const productWithQuantity = { ...product, quantity: 1 };
    addToCart(productWithQuantity);
    closeModal();
  };

  return (
    <div>
      <Navbar />
      <div className="product-categories">
        <div className="search-bar">
          <input
            type="text"
            placeholder="Search..."
            value={searchTerm}
            onChange={handleSearch}
          />
          <img
            src={options}
            alt="options"
            className="options"
            onClick={handleAdvancedSearchClick}
          />
        </div>
        <div className="carousel-wrapper">
          <Carousel showThumbs={false} autoPlay interval={3000} infiniteLoop>
            {carouselProducts.map((product) => (
              <div key={product.product_id}>
                <img src={product.image} alt={product.name} />
                <p className="legend">{product.name}</p>
              </div>
            ))}
          </Carousel>
        </div>
        {filteredCategories.map(([categoryName, products], index) => (
          <div key={index} className="category">
            <h2>{categoryName}</h2>
            <div className="products">
              {products.slice(0, 8).map((product) => (
                <div key={product.product_id} className="product" onClick={() => handleProductClick(product)}>
                  <div className="product-card">
                    <img src={product.image} alt={product.name} />
                    <p>{product.name}</p>
                  </div>
                </div>
              ))}
              <div className="view-all" onClick={() => handleViewAll(categoryName)}>
                <p>View All</p>
              </div>
            </div>
          </div>
        ))}
      </div>
      <Footer />
      {showModal && selectedProduct && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>&times;</span>
            <img src={selectedProduct.image} alt={selectedProduct.name} />
            <h2>{selectedProduct.name}</h2>
            <p>{selectedProduct.description}</p>
            <p><strong>Price:</strong> Ksh {selectedProduct.price}</p>
            <p><strong>Stock Quantity:</strong> {selectedProduct.stock_quantity}</p>
            <p><strong>Category:</strong> {selectedProduct.category_name}</p>
            <button className="add-to-cart" onClick={() => handleAddToCart(selectedProduct)}>Add to Cart</button>
            <button className="add-to-cart" onClick={closeModal}>Close</button>
          </div>
        </div>
      )}
      {showAdvancedSearch && (
        <div className="advanced-search-modal">
          <div className="modal-content">
            <span className="close" onClick={() => setShowAdvancedSearch(false)}>&times;</span>
            <h2>Advanced Search</h2>
            <div className="advanced-search-form">
              <div>
                <label>Name:</label>
                <input
                  type="text"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>
              <div>
                <label>Categories:</label>
                <select
                  value={selectedCategory}
                  onChange={(e) => setSelectedCategory(e.target.value)}
                >
                  <option value="">All Categories</option>
                  {categories
                    .filter(([categoryName]) => !selectedCategory || categoryName === selectedCategory)
                    .map(([categoryName]) => (
                      <option key={categoryName} value={categoryName}>{categoryName}</option>
                    ))}
                </select>
              </div>
              <div>
                <label>Price:</label>
                <div className="price-range">
                  <input
                    type="number"
                    placeholder="min"
                    value={minPrice}
                    onChange={(e) => setMinPrice(e.target.value)}
                  />
                  <input
                    type="number"
                    placeholder="max"
                    value={maxPrice}
                    onChange={(e) => setMaxPrice(e.target.value)}
                  />
                </div>
              </div>
              <div className="modal-buttons">
                <button className="search-button" onClick={handleAdvancedSearchSubmit}>
                  Search
                </button>
                <button className="clear-button" onClick={handleClearFilters}>
                  Clear
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HomePage;
