function wrongIdentification() {
    if(document.getElementById("error") !== null)
        return
    var container = document.getElementById("container")
    var error = document.createElement("span")
    error.innerText = "Wrong Username/Password"
    error.setAttribute("id", "error")
    error.style.color = "Red"
    container.getElementsByTagName("form")[0].appendChild(error)
    document.getElementById("user").style.backgroundColor = "Red"
    document.getElementById("pass").style.backgroundColor = "Red"
}