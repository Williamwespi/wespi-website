/* Volledige voor-/na-weergave naast de gedeelde, toetsenbordbedienbare slider. */
document.querySelectorAll('.pb-vergelijking').forEach(article => {
    const range = article.querySelector('.beeldvergelijker__slider');
    const buttons = article.querySelectorAll('[data-pb-stand]');
    if (!range) return;
    const update = () => buttons.forEach(button => button.setAttribute('aria-pressed', String(range.value === button.dataset.pbStand)));
    buttons.forEach(button => button.addEventListener('click', () => {
        range.value = button.dataset.pbStand;
        range.dispatchEvent(new Event('input', {bubbles: true}));
    }));
    range.addEventListener('input', update);
    update();
});
