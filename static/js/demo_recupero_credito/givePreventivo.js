document.addEventListener('DOMContentLoaded', function () {
    const body = document.body

    body.addEventListener('submit', function (event) {

        if (event.target.id === 'form_somma') {
            event.preventDefault();

            const form = event.target;
            const token = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

            const request = new XMLHttpRequest();

            const action = '/recupero-credito/give-preventivo/';

            request.open('POST', action, true);

            request.setRequestHeader('X-CSRFToken', token);

            request.onload = function () {
                const formContainer = document.querySelector("#preventivo-container");
                const response = JSON.parse(this.response);

                if (response.status == 'ok') {
                    formContainer.innerHTML = ''
                    formContainer.innerHTML = response.preventivo_form;
                } else if (response.status == 'error') {
                    if (response.preventivo_errors) {
                        formContainer.innerHTML = response.preventivo_errors;
                    } else {
                        let div = document.getElementById(`errorList_${event.target.id}`)
                        div.innerHTML = '';
                        for (let i in response.errors) {
                            let errorMessages = response.errors[i];

                            for (let j in errorMessages) {
                                let errorMessage = errorMessages[j];

                                let p = document.createElement('p');
                                p.innerHTML = errorMessage;
                                div.appendChild(p);
                            }
                        }
                    }
                }
            }
            request.send(new FormData(form));
        }



    })
})