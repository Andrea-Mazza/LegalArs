document.addEventListener('DOMContentLoaded', function () {
    const activity = Array.from(document.getElementsByClassName('img-container'))
    const section = document.getElementById('activity-body')

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

        if (scrollPosition >= 500 && !loopCompleted) {
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