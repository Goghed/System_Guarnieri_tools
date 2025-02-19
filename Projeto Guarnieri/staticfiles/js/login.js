// Adicionando interações simples
document.addEventListener('DOMContentLoaded', function () {
    const loginContainer = document.querySelector('.login-container');

    // Efeito de hover no container
    loginContainer.addEventListener('mouseenter', () => {
        loginContainer.style.transform = 'scale(1.05)';
    });

    loginContainer.addEventListener('mouseleave', () => {
        loginContainer.style.transform = 'scale(1)';
    });
});