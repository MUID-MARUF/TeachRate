document.getElementById("loginBtn").addEventListener("click", function() {
    // You can add validation logic here if needed
    // Example: Check if username and password are entered
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username && password) {
        // Redirect to home page after successful login (replace with your actual home page URL)
        window.location.href = "home.html";
    } else {
        alert("Please enter both username and password");
    }
});
