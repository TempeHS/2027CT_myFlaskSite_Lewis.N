document.addEventListener("DOMContentLoaded", () => {
  // --- Existing Scroll Reveal Observer Code ---
  const elements = document.querySelectorAll(".reveal-on-scroll");
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("reveal-active");
        }
      });
    },
    { threshold: 0.15 },
  );
  elements.forEach((el) => observer.observe(el));

  // --- NEW: Navbar Scrolling Fade Listener ---
  const navbar = document.querySelector(".navbar");

  window.addEventListener("scroll", () => {
    // If user scrolls past 50 pixels down, add the class, otherwise clear it
    if (window.scrollY > 50) {
      navbar.classList.add("navbar-scrolled");
    } else {
      navbar.classList.remove("navbar-scrolled");
    }
  });
});
