//############## TIMER CONFIGURATION START ##############
//Set Timer Length

var minutes = 0
var seconds = 9
//############## TIMER CONFIGURATION END ##############

function countdown(id, minutes, seconds) {
    var element, endTime, hours, mins, msLeft, time;

    function twoDigits(n) {
        return (n <= 9 ? "0" + n : n);
    }

    function updateTimer() {
        msLeft = endTime - (+new Date);

        //USER CUSTOMIZATION- you can edit color and text of the 'time expired' readout under the element.innerHTML
        if (msLeft < 1000) {
            element.innerHTML = "<span style='color:#CC5B5B'>!<br/>!<br/>!<br/>!<br/>!<br/>!</span>";
        } else {
            time = new Date(msLeft);
            hours = time.getUTCHours();
            mins = time.getUTCMinutes();
            element.innerHTML = (hours ? hours + ':' + twoDigits(mins) : mins) + ':' + twoDigits(time.getUTCSeconds());
            setTimeout(updateTimer, time.getUTCMilliseconds() + 500);
        }
    }
    element = document.getElementById(elementName);
    endTime = (+new Date) + 1000 * (60 * minutes + seconds) + 500;
    updateTimer();
}
countdown("s2", minutes, seconds); //2nd value is the minute, 3rd is the seconds