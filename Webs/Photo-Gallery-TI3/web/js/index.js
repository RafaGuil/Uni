"use strict"

import { galleryRenderer } from "/js/renderers/gallery.js";
import { accordionRenderer } from "/js/renderers/accordion.js";
import { messageRenderer } from "/js/renderers/messages.js";
import { photoswithusersAPI_auto } from "/js/api/_photoswithusers.js";

async function main() {
    loadPhotos();
}

async function loadPhotos() {

    let galleryContainer = document.getElementById("gallery");

    try {
        let photos = await photoswithusersAPI_auto.getAll();
        console.log(photos);

        let galleryRen = galleryRenderer.asCardGallery(photos);
        console.log(galleryRen);
        galleryContainer.appendChild(galleryRen);

        let accordionRen = accordionRenderer.asCardAccordion(photos);
        console.log(accordionRen);
        galleryContainer.appendChild(accordionRen);


        document.dispatchEvent(new CustomEvent("galleryRendered"));

    } catch (error) {
        messageRenderer.showErrorMessage("Error al cargar la galería", error);
    }

}

document.addEventListener("DOMContentLoaded", main);