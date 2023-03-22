document.addEventListener('DOMContentLoaded', function () {

    function typingEffect(elem) {
        // Get the text element
        // const elem = document.getElementById('typing-container');

        // Set the initial text of the paragraph to an empty string
        elem.innerHTML = '';

        // Set the delay between each character in milliseconds
        const delay = 25;

        // Set the initial position of the text cursor
        let i = 0;

        // Create a function that will be called by setInterval() to update the text of the paragraph
        function updateText() {
            // Get the next character of the text
            const text = elem.getAttribute('data-text');
            const char = text[i];

            // Add the character to the text of the paragraph
            elem.textContent += char;

            // Increment the position of the text cursor
            i++;

            // If we have reached the end of the text, stop the interval
            if (i >= text.length) {
                clearInterval(intervalId);
                elem.innerHTML += '<span class="cursor"></span>';
            }
        }

        // Start the interval to update the text of the paragraph
        const intervalId = setInterval(updateText, delay);
    }


    //These elements are located in legal_sharing.html
    const headingOne = document.getElementById('typing-container');
    const headingTwo = document.getElementById('typing-container-2');
    const headingThree = document.getElementById('typing-container-3')

    typingEffect(headingOne);

    setTimeout(function () {
        typingEffect(headingTwo);
    }, 25);

    setTimeout(function () {
        typingEffect(headingThree);
    }, 75);


})