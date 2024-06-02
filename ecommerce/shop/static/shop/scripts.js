// static/shop/scripts.js

document.addEventListener('DOMContentLoaded', () => {
    // Example: Add event listeners for cart update
    const cartButtons = document.querySelectorAll('.cart-button');

    cartButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Logic for updating cart
            console.log('Cart updated');
        });
    });
});
