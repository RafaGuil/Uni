"use strict"

import { galleryRenderer } from "/js/renderers/gallery.js";

function main() {

    let button = document.getElementById("test-button");
    button.onclick = clickHandler;


    let container = document.getElementById("gallery");
    let photos = [
        {
            title: "Samoyed",
            description: "A very good boy.",
            userId: 1,
            url: "https://i.ibb.co/tY1Jcnc/wlZCfCv.jpg",
            date: "15/08/2020",
        },
        {
            title: "ETSII",
            description: "E.T.S. Ing. Informatica, Universidad de Sevilla",
            userId: 2,
            url: "images/gato.webp",
            date: "01/01/2021",
        },
        {
            title: "Seville",
            description: "The beautiful city of Seville",
            userId: 3,
            url: "images/gato.webp",
            date: "03/02/2019",
        },
        {
            title: "Abstract art",
            description: "Clipart",
            userId: 4,
            url: "images/example.jpg",
            date: "14/08/2019",
        },
    ];
    let gallery = galleryRenderer.asCardGallery(photos);
    container.appendChild(gallery);

    let cards = document.getElementsByClassName("card");
    for (let card of cards) {
        console.log("aaaaaaaaaaaaa")
        card.onmouseenter = handleMouseEnter;
        card.onmouseleave = handleMouseLeave;
    }
}

function clickHandler(event) {
    let myT = event.target;
    alert(myT.textContent);
}

function handleMouseEnter(event) {
    let card = event.target;
    card.style.border = "6px solid blue"
}

function handleMouseLeave(event) {
    let card = event.target;
    card.style.border = "none";
}

document.addEventListener("DOMContentLoaded", main);

