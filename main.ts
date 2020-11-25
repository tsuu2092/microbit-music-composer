input.onButtonPressed(Button.A, function () {
    if (role == "admin") {
        radio.sendString("user")
    }
})
radio.onReceivedString(function (receivedString) {
    role = "user"
})
input.onButtonPressed(Button.B, function () {
    basic.showString(role)
})
let role = ""
role = "admin"
