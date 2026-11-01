const calendar = document.getElementById("calendar");
const monthYear = document.getElementById("monthYear");

const today = new Date();

let currentMonth = today.getMonth();
let currentYear = today.getFullYear();

const weekdays = [
    "Sun", "Mon", "Tue", "Wed",
    "Thu", "Fri", "Sat"
];

function displayCalendar() {

    calendar.innerHTML = "";

    const firstDay = new Date(
        currentYear, currentMonth, 1
    ).getDay();

    const totalDays = new Date(
        currentYear, currentMonth + 1, 0
    ).getDate();

    const monthName = new Date(
        currentYear, currentMonth
    ).toLocaleString("en-US", { month: "long" });

    monthYear.textContent =
        monthName + " " + currentYear;

    // Display weekdays
    weekdays.forEach(day => {
        const div = document.createElement("div");
        div.className = "day-name";
        div.textContent = day;
        calendar.appendChild(div);
    });

    // Empty spaces before first date
    for (let i = 0; i < firstDay; i++) {
        const empty = document.createElement("div");
        calendar.appendChild(empty);
    }

    // Display dates
    for (let day = 1; day <= totalDays; day++) {

        const div = document.createElement("div");
        div.className = "date";
        div.textContent = day;

        const weekday = new Date(
            currentYear, currentMonth, day
        ).getDay();

        if (weekday === 6) {
            div.classList.add("saturday");
        }

        // Highlight today's date
        if (
            day === today.getDate() &&
            currentMonth === today.getMonth() &&
            currentYear === today.getFullYear()
        ) {
            div.classList.add("today");
        }

        calendar.appendChild(div);
    }
}

function changeMonth(value) {

    currentMonth += value;

    if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }

    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
    }

    displayCalendar();
}

displayCalendar();