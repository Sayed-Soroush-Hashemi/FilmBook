function setElementAlarmed(element, alarmText) {
    element.style.backgroundColor = "rgb(255, 50, 50)";
    element.setAttribute("title", alarmText);
}
function clearElementAlarm(element) {
    element.style.backgroundColor = "";
    element.setAttribute("title", "");
}
function focusGained() {
    this.select();
}
function checkUsername() {
    var usernameElement = document.getElementById("username");
    var username = usernameElement.value;
    var regex = new RegExp("^[a-zA-Z0-9]+$");
    if(regex.test(username) === false) {
        setElementAlarmed(usernameElement, "Just english alphabet characters and digits");
        return false;
    }
    clearElementAlarm(usernameElement);
    return true;
}
function checkPassword() {
    var passwordElement = document.getElementById("password");
    var password = passwordElement.value;
    var security = 0;
    var security_limit = 4;
    var regex = new RegExp("\\d");
    security += regex.test(password);
    regex = new RegExp("[a-z]");
    security += regex.test(password);
    regex = new RegExp("[A-Z]");
    security += regex.test(password);
    security += (password.length > 8);
    if (security < security_limit) {
        setElementAlarmed(passwordElement, "must contain at least one digit, one lower case and one upper case character. \nShould be at least 8 characters.");
        return false;
    }
    clearElementAlarm(passwordElement);
    return true;
}
function checkConfirmPassword() {
    var confirmPasswordElement = document.getElementById("confirmPassword");
    var confirmPassword = confirmPasswordElement.value;
    var password = document.getElementById("password").value;
    if (confirmPassword !== password) {
        setElementAlarmed(confirmPasswordElement, "doesn't match with password");
        return false;
    }
    clearElementAlarm(confirmPasswordElement);
    return true;
}
function checkNickName() {
    var nickNameElement = document.getElementById("nickName");
    var nickName = nickNameElement.value;
    var regex = new RegExp("^[A-Za-z0-9]+$");
    if (regex.test(nickName) === false) {
        setElementAlarmed(nickNameElement, "just engilsh alphabet characters and digits");
        return false;
    }
    clearElementAlarm(nickNameElement);
    return true;
}
function checkEmail() {
    var emailElement = document.getElementById("email");
    var email = emailElement.value;
    var regex = new RegExp("^[a-zA-Z0-9]+@[a-zA-Z0-9]+\\.[a-zA-Z0-9]+$");
    if (regex.test(email) === false) {
        setElementAlarmed(emailElement, "invalid email");
        return false;
    }
    clearElementAlarm(emailElement);
    return true;
}
function checkBirthDate() {
    var birthDateElement = document.getElementById("birthDate");
    var birthDate = birthDateElement.value;
    var regex = new RegExp("\\d{4}\\-\\d{2}\\-\\d{2}");
    if (regex.test(birthDate) === false) {
        setElementAlarmed(birthDateElement, "invalid birth date");
        return false;
    }
    console.log(birthDate);
    clearElementAlarm(birthDateElement);
    return true;
}