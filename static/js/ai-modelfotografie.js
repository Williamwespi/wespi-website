(() => {
    const page = document.querySelector('.ai-modelfotografie');
    const dialog = page?.querySelector('.ai-lightbox');
    if (!dialog || typeof dialog.showModal !== 'function') return;
    const models = JSON.parse(page.querySelector('#ai-modelgegevens').textContent);
    const grid = dialog.querySelector('.ai-lightbox-media');
    const detail = page.querySelector('.ai-detail');
    const detailMedia = detail.querySelector('.ai-detail-media');
    let opener, photoOpener, previousOverflow;
    page.querySelectorAll('[data-ai-model]').forEach(link => link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        opener = link;
        const model = models.find(m => m.id === link.dataset.aiModel);
        dialog.querySelector('h2').textContent = model.naam;
        grid.replaceChildren();
        [...model.originelen, ...model.fotos].forEach(item => {
            const link = document.createElement('a');
            link.href = '/static/' + item.src;
            const img = document.createElement('img');
            img.src = '/static/' + item.presentatie.src;
            img.alt = item.alt;
            img.width = item.presentatie.width;
            img.height = item.presentatie.height;
            const caption = document.createElement('span');
            caption.textContent = item.alt;
            const frame = document.createElement('span');
            frame.className = 'ai-galerij-fotovlak';
            frame.append(img);
            caption.className = 'ai-galerij-bijschrift';
            link.append(frame, caption);
            link.addEventListener('click', event => {
                if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
                event.preventDefault();
                photoOpener = link;
                const large = img.cloneNode();
                large.src = link.href;
                large.width = item.width;
                large.height = item.height;
                detailMedia.replaceChildren(large);
                detail.showModal();
            });
            grid.append(link);
        });
        previousOverflow = document.body.style.overflow;
        document.body.style.overflow = 'hidden';
        dialog.showModal();
        dialog.scrollTop = 0;
    }));
    page.querySelectorAll('[data-ai-video]').forEach(link => link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        const model = models.find(m => m.id === link.dataset.aiVideo);
        const video = document.createElement('video');
        video.controls = true;
        video.playsInline = true;
        video.muted = true;
        video.preload = 'none';
        video.poster = '/static/' + model.video.poster;
        video.src = '/static/' + model.video.src;
        video.setAttribute('aria-label', model.video.alt);
        link.replaceWith(video);
        video.className = 'ai-inline-video';
        video.focus();
        video.play().catch(() => {});
    }));
    dialog.querySelector('.ai-lightbox-sluiten').addEventListener('click', () => dialog.close());
    detail.querySelector('.ai-detail-sluiten').addEventListener('click', () => detail.close());
    detail.addEventListener('close', () => { detailMedia.replaceChildren(); photoOpener?.focus(); });
    dialog.addEventListener('close', () => {
        grid.replaceChildren();
        document.body.style.overflow = previousOverflow;
        opener?.focus();
    });
    [dialog, detail].forEach(modal => {
        modal.addEventListener('click', event => {
            if (event.target !== modal) return;
            const r = modal.getBoundingClientRect();
            if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) modal.close();
        });
        modal.addEventListener('keydown', event => {
            if (event.key !== 'Tab') return;
            const controls = [...modal.querySelectorAll('button, a[href]')];
            const first = controls[0], last = controls[controls.length - 1];
            if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
            else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
        });
    });
})();
