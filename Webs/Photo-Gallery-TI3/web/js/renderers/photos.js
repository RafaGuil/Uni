"use strict";

import { parseHTML } from "/js/utils/parseHTML.js";

const photoRenderer = {
    asCard: function(photo) {
        let html = `<div class="col col-md-4">
                <div class="card bg-dark text-light">
                    <a href="photo_detail.html">
                        <img src=${photo.url} class="card-img-top">
                    </a>
                    <div class="card-body">
                        <h5 class="card-title text-center">${photo.title}</h5>
                        <p class="card-text">${photo.description}</p>
                        <p class="text-end">${photo.userId}</p>
                    </div>
                </div>
            </div>`

        let newCard = parseHTML(html);
        return newCard;
    }
};

export { photoRenderer };