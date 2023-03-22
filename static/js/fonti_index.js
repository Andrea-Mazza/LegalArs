document.addEventListener('DOMContentLoaded', function () {
    // Seleziona tutti gli elementi figli dell'elemento fontiBody con il tag specifico
    const elementiIndice = document.querySelectorAll('h4[id]');

    const container = document.querySelector('.container-index');

    for (let i = 0; i < elementiIndice.length; i++) {
        const ul = document.createElement('ul');
        const li = document.createElement('li');
        const a = document.createElement('a');
        a.setAttribute("href", `#${elementiIndice[i].id}`);
        a.innerHTML = elementiIndice[i].id;


        li.appendChild(a);
        ul.appendChild(li);
        container.appendChild(ul);
    };


});