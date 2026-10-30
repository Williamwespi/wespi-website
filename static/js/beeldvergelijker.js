document.querySelectorAll("[data-beeldvergelijker]").forEach(function (vergelijker) {
    const slider = vergelijker.querySelector(".beeldvergelijker__slider");
    if (!slider || vergelijker.dataset.geinitialiseerd) return;
    vergelijker.dataset.geinitialiseerd = "true";

    function bijwerken() {
        const percentage = Number(slider.value);
        vergelijker.style.setProperty("--vergelijking-positie", percentage + "%");
        slider.setAttribute("aria-valuetext", percentage + "% origineel, " + (100 - percentage) + "% bewerkt");
    }

    function verplaatsen(event) {
        const kader = slider.getBoundingClientRect();
        if (!kader.width) return;
        slider.value = Math.round(Math.max(0, Math.min(100, (event.clientX - kader.left) / kader.width * 100)));
        bijwerken();
    }

    slider.addEventListener("input", bijwerken);
    slider.addEventListener("pointerdown", function (event) {
        if (!event.isPrimary || event.button !== 0) return;
        event.preventDefault();
        slider.focus({ preventScroll: true });
        slider.setPointerCapture(event.pointerId);
        verplaatsen(event);
    });
    slider.addEventListener("pointermove", function (event) {
        if (slider.hasPointerCapture(event.pointerId)) verplaatsen(event);
    });
    function loslaten(event) {
        if (slider.hasPointerCapture(event.pointerId)) slider.releasePointerCapture(event.pointerId);
    }
    slider.addEventListener("pointerup", loslaten);
    slider.addEventListener("pointercancel", loslaten);
    bijwerken();
});
