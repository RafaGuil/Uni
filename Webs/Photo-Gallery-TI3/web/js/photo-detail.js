"use strict"

import { sessionManager } from "/js/utils/session.js";


function main() {
    showUser();
    addLogoutHandler();
    // hideActionsColumn();
    desactiveButton();
}

function showUser() {
    let title = document.getElementById("navbar-title");
    let text;
    if (sessionManager.isLogged()) {
        let username = sessionManager.getLoggedUser().username;
        text = "Hi, @" + username;
    } else {
        text = "Guest";
    }
    title.textContent = text;
}

function addLogoutHandler() {
    let logoutButton = document.getElementById("navbar-logout");
    logoutButton.onclick = function () {
        sessionManager.logout();
        window.location.href = "index.html";
    };
}

// function hideActionsColumn() {
//     let actions_col = document.getElementById("actions-col");
//     if (!sessionManager.isLogged()) {
//         actions_col.style.display = "none";
//     }
// }

function desactiveButton() {
    let buttons = document.getElementsByClassName("accordion-button");
    if (!sessionManager.isLogged()) {
        for (let button of buttons) {
            button.removeAttribute("data-bs-target");
            button.removeAttribute("data-bs-toggle");
        }
    }
}

document.addEventListener("galleryRendered", main); // Hasta que no se activa el dispatchEvent de index.js, no funciona main