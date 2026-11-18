document.addEventListener("DOMContentLoaded", function() {
    const adminLink = document.querySelector(".admin-trigger-link");
    const modal = document.getElementById("adminModal");
    const closeModal = document.getElementById("closeModal");
    const adminBtn = document.querySelector(".admin-btn"); // Select your admin button

    // Open modal when the admin link is clicked
    if (adminLink) {
        adminLink.addEventListener("click", function(e) {
            e.preventDefault();
            modal.classList.add("active");
        });
    }

    // Close modal when clicking 'Cancel'
    if (closeModal) {
        closeModal.addEventListener("click", function() {
            modal.classList.remove("active");
        });
    }

    // Close modal when clicking "I'M AN ADMIN" (since it opens in a new tab)
    if (adminBtn) {
        adminBtn.addEventListener("click", function() {
            modal.classList.remove("active");
        });
    }

    // Close modal if clicking outside the modal box
    window.addEventListener("click", function(e) {
        if (e.target === modal) {
            modal.classList.remove("active");
        }
    });

    // ===== Mobile menu (hamburger) =====
    const nav = document.querySelector("nav");
    const navToggle = document.getElementById("navToggle");
    const navLinks = document.getElementById("navLinks");

    // One function opens/closes the menu and keeps everything in sync:
    // the .menu-open class (CSS shows/hides the links), the ARIA attributes
    // (screen readers), and the icon (bars <-> X).
    function setMenu(open) {
        nav.classList.toggle("menu-open", open);
        navToggle.setAttribute("aria-expanded", open);
        navToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");

        const icon = navToggle.querySelector("i");
        icon.classList.toggle("fa-bars", !open);
        icon.classList.toggle("fa-xmark", open);
    }

    if (nav && navToggle && navLinks) {
        // The button opens/closes the menu
        navToggle.addEventListener("click", function() {
            setMenu(!nav.classList.contains("menu-open"));
        });

        // Tapping a link inside the menu closes it
        navLinks.addEventListener("click", function(e) {
            if (e.target.closest("a")) {
                setMenu(false);
            }
        });

        // Tapping anywhere outside the nav closes it
        document.addEventListener("click", function(e) {
            if (!nav.contains(e.target)) {
                setMenu(false);
            }
        });

        // Escape key closes it
        document.addEventListener("keydown", function(e) {
            if (e.key === "Escape") {
                setMenu(false);
            }
        });

        // If the window grows past the mobile breakpoint (same 992px as the CSS),
        // reset the menu so it isn't left "open" when the desktop nav comes back
        const desktopQuery = window.matchMedia("(min-width: 993px)");
        desktopQuery.addEventListener("change", function(e) {
            if (e.matches) {
                setMenu(false);
            }
        });
    }
});
