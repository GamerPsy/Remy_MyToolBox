const beforeTheDay =
  '<div id="clockdiv" style="max-height: 25px;font-family: sans-serif;color: #fff;font-weight: 100;text-align: center;font-size: 30px;">' +
  '<div style="padding: 10px;border-radius: 3px;background: #00BF96;display: inline-block;">' +
  '<span style="padding: 15px;border-radius: 3px;background: #00816A;display: inline-block;" class="days"></span>' +
  '<div style="padding-top: 5px;font-size: 16px;">Days</div>' +
  "</div>" +
  '<div style="padding: 10px;border-radius: 3px;background: #00BF96;display: inline-block;">' +
  '<span style="padding: 15px;border-radius: 3px;background: #00816A;display: inline-block;" class="hours"></span>' +
  '<div style="padding-top: 5px;font-size: 16px;">Hours</div>' +
  "</div>" +
  '<div style="padding: 10px;border-radius: 3px;background: #00BF96;display: inline-block;">' +
  '<span style="padding: 15px;border-radius: 3px;background: #00816A;display: inline-block;" class="minutes"></span>' +
  '<div style="padding-top: 5px;font-size: 16px;">Minutes</div>' +
  "</div>" +
  '<div style="padding: 10px;border-radius: 3px;background: #00BF96;display: inline-block;">' +
  '<span style="padding: 15px;border-radius: 3px;background: #00816A;display: inline-block;" class="seconds"></span>' +
  '<div style="padding-top: 5px;font-size: 16px;">Seconds</div>' +
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
