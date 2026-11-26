// expandable month calendar
const openBtn = document.getElementById("openMonthPicker");
const popup = document.getElementById("monthPickerPopup");
const yearDisplay = document.getElementById("pickerYear");
const pickerData = document.getElementById("monthPickerData")

let selectedMonth = Number(pickerData.dataset.month);
let selectedYear = Number(pickerData.dataset.year);

let CurrentYear = selectedYear;

openBtn.addEventListener("click", function(event){
    event.stopPropagation();
    popup.classList.toggle("show");
    CurrentYear = selectedYear;
    updatePicker();
});
document.getElementById("prevYear").addEventListener("click", function(event){
    event.stopPropagation();
    CurrentYear--;
    updatePicker();
});
document.getElementById("nextYear").addEventListener("click", function(event){
    event.stopPropagation();
    CurrentYear++;
    updatePicker();
});

function updatePicker(){
    yearDisplay.textContent = CurrentYear;
    document.querySelectorAll(".month-option").forEach(button =>{
        const month = Number(button.dataset.month);
        button.classList.toggle(
            "selected",
            month === selectedMonth && CurrentYear === selectedYear
        );
    });
}
document.querySelectorAll(".month-option").forEach(button =>{
    button.addEventListener("click", function(event){
        event.stopPropagation();
        const month= Number(this.dataset.month);
        const url = new URL(window.location.href);
        url.searchParams.set("month", month);
        url.searchParams.set("year", CurrentYear);
        window.location.href = url.toString();
    });
});

// Close popup when clicking outside
document.addEventListener("click", function(event){
    if(
        !event.target.closest(".month-picker-container")
    ){
        popup.classList.remove("show");
    }
});