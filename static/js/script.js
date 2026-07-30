// =====================================
// THE SILK WEB MAIN SCRIPT
// =====================================

document.addEventListener("DOMContentLoaded", () => {
  // =====================================
  // LIVE SEARCH
  // =====================================

  const searchInput = document.getElementById("liveSearch");
  const searchResults = document.getElementById("searchResults");

  if (searchInput && searchResults) {
    searchInput.addEventListener("input", async () => {
      const query = searchInput.value.trim();

      if (query.length < 2) {
        searchResults.style.display = "none";
        searchResults.innerHTML = "";
        return;
      }

      try {
        const response = await fetch(
          `/api/search?q=${encodeURIComponent(query)}`,
        );

        const data = await response.json();

        searchResults.innerHTML = "";

        if (!data.results || data.results.length === 0) {
          searchResults.style.display = "none";
          return;
        }

        data.results.forEach((result) => {
          const item = document.createElement("a");

          item.className = "search-result-item";
          item.href = result.url;
          item.textContent = result.name;

          searchResults.appendChild(item);
        });

        searchResults.style.display = "block";
      } catch (err) {
        console.error(err);
      }
    });

    document.addEventListener("click", (e) => {
      if (
        !searchInput.contains(e.target) &&
        !searchResults.contains(e.target)
      ) {
        searchResults.style.display = "none";
      }
    });
  }

  // =====================================
  // NAVBAR SCROLL
  // =====================================

  const navbar = document.getElementById("mainNavbar");

  function updateNavbar() {
    if (!navbar) return;

    if (window.scrollY > 30) {
      navbar.classList.add("navbar-scrolled");
    } else {
      navbar.classList.remove("navbar-scrolled");
    }
  }

  updateNavbar();

  window.addEventListener("scroll", updateNavbar);

  // =====================================
  // PARALLAX
  // =====================================

  const parallax = document.querySelectorAll(".parallax, .parallax-card");

  function updateParallax() {
    const scroll = window.scrollY;

    parallax.forEach((el) => {
      const speed = Number(el.dataset.speed || 0.08);

      el.style.transform = `translateY(${scroll * speed}px)`;
    });
  }

  if (parallax.length) {
    window.addEventListener("scroll", updateParallax);
  }

  // =====================================
  // BACK TO TOP
  // =====================================

  const backToTop = document.getElementById("backToTop");

  if (backToTop) {
    function updateButton() {
      if (window.scrollY > 300) {
        backToTop.classList.add("show");
      } else {
        backToTop.classList.remove("show");
      }
    }

    updateButton();

    window.addEventListener("scroll", updateButton);

    backToTop.addEventListener("click", () => {
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    });
  }

  // =====================================
  // PAGE LOADER
  // =====================================

  const loader = document.getElementById("pageLoader");

  if (loader) {
    window.addEventListener("load", () => {
      loader.classList.add("hide");

      setTimeout(() => {
        loader.remove();
      }, 500);
    });
  }

  // =====================================
  // PAGE TRANSITIONS
  // =====================================

  const transition = document.getElementById("pageTransition");

  if (transition) {
    document.body.addEventListener("click", (e) => {
      const link = e.target.closest("a");

      if (!link) return;

      const href = link.getAttribute("href");

      if (
        !href ||
        href.startsWith("#") ||
        href.startsWith("http") ||
        link.target === "_blank" ||
        link.hasAttribute("download")
      ) {
        return;
      }

      e.preventDefault();

      transition.classList.add("active");

      setTimeout(() => {
        window.location.href = href;
      }, 300);
    });
  }

  // =====================================
  // RESTORE AFTER CHROME BACK BUTTON
  // =====================================

  window.addEventListener("pageshow", () => {
    updateNavbar();

    if (backToTop) {
      if (window.scrollY > 300) {
        backToTop.classList.add("show");
      } else {
        backToTop.classList.remove("show");
      }
    }

    if (parallax.length) {
      updateParallax();
    }
  });
});
