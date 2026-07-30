// ===============================
// The Silk Web Theme Manager
// ===============================

const body = document.body;
const html = document.documentElement;

const toggle = document.getElementById("themeToggle");
const icon = document.getElementById("themeIcon");

const STORAGE_KEY = "silkweb-theme";

// -------------------------------
// Apply Theme
// -------------------------------

function applyTheme(theme) {
  html.setAttribute("data-theme", theme);

  if (theme === "light") {
    body.classList.add("light-mode");
    body.classList.remove("dark-mode");

    icon.className = "bi bi-sun-fill";

    toggle.classList.remove("btn-outline-light");
    toggle.classList.add("btn-outline-dark");
  } else {
    body.classList.add("dark-mode");
    body.classList.remove("light-mode");

    icon.className = "bi bi-moon-stars-fill";

    toggle.classList.remove("btn-outline-dark");
    toggle.classList.add("btn-outline-light");
  }

  localStorage.setItem(STORAGE_KEY, theme);
}

// -------------------------------
// Detect Saved Theme
// -------------------------------

const savedTheme = localStorage.getItem(STORAGE_KEY);

if (savedTheme) {
  applyTheme(savedTheme);
} else {
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  applyTheme(prefersDark ? "dark" : "light");
}

// -------------------------------
// Toggle Theme
// -------------------------------

if (!toggle || !icon) {
  console.warn("Theme controls not found");
} else {
  toggle.addEventListener("click", () => {
    const currentTheme = html.getAttribute("data-theme");

    if (currentTheme === "dark") {
      applyTheme("light");
    } else {
      applyTheme("dark");
    }
  });
}
// -------------------------------
// Watch System Theme
// -------------------------------

window
  .matchMedia("(prefers-color-scheme: dark)")
  .addEventListener("change", (e) => {
    if (!localStorage.getItem(STORAGE_KEY)) {
      applyTheme(e.matches ? "dark" : "light");
    }
  });

// -------------------------------
// Smooth Page Fade
// -------------------------------

window.addEventListener("load", () => {
  body.classList.add("page-loaded");
});

// -------------------------------
// Navbar Scroll Effect
// -------------------------------

const navbar = document.getElementById("mainNavbar");

window.addEventListener("scroll", () => {
  if (window.scrollY > 20) {
    navbar.classList.add("navbar-scrolled");
  } else {
    navbar.classList.remove("navbar-scrolled");
  }
});

// -------------------------------
// Keyboard Shortcut
// Press D
// -------------------------------

document.addEventListener("keydown", (event) => {
  if (
    event.key.toLowerCase() === "d" &&
    !event.ctrlKey &&
    !event.metaKey &&
    !event.altKey
  ) {
    toggle.click();
  }
});
