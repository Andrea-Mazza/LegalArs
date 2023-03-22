document.addEventListener('DOMContentLoaded', function () {

    //Find al the needed elements in the DOM through them id attribute
    const headerBtn = document.getElementById('headerBtn')
    const lineOne = document.getElementById('lineOne')
    const lineTwo = document.getElementById('lineTwo')
    const lineThree = document.getElementById('lineThree')

    // Build the animation for each line element
    const lineOneAnimation = [
        { top: '4px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(225deg)' },
        { top: '4px', transform: 'rotate(0deg)' }
    ]

    const lineTwoAnimation = [
        { width: '35px' },
        { width: '0px' },
        { width: '35px' }
    ]

    const lineThreeAnimation = [
        { top: '24px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(0deg)' },
        { top: '14px', transform: 'rotate(-225deg)' },
        { top: '24px', transform: 'rotate(0deg)' }
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
        lineOne.animate(lineOneAnimation, animationTiming)
        lineTwo.animate(lineTwoAnimation, lineTwoTiming)
        lineThree.animate(lineThreeAnimation, animationTiming)
    })

})