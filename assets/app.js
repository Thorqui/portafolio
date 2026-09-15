(() => {
    const dialog = document.getElementById('project-tooltip');
    const close = document.getElementById('tooltip-close');
    let origin;
    document.querySelectorAll('.project-card').forEach(card => {
        const item = document.createElement('div');
        item.className = 'project-item';
        card.before(item);
        item.append(card);
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'details-button';
        button.dataset.i18n = 'project.details';
        button.textContent = document.documentElement.lang === 'en' ? 'View details' : 'Ver detalles';
        button.setAttribute('aria-haspopup', 'dialog');
        button.addEventListener('click', () => {
            origin = button;
            document.querySelectorAll('.project-card.active').forEach(el => el.classList.remove('active'));
            card.classList.add('active');
            const img = document.getElementById('tooltip-img');
            img.style.display = '';
            img.src = card.dataset.img;
            img.alt = card.dataset.title;
            document.getElementById('tooltip-title').textContent = card.dataset.title;
            document.getElementById('tooltip-desc').textContent = document.documentElement.lang === 'en' ? card.dataset.descEn : card.dataset.descEs;
            for (const kind of ['demo', 'repo']) {
                const link = document.getElementById(`tooltip-${kind}`);
                link.href = card.dataset[kind] || '#';
                link.classList.toggle('hidden', !card.dataset[kind]);
            }
            dialog.showModal();
            close.focus();
        });
        item.append(button);
    });
    close.addEventListener('click', () => dialog.close());
    dialog.addEventListener('click', event => {
        const rect = dialog.getBoundingClientRect();
        if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
    });
    dialog.addEventListener('close', () => {
        document.querySelectorAll('.project-card.active').forEach(el => el.classList.remove('active'));
        origin?.focus();
    });
})();
