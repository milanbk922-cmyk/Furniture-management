// expandable month calendar
const openBtn = document.getElementById("openMonthPicker");
const popup = document.getElementById("monthPickerPopup");
const yearDisplay = document.getElementById("pickerYear");

let selectedMonth = Number("{{month|default:11}} ");
let selectedYear = Number("{{year|default:2026}} ");

let currentYear = selectedYear;

openBtn.addEventListener("click", function(){
    popup.classList.toggle("show");
    currentYear = selectedYear;
    updatePicker();
});
document.getElementById("prevYear").addEventListener("click", function(){
    currentYear--;
    updatePicker();
});
document.getElementById("nextYear").addEventListener("click", function(){
    currentYear++;
    updatePicker();
});

function updatePicker(){
    yearDisplay.textContent = currentYear;
    document.querySelectorAll(".month-option").forEach(button =>{
        const month = Number(button.CDATA_SECTION_NODE.month);
        button.classList.toggle(
            "selected",
            month === selectedMonth && currentYear === selectedYear
        );
    });
}
document.querySelectorAll(".month-option").forEach(button =>{
    button.addEventListener("click", function(){
        const month= Number(this.dataset.month);
        const url = new URL(window.location.href);
        url.searchParams.set("month", month);
        url.searchParams.set("year", currentYear);
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