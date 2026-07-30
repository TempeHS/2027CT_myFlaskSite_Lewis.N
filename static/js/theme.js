// =================================
// THE SILK WEB THEME SYSTEM
// =================================

const STORAGE_KEY = "silkweb-theme";

const html = document.documentElement;
const body = document.body;

const toggle = document.getElementById("themeToggle");
const icon = document.getElementById("themeIcon");

// Apply Theme
function applyTheme(theme) {
  html.setAttribute("data-theme", theme);

  localStorage.setItem(STORAGE_KEY, theme);

  if (icon && toggle) {
    if (theme === "light") {
      icon.className = "bi bi-sun-fill";

      toggle.classList.remove("btn-outline-light");

      toggle.classList.add("btn-outline-dark");
    } else {
      icon.className = "bi bi-moon-stars-fill";

      toggle.classList.remove("btn-outline-dark");

      toggle.classList.add("btn-outline-light");
    }
  }
}

// Load saved theme
const savedTheme = localStorage.getItem(STORAGE_KEY);

if (savedTheme) {
  applyTheme(savedTheme);
} else {
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  applyTheme(prefersDark ? "dark" : "light");
}

// Toggle button

if (toggle) {
  toggle.addEventListener("click", () => {
    const current = html.getAttribute("data-theme");

    if (current === "dark") {
      applyTheme("light");
    } else {
      applyTheme("dark");
    }
  });
}

// ===============================
// PAGE ANIMATION
// ===============================

window.addEventListener("load", () => {
  body.classList.add("page-loaded");
});

// ===============================
// NAVBAR SCROLL EFFECT
// ===============================

const navbar = document.getElementById("mainNavbar");

window.addEventListener("scroll", () => {
  if (!navbar) return;

  if (window.scrollY > 20) {
    navbar.classList.add("navbar-scrolled");
  } else {
    navbar.classList.remove("navbar-scrolled");
  }
});

// ===============================
// Keyboard shortcut D
// ===============================

document.addEventListener("keydown", (event) => {
  const activeElement = document.activeElement;

  // Ignore shortcut when typing
  if (
    activeElement.tagName === "INPUT" ||
    activeElement.tagName === "TEXTAREA" ||
    activeElement.isContentEditable
  ) {
    return;
  }

  if (
    event.key.toLowerCase() === "d" &&
    !event.ctrlKey &&
    !event.altKey &&
    !event.metaKey
  ) {
    if (toggle) {
      toggle.click();
    }
  }
});
