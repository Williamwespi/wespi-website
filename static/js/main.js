document.addEventListener("DOMContentLoaded", function () {

    const header = document.querySelector(".site-header");

    if (!header) {
        return;
    }


    function updateHeader() {

        if (window.scrollY > 40) {

            header.classList.add("is-scrolled");

        } else {

            header.classList.remove("is-scrolled");

        }

    }


    updateHeader();

    window.addEventListener(
        "scroll",
        updateHeader,
        {
            passive: true
        }
    );

});
/* ========================================
   PACKSHOTFOTOGRAFIE - LIGHTBOX
======================================== */

document.addEventListener("DOMContentLoaded", function () {

    const packshotImages = document.querySelectorAll(
        ".packshot-gallery img, .packshot-voorbeeld__beeld img"
    );

    if (!packshotImages.length) {
        return;
    }


    /* Lightbox maken */

    const lightbox = document.createElement("div");

    lightbox.className = "packshot-lightbox";

    lightbox.innerHTML = `
        <button
            class="packshot-lightbox__close"
            type="button"
            aria-label="Afbeelding sluiten"
        >
            ×
        </button>

        <img
            class="packshot-lightbox__image"
            src=""
            alt=""
        >
    `;

    document.body.appendChild(lightbox);


    const lightboxImage =
        lightbox.querySelector(".packshot-lightbox__image");

    const closeButton =
        lightbox.querySelector(".packshot-lightbox__close");


    /* Openen */

    function openLightbox(image) {

        lightboxImage.src = image.src;
        lightboxImage.alt = image.alt || "";

        lightbox.classList.add("is-open");

        document.body.style.overflow = "hidden";
    }


    /* Sluiten */

    function closeLightbox() {

        lightbox.classList.remove("is-open");

        document.body.style.overflow = "";

        setTimeout(function () {

            if (!lightbox.classList.contains("is-open")) {
                lightboxImage.src = "";
            }

        }, 250);
    }


    /* Klik op productfoto */

    packshotImages.forEach(function (image) {

        image.addEventListener("click", function () {
            openLightbox(image);
        });

    });


    /* Klik op kruisje */

    closeButton.addEventListener("click", function () {
        closeLightbox();
    });


    /* Klik naast afbeelding */

    lightbox.addEventListener("click", function (event) {

        if (event.target === lightbox) {
            closeLightbox();
        }

    });


    /* ESC */

    document.addEventListener("keydown", function (event) {

        if (
            event.key === "Escape" &&
            lightbox.classList.contains("is-open")
        ) {
            closeLightbox();
        }

    });

});