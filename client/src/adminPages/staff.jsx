import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './admin.css';
import ModalForm from './ModalForm';

const Staff = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleAddNewStaff = () => {
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  const handleFormSubmit = (formData) => {
    console.log('Form Data:', formData);
    handleCloseModal();
  };

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
        <div className="card" onClick={handleAddNewStaff}>
          <span className="card-icon">&#x1F464;</span>
          <p>Add new staff</p>
        </div>
        <Link to="/search" className="card">
          <span className="card-icon">&#x1F464;</span>
          <p>Search</p>
        </Link>
        <Link to="/view-all" className="card">
          <span className="card-icon">&#x1F4C8;</span>
          <p>View All</p>
        </Link>
      </div>
      <ModalForm isOpen={isModalOpen} onClose={handleCloseModal} onSubmit={handleFormSubmit} />
    </div>
  );
};

export default Staff;
