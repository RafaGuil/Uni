"use strict";

import { parseHTML } from "/js/utils/parseHTML.js";

const accordionRenderer = {
    asCardAccordion: function (photos) {
        let accordionContainer = parseHTML(`<div class="accordion-item"></div>`) 
        let counter = 0;
        for (let photo of photos) {
            let header = parseHTML(`<h2 class="accordion-header" id="heading${counter}"></h2>`)
            let button = parseHTML(`<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${counter}" aria-expanded="true" aria-controls="collapse${counter}">${photo.title}</button>`)
            accordionContainer.appendChild(header)
            header.appendChild(button)
            let collapseOne = parseHTML(`<div id="collapse${counter}" class="accordion-collapse collapse " aria-labelledby="heading${counter}" data-bs-parent="#accordionExample"></div>`)
            accordionContainer.appendChild(collapseOne)
            let body = parseHTML(`<div class="accordion-body" style="color: black">
                                    <img src="${photo.url}" class="img-fluid" style="width: 100%">
                                    <br>
                                    <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                                </div>`)
            collapseOne.appendChild(body)
            counter += 1
        }
        return accordionContainer;
    }
};

export { accordionRenderer };