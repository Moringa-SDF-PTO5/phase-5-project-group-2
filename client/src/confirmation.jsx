import React, { useContext } from 'react';
import { AppContext } from './AppContext';

const ConfirmationPage = () => {
    const { cartItems } = useContext(AppContext);
    console.log(cartItems)

    return (
        <div>
            <h2>Order Confirmation</h2>
            {cartItems.length === 0 ? (
                <p>Your order has been placed successfully!</p>
            ) : (
                <p>There seems to be an issue. Please contact support.</p>
            )}
        </div>
    );
};

export default ConfirmationPage;
