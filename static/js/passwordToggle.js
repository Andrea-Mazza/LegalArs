document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.getElementById("password");
    const passwordInput1 = document.getElementById("password1");

    const passField = [];
    passField.push(passwordInput);
    passField.push(passwordInput1);
    const passwordToggle = document.getElementById("password-toggle");

    passwordToggle.addEventListener("click", function () {
        for (let i = 0; i < passField.length; i++) {
            if (passField[i]) {
                if (passField[i].type === "password") {
                    passField[i].type = "text";
                } else {
                    passField[i].type = "password";
                }
            }
        }
    });


})