document.addEventListener('DOMContentLoaded', function () {

    body = document.body;

    this.body.addEventListener('submit', function (event) {
        // Verifica se l'elemento che ha innescato l'evento è uno dei tuoi form
        if (event.target.id === 'form_cr_pf' || event.target.id === 'form_cr_pj'
            || event.target.id === 'tipo_cr_form' || event.target.id === 'tipo_db_form'
            || event.target.id === 'form_db_pf' || event.target.id === 'form_db_pj'
            || event.target.id === 'form_somma' || event.target.id === 'firma-form' || event.target.id === 'documenti_form') {
            // Impedisci l'invio del form
            event.preventDefault();

            let formContainerCr = document.querySelector("#cr-form-container");
            let formContainerDb = document.querySelector("#db-form-container");
            let formContainerDoc = document.querySelector('#documenti-form-container');

            const loadingSpinner = document.getElementById(`loadingSpinner_${event.target.id}`)

            const form = event.target;
            const token = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

            const request = new XMLHttpRequest();

            // Determina l'URL dell'azione in base all'ID del form
            let action;
            switch (form.id) {
                case 'form_cr_pf':
                    action = '/recupero-credito/get-cr-pf-form/';
                    break;
                case 'form_cr_pj':
                    action = '/recupero-credito/get-cr-pj-form/';
                    break;
                case 'tipo_cr_form':
                    action = '/recupero-credito/get-tipo-creditore/';
                    break;
                case 'form_db_pf':
                    action = '/recupero-credito/get-db-pf-form/';
                    break;
                case 'form_db_pj':
                    action = '/recupero-credito/get-db-pj-form/';
                    break;
                case 'tipo_db_form':
                    action = '/recupero-credito/get-tipo-debitore/';
                    break;
                case 'form_somma':
                    action = '/recupero-credito/get-somma/';
                    break;
                case 'firma-form':
                    action = '/recupero-credito/get-firma/';
                    break;
                case 'documenti_form':
                    action = '/recupero-credito/get-documenti/';
                    break;
            }
            request.open('POST', action, true);
            // request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            request.setRequestHeader('X-CSRFToken', token);

            // loadingSpinner.style.display = "block";
            // if (event.target.id == 'tipo_cr_form') {
            //     formContainerCr.innerHTML = '';
            //     formContainerCr.appendChild(loadingSpinner);
            // } else if (event.target.id == 'tipo_db_form') {
            //     formContainerDb.innerHTML = '';
            //     formContainerDb.appendChild(loadingSpinner);
            // }

            request.onload = function () {
                // loadingSpinner.style.display = "none";


                if (this.status >= 200 && this.status < 400) {
                    let response = JSON.parse(this.response);
                    if (response.status == 'ok') {
                        console.log('done');
                        if (event.target.id == 'tipo_cr_form') {
                            formContainerCr.innerHTML = '';
                            formContainerCr.innerHTML = response.new_form;
                        } else if (event.target.id == 'tipo_db_form') {
                            formContainerDb.innerHTML = '';
                            formContainerDb.innerHTML = response.new_form;
                        } else if (event.target.id == 'firma-form') {
                            formContainerDoc.innerHTML = '';
                            formContainerDoc.innerHTML = response.new_form;
                        }
                    } else {
                        console.log('Validation error: ', response.errors);

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

                        // Mostra gli errori di validazione
                        // for (let fieldName in response.errors) {
                        //     let errorMessages = response.errors[fieldName];
                        //     // Ora hai il nome del campo (fieldName) e una lista di messaggi di errore (errorMessages)
                        //     // Usa questi per mostrare gli errori nel tuo form
                        //     let errorDiv = document.getElementById(fieldName + '_error');
                        //     if (errorDiv) {
                        //         errorDiv.textContent = errorMessages.join(', ');
                        //     } else {
                        //         console.log('Non è stato trovato nessun div di errore per il campo ' + fieldName);
                        //     }
                        // }
                    }
                } else if (this.status == 400) {
                    alert('Assicurati che tutti i campi siano stati compilati e confermati correttamente');
                } else {
                    alert('Server error');
                }
            }

            request.send(new FormData(form));
        }

        if (event.target.id === 'check-fields-form') {
            // Impedisci l'invio del form
            event.preventDefault();

            const form = event.target;
            const token = form.querySelector('input[name="csrfmiddlewaretoken"]').value;

            const request = new XMLHttpRequest();

            // Determina l'URL dell'azione in base all'ID del form
            let action = '/recupero-credito/check-fields/';

            request.open('POST', action, true);
            request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            request.setRequestHeader('X-CSRFToken', token);

            request.onload = function () {

                let formContainer = document.querySelector("#preventivo-container");

                if (this.status >= 200 && this.status < 400) {
                    let response = JSON.parse(this.response);
                    if (response.status == 'ok') {
                        console.log('done');
                        formContainer.innerHTML = '';
                        formContainer.innerHTML = response.new_form;
                    } else {
                        alert('Assicurati che tutti i campi siano stati compilati e confermati correttamente');
                    }
                } else {
                    alert('Server error');
                }
            }

            request.send(new URLSearchParams(new FormData(form)).toString());
        }
    })


})