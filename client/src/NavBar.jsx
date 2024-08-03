import React, { useContext,useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { AppContext } from './AppContext';
import techlogo from './assets/techlogo.png';
import cart from './assets/cart.png';
import home from './assets/home.png';
import profile from './assets/profile.png';

const Navbar = () => {
  const { isLoggedIn, logout, cartItems } = useContext(AppContext);
  const [showProfileOptions, setShowProfileOptions] = useState(false);
  const navigate = useNavigate();

  const handleHomeClick = () => {
    navigate('/');
  };

  const handleCartClick = () => {
    navigate('/ordering');
  };

  const handleProfileClick = () => {
    setShowProfileOptions(!showProfileOptions);
  };

  const handleLogout = () => {
    logout();
    setShowProfileOptions(false);
  };

  const cartItemCount = cartItems.reduce((count, item) => count + item.quantity, 0);
  const handleMyOrdersClick = () => {
    navigate('/order-details');
    setShowProfileOptions(false);
  };
  return (
    <nav className="navbar">
      <div className='title'>
      <img src={techlogo} alt="Tech Haven Logo" className="logo" />
      <h1>TECH HAVEN</h1>
      </div>
      <div className="navbar-icons">
        <button className="icon-btn" onClick={handleHomeClick}>
          <img src={home} alt="Home" className="icon" />
        </button>
        <div className="icon-btn" onClick={handleCartClick}>
          <img src={cart} alt="Cart" className="icon" />
          {cartItemCount > 0 && <span className="cart-count">{cartItemCount}</span>}
        </div>
        <div className="icon-btn" onClick={handleProfileClick}>
          <img src={profile} alt="Profile" className="icon" />
          {showProfileOptions && (
            <div className="profile-options">
              {isLoggedIn ? (
                <>
                  <div className="option" onClick={handleMyOrdersClick}>My Orders</div>
                  <div className="option" onClick={handleLogout}>Log out</div>
                </>
              ) : (
                <div className="option" onClick={() => navigate('/login')}>Login</div>
              )}
            </div>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
