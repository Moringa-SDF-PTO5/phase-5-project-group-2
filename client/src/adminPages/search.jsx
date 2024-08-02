import React from 'react';
import './admin.css'

const SearchUser = () => {
  return (
    <div className="search-user">
      <header className="header">
        <div className="left-icons">
          <span className="icon">&#x1F5C2;</span>
          <span>Admin</span>
        </div>
        <div className="right-icons">
          <span className="icon">&#x1F4E6;</span>
          <span className="icon">&#x1F464;</span>
        </div>
      </header>
      <div className="search-bar">
        <input type="text" placeholder="Enter staff email" />
        <button className="search-btn">&#x1F50D;</button>
      </div>
    </div>
  );
};

export default SearchUser;
