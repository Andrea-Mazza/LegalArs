document.addEventListener('DOMContentLoaded', function () {

    const button = document.getElementById('scroll-to-top');

    // Funzione per verificare la posizione dell'utente
    function checkPosition() {
        if (window.pageYOffset > 0) {
            button.style.display = "block"; // mostra il pulsante se l'utente si trova al di sotto dell'inizio della pagina
        } else {
            button.style.display = "none"; // nasconde il pulsante se l'utente si trova all'inizio della pagina
        }
    }

    // Chiamata alla funzione all'avvio e ad ogni scroll
    checkPosition();
    window.addEventListener("scroll", checkPosition);

    // Funzione per far scorrere l'utente all'inizio della pagina

    button.addEventListener('click', function () {
        window.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    })
})