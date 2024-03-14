document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Get form data
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;
    // Send POST request to backend server
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password, email })
    })
    .then(response => {
        if (response.ok) {
            // Registration successful, redirect to login page
            window.location.href = '/login.html';
        } else {
            // Handle registration error
            console.error('Registration failed');
        }
    })
    .catch(error => console.error('Error:', error));
});
