import React from 'react';
import Instagram from './assets/Instagram.png';
import X from './assets/X.png';
import Facebook from './assets/Facebook.png'

const Footer = () => {
  const handleSocialClick = (url) => {
    window.open(url, '_blank');
  };

  return (
    <footer className="footer">
      <div>Contact: +2547123456789</div>
      <div>Physical Address: Luthuli Street, Nairobi</div>
      <div className="social-media">
        <button onClick={() => handleSocialClick('https://www.instagram.com')}>
          <img src={Instagram} alt="Instagram" className="social-icon" />
        </button>
        <button onClick={() => handleSocialClick('https://www.x.com')}>
          <img src={X} alt="X (Twitter)" className="social-icon" />
        </button>
        <button onClick={() => handleSocialClick('https://www.facebook.com')}>
          <img src={Facebook} alt="Facebook" className="social-icon" />
        </button>
      </div>
    </footer>
  );
};

export default Footer;
