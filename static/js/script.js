// =====================================
// THE SILK WEB MAIN SCRIPT
// =====================================

// Prevent duplicate script loading
if (!window.silkWebLoaded) {
  window.silkWebLoaded = true;

  // =====================================
  // LIVE SEARCH SUGGESTIONS
  // =====================================

  const searchInput = document.getElementById("liveSearchInput");
  const searchResults = document.getElementById("searchSuggestions");

  if (searchInput && searchResults) {
    searchInput.addEventListener("input", async function () {
      const query = searchInput.value.trim();

      if (query.length < 2) {
        searchResults.style.display = "none";
        return;
      }

      try {
        const response = await fetch(
          `/api/search?q=${encodeURIComponent(query)}`,
        );

        const data = await response.json();

        searchResults.innerHTML = "";

        if (data.results.length === 0) {
          searchResults.style.display = "none";
          return;
        }

        data.results.forEach((result) => {
          const item = document.createElement("div");

          item.className = "search-result";

          item.textContent = result.name;

          item.onclick = function () {
            window.location.href = result.url;
          };

          searchResults.appendChild(item);
        });

        searchResults.style.display = "block";
      } catch (error) {
        console.error("Search error:", error);
      }
    });

    document.addEventListener("click", function (event) {
      if (
        !searchInput.contains(event.target) &&
        !searchResults.contains(event.target)
      ) {
        searchResults.style.display = "none";
      }
    });
  }

  // =====================================
  // PAGE LOAD ANIMATION
  // =====================================

  window.addEventListener("load", () => {
    document.body.classList.add("page-loaded");
  });

  // =====================================
  // NAVBAR SCROLL EFFECT
  // =====================================

  const mainNavbar = document.getElementById("mainNavbar");

  window.addEventListener("scroll", () => {
    if (!mainNavbar) return;

    if (window.scrollY > 30) {
      mainNavbar.classList.add("navbar-scrolled");
    } else {
      mainNavbar.classList.remove("navbar-scrolled");
    }
  });

  // =====================================
  // FEATURE CARD CLICK EFFECT
  // =====================================

  document.querySelectorAll(".feature-card").forEach((card) => {
    card.addEventListener("click", () => {
      const link = card.dataset.link;

      if (link) {
        window.location.href = link;
      }
    });
  });

  // =====================================
  // PARALLAX SCROLL EFFECT
  // =====================================

  const parallaxElements = document.querySelectorAll(
    ".parallax, .parallax-card",
  );

  window.addEventListener("scroll", () => {
    const scrollY = window.scrollY;

    parallaxElements.forEach((element) => {
      const speed = element.dataset.speed || 0.2;

      element.style.transform = `translateY(${scrollY * speed}px)`;
    });
  });

  // =====================================
  // BACK TO TOP BUTTON
  // =====================================

  const backToTopButton = document.getElementById("backToTop");

  if (backToTopButton) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 300) {
        backToTopButton.classList.add("show");
      } else {
        backToTopButton.classList.remove("show");
      }
    });

    backToTopButton.addEventListener("click", () => {
      window.scrollTo({
        top: 0,

        behavior: "smooth",
      });
    });
  }
}
