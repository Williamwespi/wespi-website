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

                menuButton.setAttribute("aria-label", menuIsOpen ? "Menu sluiten" : "Menu openen");
                if (window.innerWidth <= 950) {
                    resetBeeldsubmenu();
                    navigation.scrollTop = 0;
                }

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
                        menuButton.setAttribute("aria-label", "Menu openen");
                        resetBeeldsubmenu();

                    }

                }
            );

        });

    }


    /* ========================================
       HEADER - BEELD DROPDOWN
    ======================================== */

    const dropdown =
        document.querySelector(".navigatie-dropdown");

    const dropdownButton =
        document.querySelector(
            ".navigatie-dropdown-knop"
        );

    let dropdownCloseTimer;
    let dropdownPinned = false;
    let dropdownHovered = false;
    const desktopNavigation = window.matchMedia("(min-width: 951px)");

    function setBeeldsubmenu(open) {
        if (!dropdown || !dropdownButton) return;
        dropdown.classList.toggle("is-open", open);
        dropdownButton.setAttribute("aria-expanded", String(open));
    }

    function resetBeeldsubmenu() {
        clearTimeout(dropdownCloseTimer);
        dropdownPinned = false;
        dropdownHovered = false;
        setBeeldsubmenu(false);
    }

    function closeMobileNavigation(returnFocus = false) {
        if (!navigation || !menuButton) return;
        navigation.classList.remove("is-open");
        menuButton.classList.remove("is-open");
        menuButton.setAttribute("aria-expanded", "false");
        menuButton.setAttribute("aria-label", "Menu openen");
        resetBeeldsubmenu();
        if (returnFocus) menuButton.focus({ preventScroll: true });
    }

    if (dropdown && dropdownButton) {
        dropdownButton.addEventListener("click", function () {
            clearTimeout(dropdownCloseTimer);
            if (dropdownPinned) {
                resetBeeldsubmenu();
            } else {
                dropdownPinned = true;
                setBeeldsubmenu(true);
            }
        });

        // E?n open/dicht-status voor muis, aanraking en toetsenbord.
        dropdown.addEventListener("pointerenter", function (event) {
            if (!desktopNavigation.matches || event.pointerType !== "mouse") return;
            clearTimeout(dropdownCloseTimer);
            dropdownHovered = true;
            setBeeldsubmenu(true);
        });
        dropdown.addEventListener("pointerleave", function (event) {
            if (!desktopNavigation.matches || event.pointerType !== "mouse") return;
            dropdownHovered = false;
            dropdownCloseTimer = setTimeout(function () {
                if (!dropdownPinned && !dropdown.contains(document.activeElement)) {
                    resetBeeldsubmenu();
                }
            }, 180);
        });
        dropdown.addEventListener("focusout", function () {
            requestAnimationFrame(function () {
                if (!dropdown.contains(document.activeElement)) {
                    dropdownPinned = false;
                    if (!dropdownHovered) resetBeeldsubmenu();
                }
            });
        });
        dropdownButton.addEventListener("keydown", function (event) {
            if (event.key !== "ArrowDown" && event.key !== "ArrowUp") return;
            event.preventDefault();
            clearTimeout(dropdownCloseTimer);
            dropdownPinned = true;
            setBeeldsubmenu(true);
            const links = dropdown.querySelectorAll(".navigatie-dropdown-menu a");
            const link = event.key === "ArrowUp" ? links[links.length - 1] : links[0];
            requestAnimationFrame(function () {
                if (link && dropdown.classList.contains("is-open")) link.focus();
            });
        });
    }

    document.addEventListener("click", function (event) {
        if (dropdown && !dropdown.contains(event.target)) resetBeeldsubmenu();
        if (header && navigation && navigation.classList.contains("is-open") &&
            !header.contains(event.target)) {
            closeMobileNavigation();
        }
    });

    document.addEventListener("keydown", function (event) {
        if (event.key !== "Escape") return;
        if (dropdown && dropdown.classList.contains("is-open")) {
            event.preventDefault();
            const focusInDropdown = dropdown.contains(document.activeElement);
            resetBeeldsubmenu();
            if (focusInDropdown) dropdownButton.focus({ preventScroll: true });
        } else if (navigation && navigation.classList.contains("is-open")) {
            event.preventDefault();
            closeMobileNavigation(true);
        }
    });

    desktopNavigation.addEventListener("change", function () {
        closeMobileNavigation();
    });


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
        document.createElement("dialog");

    lightbox.className =
        "packshot-lightbox";
    lightbox.setAttribute("aria-label", "Productfoto vergroten");

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

    let lastImage;
    let previousOverflow;

    function openLightbox(image) {

        lastImage = image;
        previousOverflow = document.body.style.overflow;
        lightboxImage.src = image.dataset.lightboxSrc || image.currentSrc || image.src;
        lightboxImage.alt = image.alt || "";

        lightbox.classList.add("is-open");
        lightbox.showModal();
        closeButton.focus({ preventScroll: true });

        document.body.style.overflow =
            "hidden";

    }


    function closeLightbox() {

        lightbox.close();
        lightbox.classList.remove(
            "is-open"
        );

        document.body.style.overflow =
            previousOverflow;
        lastImage?.focus({ preventScroll: true });

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

            image.tabIndex = 0;
            image.setAttribute("role", "button");
            image.setAttribute("aria-haspopup", "dialog");
            image.setAttribute("aria-label", "Vergroot: " + (image.alt || "productfoto"));
            image.addEventListener("keydown", function (event) {
                if (event.key === "Enter" || event.key === " ") {
                    event.preventDefault();
                    openLightbox(image);
                }
            });
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
    lightbox.addEventListener("cancel", function (event) {
        event.preventDefault();
        closeLightbox();
    });


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
