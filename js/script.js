document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contactForm");

    if (!form) {
        return;
    }

    form.addEventListener("submit", (event) => {
        event.preventDefault();

        const name = document.getElementById("name").value.trim();
        const successMessage = document.getElementById("successMessage");

        successMessage.innerText = `Thank you ${name}! Your message has been sent.`;
        form.reset();
    });
});

