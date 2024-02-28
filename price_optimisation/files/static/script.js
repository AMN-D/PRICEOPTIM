let lastScrollTop = 0;
const header = document.querySelector('.base-header');
const headerHeight = header.offsetHeight;
const scrollThreshold = 200; 

window.addEventListener("scroll", function () {
  let currentScroll = window.pageYOffset || document.documentElement.scrollTop;
  if (currentScroll > lastScrollTop && currentScroll > scrollThreshold) {
    header.style.transform = `translateY(-${headerHeight}px)`;
    header.style.transition = "transform 0.3s ease"; 
  } else if (currentScroll < lastScrollTop && currentScroll < scrollThreshold - headerHeight) {
    header.style.transform = "translateY(0)";
    header.style.transition = "transform 0.3s ease"; 
  }

  lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
}, false);

document.addEventListener("DOMContentLoaded", function() {
    const sampleLink = document.querySelector('a[href="#"]');
    const offset = 695;

    sampleLink.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default link behavior
        const targetPosition = this.parentElement.offsetTop + offset;
        window.scrollTo({
            top: targetPosition,
            behavior: "smooth"
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
  const sampleLink = document.querySelector('a[href="##"]');
  const offset = 900;
  const additionalScroll = 99999; // Additional scroll value

  sampleLink.addEventListener("click", function(event) {
      event.preventDefault(); // Prevent the default link behavior
      const targetPosition = this.parentElement.offsetTop + offset + additionalScroll; // Modify target position
      window.scrollTo({
          top: targetPosition,
          behavior: "smooth"
      });
  });
});


