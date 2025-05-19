"use strict"

import { messageRenderer } from "/js/renderers/messages.js";
import { userValidator } from "/js/validators/users_login.js";
import { authAPI_auto } from "/js/api/_auth.js"
import { sessionManager } from "/js/utils/session.js";

function main() {
    let myform = document.getElementById("log-form");
    myform.onsubmit = handleSubmitLogin;

}

function handleSubmitLogin(event) {
    event.preventDefault();
    let form = event.target;
    let formData = new FormData(form);
    let errors = userValidator.validateRegister(formData);
    if (errors.length > 0) {
        let errorsDiv = document.getElementById("errors");
        errorsDiv.innerHTML = "";
        for (let error of errors) {
            messageRenderer.showErrorMessage(error);
        }
    } else {
        sendLogin(formData);
    }
}

async function sendLogin(formData) {
    try {
        let loginData = await authAPI_auto.login(formData); //Cambia esto en diferencia del register.js
        let sessionToken = loginData.sessionToken;
        let loggedUser = loginData.user;
        sessionManager.login(sessionToken, loggedUser);
        window.location.href = "index.html";
    } catch (err) {
        messageRenderer.showErrorMessage("Error registering a new user", err);
    }
}

document.addEventListener("DOMContentLoaded", main);
