document.addEventListener('DOMContentLoaded', function () {

    //Find al the needed elements in the DOM through them id attribute
    // const body = document.getElementById('body')
    const headerBtn = document.getElementById('headerBtn')
    const lineOne = document.getElementById('lineOne')
    const lineTwo = document.getElementById('lineTwo')
    const lineThree = document.getElementById('lineThree')

    // Build the animation for each line element
    const lineOneAnimation = [
        { top: '4px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(225deg)' }
    ]

    const lineTwoAnimation = [
        { width: '35px' },
        { width: '0px' }
    ]

    const lineThreeAnimation = [
        { top: '24px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(-225deg)' }
    ]

    // Define the timing for all that animation, the lineTwo's animaiton will be faster in order to be invisible when 
    // other lines will rotate
    const animationTiming = {
        duration: 300,
        iteration: 1,
        fill: 'both'
    }

    const lineTwoTiming = {
        duration: 250,
        iteration: 1,
        fill: 'both'
    }

    // Active the animation through a click on headerBtn
    headerBtn.addEventListener('click', function () {
        if (headerBtn.classList.contains('not-open')) {
            lineOne.animate(lineOneAnimation, animationTiming)
            lineTwo.animate(lineTwoAnimation, lineTwoTiming)
            lineThree.animate(lineThreeAnimation, animationTiming)

            headerBtn.classList.remove('not-open')
            // body.classList.add('menu-open')
        } else {
            lineOne.animate(lineOneAnimation, animationTiming).reverse()
            lineTwo.animate(lineTwoAnimation, lineTwoTiming).reverse()
            lineThree.animate(lineThreeAnimation, animationTiming).reverse()

            headerBtn.classList.add('not-open')
            // body.classList.remove('menu-open')
        }
    })

})

//This is a comment to test the collect static command