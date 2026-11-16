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
});

