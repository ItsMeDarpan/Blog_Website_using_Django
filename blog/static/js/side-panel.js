document.addEventListener("DOMContentLoaded", function () {
    const profileButton = document.querySelector(".profile-button");
    const dropdownContent = document.querySelector(".dropdown-content");

    if (profileButton && dropdownContent) {
        // Toggle dropdown on button click
        profileButton.addEventListener("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
            dropdownContent.classList.toggle("show");
            this.classList.toggle("active");
            console.log('Dropdown clicked'); // Debug line
        });

        // Close dropdown when clicking outside
        document.addEventListener("click", function (e) {
            if (!profileButton.contains(e.target) && !dropdownContent.contains(e.target)) {
                dropdownContent.classList.remove("show");
                profileButton.classList.remove("active");
            }
        });

        // Prevent dropdown from closing when clicking inside it
        dropdownContent.addEventListener('click', function(e) {
            e.stopPropagation();
        });
    } else {
        console.log('Profile button or dropdown not found'); // Debug line
    }
});
