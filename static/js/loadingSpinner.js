document.addEventListener("DOMContentLoaded", function () {
    const tuttiGliElementiA = document.querySelectorAll('a');

    // Filtra gli elementi <a> con href="#"
    tuttiGliElementiA.forEach((elemento) => {
        if (elemento.getAttribute('href') !== '#') {
            // Aggiungi un event listener per mostrare l'animazione di caricamento
            elemento.addEventListener("click", function () {
                showLoadingAnimation();
            });
        }
    });
});

function showLoadingAnimation() {
    var loadingAnimation = document.getElementById("loading-animation");
    loadingAnimation.style.display = "block";
}