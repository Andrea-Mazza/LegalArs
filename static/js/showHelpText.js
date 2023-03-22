document.addEventListener('DOMContentLoaded', function () {
    const questionMark = document.querySelectorAll('.question-mark');
    const helpText = document.querySelectorAll('.help-text');
    const closeHelpText = document.querySelectorAll('.closeHelpText');


    for (let i = 0; i < questionMark.length; i++) {
        questionMark[i].addEventListener('click', function () {
            if (questionMark[i].classList.contains('pressed')) {
                helpText[i].style.display = 'none';
                questionMark[i].classList.remove('pressed');
            } else {
                helpText[i].style.display = 'block';
                questionMark[i].classList.add('pressed');
            }
        })
    }

    for (let i = 0; i < closeHelpText.length; i++) {
        closeHelpText[i].addEventListener('click', function () {
            helpText[i].style.display = 'none';
            questionMark[i].classList.remove('pressed');
        })
    }


})