document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    alert('Your message has been sent!');
    // Optional: You can add logic to send the data to the Flask backend
});
