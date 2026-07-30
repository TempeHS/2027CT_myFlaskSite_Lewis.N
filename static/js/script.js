// =====================================
// THE SILK WEB MAIN SCRIPT
// =====================================

// =====================================
// LIVE SEARCH SUGGESTIONS
// =====================================

const searchInput = document.getElementById("liveSearchInput");
const searchResults = document.getElementById("searchSuggestions");

if (searchInput && searchResults) {
  searchInput.addEventListener("input", async function () {
    const query = searchInput.value.trim();

    // Hide if empty

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

        item.textContent = result.title;

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

  // Close search when clicking away

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

const navbar = document.getElementById("mainNavbar");

window.addEventListener("scroll", () => {
  if (!navbar) return;

  if (window.scrollY > 30) {
    navbar.classList.add("navbar-scrolled");
  } else {
    navbar.classList.remove("navbar-scrolled");
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
