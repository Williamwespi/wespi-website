(() => {
    const page = document.querySelector('.ai-modelfotografie');
    const dialog = page?.querySelector('.ai-lightbox');
    if (!dialog || typeof dialog.showModal !== 'function') return;

    const container = dialog.querySelector('.ai-lightbox-media');
    const title = dialog.querySelector('#ai-lightbox-titel');
    let opener;
    let previousOverflow;

    page.querySelectorAll('[data-ai-type]').forEach(link => {
        link.addEventListener('click', event => {
            if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
            event.preventDefault();
            opener = link;
            title.textContent = link.dataset.aiLabel;
            const media = document.createElement(link.dataset.aiType === 'video' ? 'video' : 'img');
            if (media.tagName === 'VIDEO') {
                media.controls = true;
                media.playsInline = true;
                media.preload = 'metadata';
                media.poster = link.querySelector('video').poster;
                media.setAttribute('aria-label', link.dataset.aiLabel);
            } else {
                media.alt = link.querySelector('img').alt;
            }
            media.src = link.href;
            container.replaceChildren(media);
            previousOverflow = document.body.style.overflow;
            document.body.style.overflow = 'hidden';
            dialog.showModal();
        });
    });

    const stopVideo = () => {
        const video = container.querySelector('video');
        if (video) {
            video.pause();
            video.removeAttribute('src');
            video.load();
        }
    };
    dialog.querySelector('.ai-lightbox-sluiten').addEventListener('click', () => {
        stopVideo();
        dialog.close();
    });
    // Stop immediately on Escape; the native dialog handles closing and focus containment.
    dialog.addEventListener('cancel', stopVideo);
    dialog.addEventListener('close', () => {
        stopVideo();
        container.replaceChildren();
        document.body.style.overflow = previousOverflow;
        opener?.focus();
    });
})();
