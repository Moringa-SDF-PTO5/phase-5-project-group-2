import React, { useEffect, useState } from 'react';
import ModalForm from './ModalForm';
import './admin.css';

const ViewAll = () => {
  const [users, setUsers] = useState([]);
  const [selectedUser, setSelectedUser] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    fetch('https://phase-5-project-group-2-server.onrender.com/staffs')
      .then(response => response.json())
      .then(data => setUsers(data))
      .catch(error => console.error('Error fetching users:', error));
  }, []);

  const handleDelete = (userId) => {
    fetch(`https://phase-5-project-group-2-server.onrender.com/staffs/${staff_id}`, {
      method: 'DELETE',
    })
      .then(response => {
        if (response.ok) {
          setUsers(users.filter(user => user.id !== userId));
        }
      })
      .catch(error => console.error('Error deleting user:', error));
  };

  const handleUpdate = (user) => {
    setSelectedUser(user);
    setIsModalOpen(true);
  };

  const handleFormSubmit = (formData, method) => {
    const url = method === 'POST' 
      ? 'https://phase-5-project-group-2-server.onrender.com/staffs' 
      : `https://phase-5-project-group-2-server.onrender.com/staffs/${formData.id}`;

    fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(updatedUser => {
        if (method === 'POST') {
          setUsers([...users, updatedUser]);
        } else {
          setUsers(users.map(user => (user.id === updatedUser.id ? updatedUser : user)));
        }
        setIsModalOpen(false);
      })
      .catch(error => console.error(`Error ${method === 'POST' ? 'adding' : 'updating'} user:`, error));
  };

  const handleAddNew = () => {
    setSelectedUser(null);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedUser(null);
  };

  return (
    <div>
      <h1>View All Users</h1>
      <button onClick={handleAddNew}>Add New Staff</button>
      <div className="user-cards">
        {users.map(user => (
          <div key={user.id} className="user-card">
            <h3>{user.first_name} {user.last_name}</h3>
            <p>{user.email}</p>
            <p>{user.role}</p>
            <button onClick={() => handleUpdate(user)}>Update</button>
            <button onClick={() => handleDelete(user.id)}>Delete</button>
          </div>
        ))}
      </div>
      {isModalOpen && (
        <ModalForm
          isOpen={isModalOpen}
          onClose={handleCloseModal}
          onSubmit={handleFormSubmit}
          initialData={selectedUser}
        />
      )}
    </div>
  );
};

export default ViewAll;
