document.addEventListener('DOMContentLoaded', function () {

    const logiIn = document.getElementById('login-form');
    const signUp = document.getElementById('registration-form');
    const switchToSign = document.getElementById('register-now');
    const switchToLog = document.getElementById('login-now');

    const accessoBody = document.getElementById('accesso-body');

    const loginAnimaiton = [
        { opacity: '1', display: 'visible' },
        { opacity: '0', visibility: 'hidden' }
    ];

    const loginAnimaitonTiming = {
        duration: 300,
        iteration: 1,
        fill: 'both'
    }

    const signUpAnimation = [
        { opacity: '0', visibility: 'hidden' },
        { opacity: '1', visibility: 'visible' }
    ];

    const signUpAnimaitonTiming = {
        duration: 300,
        iteration: 1,
        fill: 'both'
    }

    switchToSign.addEventListener('click', function () {
        logiIn.animate(loginAnimaiton, loginAnimaitonTiming);

        setTimeout(() => {
            signUp.animate(signUpAnimation, signUpAnimaitonTiming);

            accessoBody.animate([
                { height: '90vh' },
                { height: '110vh' }
            ], {
                duration: 300,
                easing: 'ease-in-out',
                fill: 'both'
            });
        }, 200);
    })

    switchToLog.addEventListener('click', function () {
        signUp.animate(signUpAnimation, signUpAnimaitonTiming).reverse();

        setTimeout(() => {
            logiIn.animate(loginAnimaiton, loginAnimaitonTiming).reverse();

            accessoBody.animate([
                { height: '90vh' },
                { height: '110vh' }
            ], {
                duration: 300,
                easing: 'ease-in-out',
                fill: 'both'
            }).reverse();
        }, 200);
    })

})