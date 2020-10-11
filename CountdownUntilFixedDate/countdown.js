const beforeTheDay =
  '<div id="clockdiv" style="max-height: 25px;">' +
  ' <div>' +
  '   <span class="days"></span>' +
  '   <div class="smalltext">Days</div>' +
  " </div>" +
  ' <div>' +
  '   <span class="hours"></span>' +
  '   <div class="smalltext">Hours</div>' +
  " </div>" +
  ' <div>' +
  '   <span class="minutes"></span>' +
  '   <div class="smalltext">Minutes</div>' +
  " </div>" +
  ' <div>' +
  '   <span class="seconds"></span>' +
  '   <div class="smalltext">Seconds</div>' +
  "</div>";
const theDay = "C'est le jour J";
const afterTheDay = "C'est en cours depuis le 15 !";

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
  document.getElementById("countdownView").innerHTML = afterTheDay;
} else if (todayFormated === jourJ) {
  document.getElementById("countdownView").innerHTML = theDay;
} else {
  document.getElementById("countdownView").innerHTML = beforeTheDay;
  initializeClock("clockdiv", deadline);
}
