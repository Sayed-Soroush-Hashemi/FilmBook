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
function setElementAlarmed(element, alarmText) {
    element.style.backgroundColor = "rgb(255, 50, 50)";
    element.setAttribute("title", alarmText);
}
function clearElementAlarm(element) {
    element.style.backgroundColor = "";
    element.setAttribute("title", "");
}