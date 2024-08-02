import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const CreateAccount = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
    });
    const [error, setError] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSignUp = async (e) => {
        e.preventDefault();
        const { username, email, password, confirmPassword } = formData;

        if (password !== confirmPassword) {
            setError("Passwords do not match");
            return;
        }

        const response = await fetch('https://phase-5-project-group-2-server.onrender.com/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, email, password })
        });

        if (response.ok) {
            navigate('/login');
        } else {
            const result = await response.json();
            setError(result.message || 'An error occurred');
        }
    };

    return (
        <div className="create-account-container">
            <div className="header">
                <img src="./assets/techlogo.png" alt="Tech Haven Logo" className="logo" />
                <h1 className="title">TECH HAVEN</h1>
            </div>
            <div className="create-account-box">
                <h2>Create Account</h2>
                {error && <p className="error">{error}</p>}
                <form onSubmit={handleSignUp}>
                    <label htmlFor="username">Username:</label>
                    <input
                        type="text"
                        id="username"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />

                    <label htmlFor="email">Email address:</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        placeholder='example@mail.com'
                        required
                    />

                    <label htmlFor="password">Password:</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        placeholder="********"
                        required
                    />

                    <label htmlFor="confirm-password">Confirm password:</label>
                    <input
                        type="password"
                        id="confirm-password"
                        name="confirmPassword"
                        value={formData.confirmPassword}
                        onChange={handleChange}
                        placeholder='********'
                        required
                    />

                    <button type="submit">Sign up</button>
                </form>
                <p>Already have an account? <span onClick={() => navigate('/login')} className="link">Click Here</span> to log in</p>
            </div>
        </div>
    );
};

export default CreateAccount;
