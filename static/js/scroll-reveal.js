// =====================================
// THE SILK WEB PARALLAX SYSTEM
// =====================================

const parallaxElements = document.querySelectorAll(".parallax");

function updateParallax() {
  const scrollPosition = window.scrollY;

  parallaxElements.forEach((element) => {
    const speed = element.dataset.speed || 0.3;

    const offset = scrollPosition * speed;

    element.style.transform = `translateY(${offset}px)`;
  });
}

window.addEventListener("scroll", updateParallax);
