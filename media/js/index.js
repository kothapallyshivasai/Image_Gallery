function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var toggleButton = document.getElementById("toggleButton");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleButton.innerHTML = '<img src="/media/icons/hide_password.png" style="height: 20px; width: 20px;" alt="hide" />';
    } else {
        passwordInput.type = "password";
        toggleButton.innerHTML = '<img src="/media/icons/show_password.png" style="height: 20px; width: 20px;" alt="show" />';
    }
}