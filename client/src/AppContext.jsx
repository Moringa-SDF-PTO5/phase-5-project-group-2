import React, { createContext, useState } from 'react';

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [cartItems, setCartItems] = useState([]);

  const login = () => setIsLoggedIn(true);
  const logout = () => setIsLoggedIn(false);

  const addToCart = (item) => {
    setCartItems((prevItems) => {
      const existingItemIndex = prevItems.findIndex((i) => i.product_id === item.product_id);
      
      if (existingItemIndex > -1) {
        const updatedItems = [...prevItems];
        updatedItems[existingItemIndex].quantity += item.quantity;
        return updatedItems;
      } else {
        return [...prevItems, item];
      }
    });
  };
  

  const clearCart = () => setCartItems([]);

  return (
    <AppContext.Provider
      value={{ isLoggedIn, login, logout, cartItems, addToCart, clearCart }}
    >
      {children}
    </AppContext.Provider>
  );
};
