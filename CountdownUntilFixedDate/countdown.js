const theDay = "<p>C'est le jour J</p>";
const afterTheDay = "<p>C'est en cours depuis le 15 !</p>";

const deadline = "2020/10/15";
let today = new Date();
let y = today.getFullYear();
let m = today.getMonth();
let d = today.getDate();
let todayFormated = new Date(y, m, d).getTime();
let jourJ = new Date("2020/10/15").getTime();

function getTimeRemaining(endtime) {
  const total = Date.parse(endtime) - Date.parse(new Date());
  const seconds = Math.floor((total / 1000) % 60);
  const minutes = Math.floor((total / 1000 / 60) % 60);
  const hours = Math.floor((total / (1000 * 60 * 60)) % 24);
  const days = Math.floor(total / (1000 * 60 * 60 * 24));

  return {
    total,
    days,
    hours,
    minutes,
    seconds,
  };
}

function initializeClock(id, endtime) {
  const clock = document.getElementById(id);
  const daysSpan = clock.querySelector(".days");
  const hoursSpan = clock.querySelector(".hours");
  const minutesSpan = clock.querySelector(".minutes");
  const secondsSpan = clock.querySelector(".seconds");

  function updateClock() {
    const t = getTimeRemaining(endtime);

    daysSpan.innerHTML = t.days;
    hoursSpan.innerHTML = ("0" + t.hours).slice(-2);
    minutesSpan.innerHTML = ("0" + t.minutes).slice(-2);
    secondsSpan.innerHTML = ("0" + t.seconds).slice(-2);

    if (t.total <= 0) {
      clearInterval(timeinterval);
    }
  }

  updateClock();
  const timeinterval = setInterval(updateClock, 1000);
}

if (todayFormated > jourJ) {
  document.getElementById("dayDandAdfer").innerHTML = afterTheDay;
} else if (todayFormated === jourJ) {
  document.getElementById("dayDandAdfer").innerHTML = theDay;
} else {
  initializeClock("clockdiv", deadline);
  document.getElementById("clockdiv").style.display = "block";
}
