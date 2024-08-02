import React, { useState, useEffect } from 'react';
import './admin.css';

const ModalForm = ({ isOpen, onClose, onSubmit, initialData }) => {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    role: '',
  });

  useEffect(() => {
    if (initialData) {
      setFormData(initialData);
    } else {
      setFormData({
        first_name: '',
        last_name: '',
        email: '',
        role: '',
      });
    }
  }, [initialData]);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData, initialData ? 'PUT' : 'POST');
  };

  if (!isOpen) return null;

  return (
    <div className="admin-modal-overlay">
      <div className="admin-modal-content">
        <span className="admin-close-button" onClick={onClose}>&times;</span>
        <h2>{initialData ? 'Update Staff' : 'Add New Staff'}</h2>
        <form onSubmit={handleSubmit}>
          <label>
            First Name:
            <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} required />
          </label>
          <label>
            Last Name:
            <input type="text" name="last_name" value={formData.last_name} onChange={handleChange} required />
          </label>
          <label>
            Email:
            <input type="email" name="email" value={formData.email} onChange={handleChange} required />
          </label>
          <label>
            Role:
            <input type="text" name="role" value={formData.role} onChange={handleChange} required />
          </label>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
};

export default ModalForm;
