document.addEventListener('DOMContentLoaded', () => {
    const element = document.querySelectorAll('.full_height');
    const header = document.getElementById('header');

    for (let i = 0; i < element.length; i++) {
        element[i].style.height = `${window.innerHeight}px`;
    }
})