import React from 'react';
import { Link } from 'react-router-dom';
import './admin.css';

const AdminDashboard = () => {
  return (
    <div className="admin-dashboard">
      <header className="header">
        <div className="left-icons">
          <span className="icon">&#x1F5C2;</span>
          <span>Admin</span>
        </div>
        <div className="right-icons">
          <span className="icon">&#x1F464;</span>
        </div>
      </header>
      <div className="content">
        <Link to="/staff" className="card">
          <span className="card-icon">&#x1F464;</span>
          <p>Staff</p>
        </Link>
        <Link to="/analysis" className="card">
          <span className="card-icon">&#x1F4C8;</span>
          <p>Analysis</p>
        </Link>
      </div>
    </div>
  );
};

export default AdminDashboard;
