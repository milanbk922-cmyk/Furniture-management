function openSidebar(){
    document.getElementById("sidebar").classList.add("active")
    document.getElementById("sidebarOverlay").classList.add("active")
}

function closeSidebar(){
    document.getElementById("sidebar").classList.remove("active")
    document.getElementById("sidebarOverlay").classList.remove("active")
}