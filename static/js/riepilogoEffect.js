document.addEventListener('DOMContentLoaded', function () {
    const tipo_creditore = document.querySelector('#id_tipo_creditore');

    // effect for start.html
    if (tipo_creditore) {
        const riepilogoTipoCr = document.getElementById('riepilogo-tipo_cr');
        const selectValue = tipo_creditore.value;

        // if (selectValue === 'PJ') {
        //     riepilogoTipoCr.innerHTML = `Tipologia: Persona Giuridica`;
        // } else {
        //     riepilogoTipoCr.innerHTML = `Tipologia: Persona Fisica`;
        // }



        // tipo_creditore.addEventListener('change', function () {
        //     let selectedValue = tipo_creditore.options[tipo_creditore.selectedIndex].innerHTML;

        //     riepilogoTipoCr.innerHTML = `Tipologia: ${selectedValue}`;

        // })


        const element = [
            tipo_creditore
        ];
        // for (let i = 0; i < valueContainer.length; i++) {
        //     element.push(document.querySelector(`#id_tipo_debitore`));

        // }
        for (let i = 0; i < element.length; i++) {
            let selectedValue = element[i].options[element[i].selectedIndex].innerHTML;
            riepilogoTipoCr.innerHTML = `Tipologia: ${selectedValue}`;

            element[i].addEventListener('change', function () {
                let selectedValue = element[i].options[element[i].selectedIndex].innerHTML;
                riepilogoTipoCr.innerHTML = `Tipologia: ${selectedValue}`;
            })
        }

        // tipo_creditore.addEventListener('change', function () {
        //     let selectedValue = this.options[this.selectedIndex].value;

        //     if (selectedValue === 'PJ') {
        //         riepilogoTipoCr.innerHTML = `Tipologia: Persona Giuridica`;
        //     } else {
        //         riepilogoTipoCr.innerHTML = `Tipologia: Persona Fisica`;
        //     }
        // })
    }


    // effect for dati_creditore.html when tipo_creditore is PJ or PF
    const denominazioneCrPj = document.querySelector('#id_cr_denominazione_sociale');
    const comuneSedeCrPj = document.querySelector('#id_cr_comune_sede_principale');
    const indirizzoSedeCrPj = document.querySelector('#id_cr_indirizzo_sede_principale');

    const nomeCrPf = document.querySelector('#id_cr_nome');
    const cognomeCrPf = document.querySelector('#id_cr_cognome');
    const luogoNasciatCrPf = document.querySelector('#id_cr_luogo_di_nascita');
    const dataNascitaCrPf = document.querySelector('#id_cr_data_di_nascita');
    const comuneResidenzaCrPf = document.querySelector('#id_cr_comune_di_residenza');
    const indirizzoResidenzaCrPf = document.querySelector('#id_cr_indirizzo_di_residenza');

    // these fields are commons between PF and PJ
    const emailCr = document.querySelector('#id_cr_email');
    const pecCr = document.querySelector('#id_cr_pec');
    const codiceCr = document.querySelector('#id_cr_codice_fiscale');
    const ivaCr = document.querySelector('#id_cr_partita_iva');

    const valueContainer = document.querySelectorAll('.value-container')

    if (denominazioneCrPj) {

        const inputList = [
            denominazioneCrPj,
            comuneSedeCrPj,
            indirizzoSedeCrPj,
            emailCr,
            pecCr,
            codiceCr,
            ivaCr
        ];

        for (let i = 0; i < inputList.length; i++) {

            if (inputList[i].nodeName === "SELECT") {
                inputList[i].addEventListener('change', function () {
                    let selectedValue = inputList[i].options[inputList[i].selectedIndex].innerHTML;

                    valueContainer[i].innerHTML = `${selectedValue}`;
                })
            } else {
                inputList[i].addEventListener('input', function () {
                    let inputValue = inputList[i].value;

                    valueContainer[i].innerHTML = `${inputValue}`;
                })
            }


        }
    }

    if (nomeCrPf) {

        const inputList = [
            nomeCrPf,
            cognomeCrPf,
            luogoNasciatCrPf,
            dataNascitaCrPf,
            comuneResidenzaCrPf,
            indirizzoResidenzaCrPf,
            emailCr,
            pecCr,
            codiceCr,
            ivaCr
        ];

        for (let i = 0; i < inputList.length; i++) {

            if (inputList[i].nodeName === "SELECT") {
                inputList[i].addEventListener('change', function () {
                    let selectedValue = inputList[i].options[inputList[i].selectedIndex].innerHTML;

                    valueContainer[i].innerHTML = `${selectedValue}`;
                })
            } else {
                inputList[i].addEventListener('input', function () {
                    let inputValue = inputList[i].value;

                    valueContainer[i].innerHTML = `${inputValue}`;
                })
            }


        }
    }

    // effect for numero_debitori.html

    // const numDebitori = document.querySelector('#id_numero_debitori');

    // if (numDebitori) {

    //     numDebitori.addEventListener('input', function () {
    //         let inputValue = numDebitori.value;

    //         valueContainer[0].innerHTML = `${inputValue}`;
    //     })
    // }

    // effect for tipo_debitore.html

    const tipoDebitore = document.querySelector('#id_tipo_debitore');

    if (tipoDebitore) {
        const element = [
            tipoDebitore
        ];
        // for (let i = 0; i < valueContainer.length; i++) {
        //     element.push(document.querySelector(`#id_tipo_debitore`));

        // }
        for (let i = 0; i < element.length; i++) {
            let selectedValue = element[i].options[element[i].selectedIndex].innerHTML;
            valueContainer[i].innerHTML = `${selectedValue}`;

            element[i].addEventListener('change', function () {
                let selectedValue = element[i].options[element[i].selectedIndex].innerHTML;
                valueContainer[i].innerHTML = `${selectedValue}`;
            })
        }
    }


    // effect for dati_debitore.html

    // const denominazioneDbPj = document.querySelector('#id_form-0-db_denominazione_sociale');

    // const sedeDbPj = document.querySelectorAll('#id_db_sede_principale');
    // const codiceDbPj = document.querySelectorAll('#id_dj_codice_fiscale');
    // const partitaDbPj = document.querySelectorAll('#id_dj_partita_iva');

    // const nomeDbPf = document.querySelector('#id_form-0-db_nome');

    // const cognomeDbPf = document.querySelectorAll('#id_db_cognome');
    // const luogoNascitaDbPf = document.querySelectorAll('#id_db_luogo_di_nascita');
    // const dataNascitaDbPf = document.querySelectorAll('#id_db_data_di_nascita');
    // const indirizzoResidenzaDbPf = document.querySelectorAll('#id_db_indirizzo_di_residenza');
    // const codiceDbPf = document.querySelectorAll('#id_df_codice_fiscale');
    // const partitaDbPf = document.querySelectorAll('#id_df_partita_iva');

    // const debitori = document.querySelector('#numero').innerHTML;
    // const numeroDebitori = parseInt(debitori);

    // if (denominazioneDbPj && nomeDbPf) {
    //     console.log('work2');
    //     const elementsPj = [];

    //     for (let i = 0; i < numeroDebitori; i++) {
    //         elementsPj.push(
    //             document.querySelector(`#id_form-${i}-db_denominazione_sociale`),
    //             document.querySelector(`#id_form-${i}-db_sede_principale`),
    //             document.querySelector(`#id_form-${i}-dj_codice_fiscale`),
    //             document.querySelector(`#id_form-${i}-dj_partita_iva`),
    //         );
    //     }
    //     for (let i = 0; i < elementsPj.length; i++) {

    //         if (elementsPj[i].nodeName === "SELECT") {
    //             elementsPj[i].addEventListener('change', function () {
    //                 let selectedValue = elementsPj[i].options[elementsPj[i].selectedIndex].innerHTML;

    //                 djContainer[i].innerHTML = `${selectedValue}`;
    //             })
    //         } else {
    //             elementsPj[i].addEventListener('input', function () {
    //                 let inputValue = elementsPj[i].value;

    //                 djContainer[i].innerHTML = `${inputValue}`;
    //             })
    //         }
    //     }



    //     console.log('work1');
    //     const elementsPf = [

    //     ];
    //     for (let i = 0; i < numeroDebitori; i++) {
    //         elementsPf.push(
    //             document.querySelector(`#id_form-${i}-db_nome`),
    //             document.querySelector(`#id_form-${i}-db_cognome`),
    //             document.querySelector(`#id_form-${i}-db_luogo_di_nascita`),
    //             document.querySelector(`#id_form-${i}-db_data_di_nascita`),
    //             document.querySelector(`#id_form-${i}-db_indirizzo_di_residenza`),
    //             document.querySelector(`#id_form-${i}-df_codice_fiscale`),
    //             document.querySelector(`#id_form-${i}-df_partita_iva`),
    //         );
    //     }
    //     for (let i = 0; i < elementsPf.length; i++) {

    //         if (elementsPf[i] !== null && elementsPf[i].nodeName === "SELECT") {
    //             elementsPf[i].addEventListener('change', function () {
    //                 let selectedValue = elementsPf[i].options[elementsPf[i].selectedIndex].innerHTML;

    //                 dfContainer[i].innerHTML = `${selectedValue}`;
    //             })
    //         } else {
    //             elementsPf[i].addEventListener('input', function () {
    //                 let inputValue = elementsPf[i].value;

    //                 dfContainer[i].innerHTML = `${inputValue}`;
    //             })
    //         }
    //     }


    // }

    const denominazioneDbPj = document.querySelector('#id_db_denominazione_sociale');
    const sedeDbPj = document.querySelector('#id_db_sede_principale');
    const codiceDbPj = document.querySelector('#id_dj_codice_fiscale');
    const ivaDbPj = document.querySelector('#id_dj_partita_iva');

    const nomeDbPf = document.querySelector('#id_db_nome');
    const cognomeDbPf = document.querySelector('#id_db_cognome');
    const luogoNascitaDbPf = document.querySelector('#id_db_luogo_di_nascita');
    const residenzaDbPf = document.querySelector('#id_db_indirizzo_di_residenza');
    const codiceDbPf = document.querySelector('#id_db_codice_fiscale');
    const ivaDbPf = document.querySelector('#id_db_partita_iva');


    const dfContainer = document.querySelectorAll('.df-value-container');
    const djContainer = document.querySelectorAll('.dj-value-container');

    if (nomeDbPf) {
        const element = [
            nomeDbPf,
            cognomeDbPf,
            luogoNascitaDbPf,
            residenzaDbPf,
            codiceDbPf,
            ivaDbPf
        ];

        for (let i = 0; i < element.length; i++) {
            if (element[i].nodeName === "SELECT") {
                element[i].addEventListener('change', function () {
                    let selectedValue = element[i].options[element[i].selectedIndex].innerHTML;

                    dfContainer[i].innerHTML = `${selectedValue}`;
                })
            } else {
                element[i].addEventListener('input', function () {
                    let inputValue = element[i].value;

                    dfContainer[i].innerHTML = `${inputValue}`;
                })
            }
        }
    }

    if (denominazioneDbPj) {
        const element = [
            denominazioneDbPj,
            sedeDbPj,
            codiceDbPj,
            ivaDbPj
        ];

        for (let i = 0; i < element.length; i++) {
            if (element[i].nodeName === "SELECT") {
                element[i].addEventListener('change', function () {
                    let selectedValue = element[i].options[element[i].selectedIndex].innerHTML;

                    djContainer[i].innerHTML = `${selectedValue}`;
                })
            } else {
                element[i].addEventListener('input', function () {
                    let inputValue = element[i].value;

                    djContainer[i].innerHTML = `${inputValue}`;
                })
            }
        }
    }


    const somma = document.querySelector('#id_somma');
    const container = document.querySelector('.somma-value-container');

    if (somma) {


        somma.addEventListener('input', function () {
            let inputValue = somma.value;

            container.innerHTML = `${inputValue}`;
        })
    }

    // const elementsPf = [];
    // const elementsPj = [];
    // for (let y = 0; y < numeroDebitori; y++) {
    //     const denominazioneDbPj = document.querySelector(`#id_form-${y}-db_denominazione_sociale`);
    //     const nomeDbPf = document.querySelector(`#id_form-${y}-db_nome`);


    //     if (nomeDbPf) {
    //         elementsPf.push(
    //             nomeDbPf,
    //             document.querySelector(`#id_form-${y}-db_cognome`),
    //             document.querySelector(`#id_form-${y}-db_luogo_di_nascita`),
    //             document.querySelector(`#id_form-${y}-db_data_di_nascita`),
    //             document.querySelector(`#id_form-${y}-db_indirizzo_di_residenza`),
    //             document.querySelector(`#id_form-${y}-df_codice_fiscale`),
    //             document.querySelector(`#id_form-${y}-df_partita_iva`),
    //         );
    //     }

    //     if (denominazioneDbPj) {
    //         elementsPj.push(
    //             denominazioneDbPj,
    //             document.querySelector(`#id_form-${y}-db_sede_principale`),
    //             document.querySelector(`#id_form-${y}-dj_codice_fiscale`),
    //             document.querySelector(`#id_form-${y}-dj_partita_iva`),
    //         );
    //     }
    // }

    // for (let i = 0; i < elementsPf.length; i++) {
    //     if (elementsPf[i].nodeName === "SELECT") {
    //         elementsPf[i].addEventListener('change', function () {
    //             let selectedValue = elementsPf[i].options[elementsPf[i].selectedIndex].innerHTML;

    //             dfContainer[i].innerHTML = `${selectedValue}`;
    //         })
    //     } else {
    //         elementsPf[i].addEventListener('input', function () {
    //             let inputValue = elementsPf[i].value;

    //             dfContainer[i].innerHTML = `${inputValue}`;
    //         })
    //     }
    // }

    // for (let i = 0; i < elementsPj.length; i++) {
    //     if (elementsPj[i].nodeName === "SELECT") {
    //         elementsPj[i].addEventListener('change', function () {
    //             let selectedValue = elementsPj[i].options[elementsPj[i].selectedIndex].innerHTML;

    //             djContainer[i].innerHTML = `${selectedValue}`;
    //         })
    //     } else {
    //         elementsPj[i].addEventListener('input', function () {
    //             let inputValue = elementsPj[i].value;

    //             djContainer[i].innerHTML = `${inputValue}`;
    //         })
    //     }
    // }


})