document.addEventListener("DOMContentLoaded", function () {

    /* ========================================
       HEADER - SCROLLGEDRAG
    ======================================== */

    const header = document.querySelector(".site-header");

    if (header) {

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

    }


    /* ========================================
       HEADER - MOBIEL MENU
    ======================================== */

    const menuButton =
        document.querySelector(".mobiel-menu-knop");

    const navigation =
        document.querySelector(".hoofdnavigatie");


    if (
        menuButton &&
        navigation
    ) {

        menuButton.addEventListener(
            "click",
            function () {

                const menuIsOpen =
                    navigation.classList.toggle("is-open");

                menuButton.classList.toggle(
                    "is-open",
                    menuIsOpen
                );

                menuButton.setAttribute(
                    "aria-expanded",
                    menuIsOpen ? "true" : "false"
                );

            }
        );


        /* Menu sluiten wanneer op een link wordt geklikt */

        const menuLinks =
            navigation.querySelectorAll("a");

        menuLinks.forEach(function (link) {

            link.addEventListener(
                "click",
                function () {

                    if (window.innerWidth <= 950) {

                        navigation.classList.remove(
                            "is-open"
                        );

                        menuButton.classList.remove(
                            "is-open"
                        );

                        menuButton.setAttribute(
                            "aria-expanded",
                            "false"
                        );

                    }

                }
            );

        });

    }


    /* ========================================
       HEADER - DIENSTEN DROPDOWN DESKTOP
    ======================================== */

    const dropdown =
        document.querySelector(".navigatie-dropdown");

    const dropdownButton =
        document.querySelector(
            ".navigatie-dropdown-knop"
        );


    if (
        dropdown &&
        dropdownButton
    ) {

        dropdownButton.addEventListener(
            "click",
            function (event) {

                if (window.innerWidth > 950) {

                    event.preventDefault();

                    const dropdownIsOpen =
                        dropdown.classList.toggle(
                            "is-open"
                        );

                    dropdownButton.setAttribute(
                        "aria-expanded",
                        dropdownIsOpen
                            ? "true"
                            : "false"
                    );

                }

            }
        );

    }


    /* ========================================
       HEADER - KLIK BUITEN MENU
    ======================================== */

    document.addEventListener(
        "click",
        function (event) {

            if (
                dropdown &&
                dropdownButton &&
                !dropdown.contains(event.target)
            ) {

                dropdown.classList.remove(
                    "is-open"
                );

                dropdownButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

            }


            if (
                header &&
                navigation &&
                menuButton &&
                navigation.classList.contains(
                    "is-open"
                ) &&
                !header.contains(event.target)
            ) {

                navigation.classList.remove(
                    "is-open"
                );

                menuButton.classList.remove(
                    "is-open"
                );

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

            }

        }
    );


    /* ========================================
       HEADER - ESC
    ======================================== */

    document.addEventListener(
        "keydown",
        function (event) {

            if (event.key !== "Escape") {
                return;
            }

            if (
                navigation &&
                menuButton
            ) {

                navigation.classList.remove(
                    "is-open"
                );

                menuButton.classList.remove(
                    "is-open"
                );

                menuButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

            }

            if (
                dropdown &&
                dropdownButton
            ) {

                dropdown.classList.remove(
                    "is-open"
                );

                dropdownButton.setAttribute(
                    "aria-expanded",
                    "false"
                );

            }

        }
    );


    /* ========================================
       PACKSHOTFOTOGRAFIE - LIGHTBOX
    ======================================== */

    const packshotImages =
        document.querySelectorAll(
            ".packshot-gallery img, .packshot-voorbeeld__beeld img"
        );

    if (!packshotImages.length) {
        return;
    }


    const lightbox =
        document.createElement("div");

    lightbox.className =
        "packshot-lightbox";

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
        lightbox.querySelector(
            ".packshot-lightbox__image"
        );

    const closeButton =
        lightbox.querySelector(
            ".packshot-lightbox__close"
        );


    function openLightbox(image) {

        lightboxImage.src = image.src;
        lightboxImage.alt = image.alt || "";

        lightbox.classList.add("is-open");

        document.body.style.overflow =
            "hidden";

    }


    function closeLightbox() {

        lightbox.classList.remove(
            "is-open"
        );

        document.body.style.overflow =
            "";

        setTimeout(function () {

            if (
                !lightbox.classList.contains(
                    "is-open"
                )
            ) {
                lightboxImage.src = "";
            }

        }, 250);

    }


    packshotImages.forEach(
        function (image) {

            image.addEventListener(
                "click",
                function () {
                    openLightbox(image);
                }
            );

        }
    );


    closeButton.addEventListener(
        "click",
        function () {
            closeLightbox();
        }
    );


    lightbox.addEventListener(
        "click",
        function (event) {

            if (event.target === lightbox) {
                closeLightbox();
            }

        }
    );


    document.addEventListener(
        "keydown",
        function (event) {

            if (
                event.key === "Escape" &&
                lightbox.classList.contains(
                    "is-open"
                )
            ) {
                closeLightbox();
            }

        }
    );

});