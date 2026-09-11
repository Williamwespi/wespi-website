document.addEventListener("DOMContentLoaded", () => {

    const lightbox = document.getElementById("bodyform-lightbox");

    if (!lightbox) {
        return;
    }


    const afbeelding = lightbox.querySelector(
        ".bodyform-lightbox-afbeelding"
    );

    const sluitknop = lightbox.querySelector(
        ".bodyform-lightbox-sluiten"
    );

    const triggers = document.querySelectorAll(
        ".bodyform-afbeelding-knop"
    );


    let laatsteTrigger = null;


    /* =====================================================
       OPENEN
       ===================================================== */

    function openLightbox(trigger) {

        const src = trigger.dataset.lightboxSrc;
        const alt = trigger.dataset.lightboxAlt || "";

        if (!src) {
            return;
        }


        laatsteTrigger = trigger;

        afbeelding.src = src;
        afbeelding.alt = alt;

        lightbox.classList.add("is-open");

        lightbox.setAttribute(
            "aria-hidden",
            "false"
        );

        document.body.style.overflow = "hidden";

        sluitknop.focus();
    }


    /* =====================================================
       SLUITEN
       ===================================================== */

    function sluitLightbox() {

        lightbox.classList.remove("is-open");

        lightbox.setAttribute(
            "aria-hidden",
            "true"
        );

        document.body.style.overflow = "";

        afbeelding.src = "";
        afbeelding.alt = "";


        if (laatsteTrigger) {
            laatsteTrigger.focus();
        }

    }


    /* =====================================================
       AFBEELDINGEN
       ===================================================== */

    triggers.forEach((trigger) => {

        trigger.addEventListener("click", () => {

            openLightbox(trigger);

        });

    });


    /* =====================================================
       SLUITKNOP
       ===================================================== */

    sluitknop.addEventListener(
        "click",
        sluitLightbox
    );


    /* =====================================================
       KLIK OP DONKERE ACHTERGROND
       ===================================================== */

    lightbox.addEventListener("click", (event) => {

        if (event.target === lightbox) {
            sluitLightbox();
        }

    });


    /* =====================================================
       ESCAPE
       ===================================================== */

    document.addEventListener("keydown", (event) => {

        if (
            event.key === "Escape" &&
            lightbox.classList.contains("is-open")
        ) {
            sluitLightbox();
        }

    });

});