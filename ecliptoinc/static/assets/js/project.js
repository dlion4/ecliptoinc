/* Project specific Javascript goes here. */
const stickySidebar = document.getElementById("sticky-sidebar");
// Get the initial top offset of the sticky section
const stickySidebarOffset = stickySidebar.offsetTop;

// Function to change position to static when section reaches the top
function checkScroll() {
  if (window.pageYOffset >= stickySectionOffset) {
    stickySidebar.style.position = "static";
  } else {
    stickySidebar.style.position = "sticky";
  }
}

// Add scroll event listener to check scroll position
window.addEventListener("scroll", checkScroll);
// window.removeEventListener("scroll", checkScroll);
