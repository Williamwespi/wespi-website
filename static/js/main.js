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