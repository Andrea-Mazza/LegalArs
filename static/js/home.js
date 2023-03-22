document.addEventListener('DOMContentLoaded', function () {

    // Select all elements with the 'home-number' class
    const homeNumbers = document.querySelectorAll('.home-number');

    // Define a function that animates an element's value from start to end over a given duration
    function animateValue(element, start, end, duration) {
        // Calculate the range between start and end
        const range = end - start;
        // Set the current value to start
        let current = start;
        // Determine the increment to use based on whether start is less than end
        const increment = end > start ? 1 : -1;
        // Calculate the time for each step
        const stepTime = Math.abs(Math.floor(duration / range));
        // Use setInterval to update the element's value every stepTime milliseconds
        const timer = setInterval(function () {
            current += increment;
            element.innerText = current;
            // If the current value has reached the end, clear the interval
            if (current == end) {
                clearInterval(timer);
            }
        }, stepTime);
    }

    // Set up the intersection observer
    const observer = new IntersectionObserver(entries => {
        // Loop through each entry
        entries.forEach(entry => {
            // If the element is intersecting (visible) and its intersection ratio is greater than 0
            if (entry.isIntersecting && entry.intersectionRatio > 0) {
                // Animate the element's inner number from 0 to its final value over 2 seconds (2000 milliseconds)
                animateValue(entry.target.querySelector('.number'), 0, parseInt(entry.target.querySelector('.number').innerText), 500);
                // Disconnect the observer once the animation is complete
                observer.disconnect();
            }
        });
    });

    // Loop through each home-number element and observe it
    homeNumbers.forEach(number => {
        observer.observe(number);
    });




    const activity = Array.from(document.getElementsByClassName('img-container'))
    const section = document.getElementById('home-section-four')

    const activityAnimation = [
        { transform: 'translateY(100%)' },
        { transform: 'translateY(0%)' }
    ]

    const activityTiming = {
        duration: 300,
        iteration: 1,
        fill: 'both'
    }

    let loopCompleted = false;

    window.addEventListener('scroll', () => {
        const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;

        if (scrollPosition >= 1967 && !loopCompleted) {
            loopCompleted = true;
            animateElements(activity, 0);
        }
    });

    function animateElements(elements, index) {
        if (index >= elements.length) {
            return;
        }

        elements[index].animate(activityAnimation, activityTiming);

        setTimeout(() => {
            animateElements(elements, index + 1);
        }, 100); // 1 second
    }

    //  the animateElements function is a recursive function that animates each element 
    // in the elements array one at a time. The setTimeout function is used to pause the loop for 1 second 
    // (1000 milliseconds) before animating the next element.

    // The animateElements function is called when the scroll position reaches 1967 pixels
    //  and the loop has not yet been completed. The loopCompleted flag is set to true to prevent the loop 
    //  from being run again.

})