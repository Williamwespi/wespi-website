// Dezelfde beeldmasker- en pointertechniek als de automotive-vergelijker,
// met een vaste beginstand en expliciet herstel voor uitsluitend deze pagina.
(function () {
    const vergelijkers = [];
    document.querySelectorAll('.kledingbewerking [data-beeldvergelijker]').forEach(function (vergelijker) {
        const slider = vergelijker.querySelector('.beeldvergelijker__slider');
        if (!slider || vergelijker.dataset.geinitialiseerd) return;
        vergelijker.dataset.geinitialiseerd = 'true';
        slider.defaultValue = '100';

        function bijwerken() {
            const percentage = Math.max(0, Math.min(100, Number(slider.value)));
            vergelijker.style.setProperty('--vergelijking-positie', percentage + '%');
            slider.setAttribute('aria-valuetext', percentage + '% origineel, ' + (100 - percentage) + '% bewerkt');
            vergelijker.classList.toggle('is-volledig-voor', percentage >= 97);
            vergelijker.classList.toggle('is-volledig-na', percentage <= 3);
        }
        function herstellen() {
            slider.value = '100';
            bijwerken();
        }
        function verplaatsen(event) {
            const kader = slider.getBoundingClientRect();
            if (!kader.width) return;
            slider.value = Math.round(Math.max(0, Math.min(100, (event.clientX - kader.left) / kader.width * 100)));
            bijwerken();
        }
        slider.addEventListener('input', bijwerken);
        slider.addEventListener('change', bijwerken);
        slider.addEventListener('pointerdown', function (event) {
            if (!event.isPrimary || event.button !== 0) return;
            event.preventDefault();
            slider.focus({ preventScroll: true });
            slider.setPointerCapture(event.pointerId);
            verplaatsen(event);
        });
        slider.addEventListener('pointermove', function (event) {
            if (slider.hasPointerCapture(event.pointerId)) verplaatsen(event);
        });
        function loslaten(event) {
            if (slider.hasPointerCapture(event.pointerId)) slider.releasePointerCapture(event.pointerId);
        }
        slider.addEventListener('pointerup', loslaten);
        slider.addEventListener('pointercancel', loslaten);
        vergelijkers.push({ slider: slider, herstellen: herstellen });
        herstellen();
    });
    // Ook terugkeren via de browsergeschiedenis begint volledig bij het origineel.
    window.addEventListener('pageshow', function () {
        vergelijkers.forEach(function (item) { item.herstellen(); });
    });
    document.addEventListener('reset', function (event) {
        // De browser reset range-controls na het reset-event; synchroniseer daarna.
        queueMicrotask(function () {
            if (event.defaultPrevented) return;
            vergelijkers.forEach(function (item) {
                if (item.slider.form === event.target) item.herstellen();
            });
        });
    }, true);
})();
