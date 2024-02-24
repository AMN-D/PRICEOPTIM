let lastScrollTop = 0;
const header = document.querySelector('.base-header');
const headerHeight = header.offsetHeight; // Get the height of the header
const scrollThreshold = 100; // Adjust this value to set the scroll threshold

window.addEventListener("scroll", function() {
    let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
    if (currentScroll > lastScrollTop && currentScroll > scrollThreshold) {
        // Scroll down and below the threshold, hide the header
        header.style.transform = "translateY(-100%)";
        header.style.transition = "transform 0.3s ease"; // Add animation
    } else {
        // Scroll up or not yet reached the threshold, show the header
        header.style.transform = "translateY(0)";
        header.style.transition = "transform 0.3s ease"; // Add animation
    }
    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
}, false);

const scrollButton = document.getElementById("scrollButton");
scrollButton.addEventListener("click", function() {
  const targetDiv = document.querySelector(".body-main-anal-black");
  const offset = 150; 
  const targetPosition = targetDiv.offsetTop + offset;
  window.scrollTo({
    top: targetPosition,
    behavior: "smooth"
  });
});

document.addEventListener("DOMContentLoaded", function() {
    const sampleLink = document.querySelector('a[href="#"]');
    const offset = 700;

    sampleLink.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default link behavior
        const targetPosition = this.parentElement.offsetTop + offset;
        window.scrollTo({
            top: targetPosition,
            behavior: "smooth"
        });
    });
});

