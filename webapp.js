
// Display a message when a service button is clicked
const serviceButtons = document.querySelectorAll("[data-service]");
const serviceAlert = document.getElementById("serviceAlert");

serviceButtons.forEach(function(button) {
    button.addEventListener("click", function() {
        const serviceName = button.dataset.service;

        serviceAlert.textContent =
            "You selected " + serviceName + ". Thank you for your interest!";

        serviceAlert.classList.remove("d-none");
    });
});

// Handle contact form submission
const contactForm = document.getElementById("contactForm");
const formAlert = document.getElementById("formAlert");

contactForm.addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    if (name === "" || email === "" || message === "") {
        formAlert.textContent = "Please fill in all fields.";
        formAlert.className = "alert alert-danger mt-3";
        return;
    }

    formAlert.textContent =
        "Thank you, " + name + "! Your form was submitted successfully.";

    formAlert.className = "alert alert-success mt-3";

    contactForm.reset();
});
