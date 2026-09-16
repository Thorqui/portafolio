(function () {
            const DICT = {
                es: {
"hero.title": "Software que resuelve problemas reales.",
"hero.desc": "Aplicaciones web, automatización y productos digitales. Del diseño de la interfaz a la lógica que hace que todo funcione.",
"nav.projects": "Proyectos",
"nav.about": "Sobre mí",
"nav.contact": "Contacto",
"projects.title": "Trabajo seleccionado",
"projects.desc": "Productos propios y proyectos de aprendizaje. Explora las demos y el código.",
"about.title": "De la experiencia al desarrollo",
"contact.title": "Hablemos de tu próximo proyecto",
"hero.cta": "Explorar proyectos",
"hero.contact": "Contactar",
"project.visit": "Abrir proyecto",
"project.details": "Ver detalles",
                    'meta.title': 'Aitor Quilez | Portafolio',
                    'stack.data': 'Datos',
                    'stack.mobile': 'Móvil',
                    'stack.agents': 'Agentes autónomos',
                    'about.bio': 'Desarrollador full-stack. Construyo aplicaciones web, automatizaciones y herramientas para resolver necesidades reales. <strong>Trabajo con interfaces, APIs y datos, combinando desarrollo de software con más de 15 años de experiencia profesional en la industria química.</strong> Aquí puedes explorar mis productos y proyectos de aprendizaje.',
                    'contact.open': 'Abierto a oportunidades',
                    'contact.cv': 'CV (PDF)',
                    'proj.demo': 'Ver Demo',
                    'proj.code': 'Ver Código',
                    'a11y.openProjects': 'Abrir proyectos',
                    'a11y.openAbout': 'Abrir sobre mí',
                    'a11y.openContact': 'Abrir contacto',
                    'a11y.email': 'Enviar correo a Aitor Quilez',
                    'a11y.cv': 'Descargar currículum de Aitor Quilez',
                    'a11y.linkedin': 'Perfil de LinkedIn',
                    'a11y.github': 'Perfil de GitHub',
                    'a11y.photo': 'Foto de Aitor Quilez',
                    'a11y.close': 'Cerrar',
                    'a11y.card': 'Ver detalle del proyecto'
                },
                en: {
"hero.title": "Software that solves real problems.",
"hero.desc": "Web applications, automation and digital products. From interface design to the logic that makes everything work.",
"nav.projects": "Projects",
"nav.about": "About",
"nav.contact": "Contact",
"projects.title": "Selected work",
"projects.desc": "Own products and learning projects. Explore the demos and source code.",
"about.title": "From experience to development",
"contact.title": "Let’s talk about your next project",
"hero.cta": "Explore projects",
"hero.contact": "Get in touch",
"project.visit": "Open project",
"project.details": "View details",
                    'meta.title': 'Aitor Quilez | Portfolio',
                    'stack.data': 'Data',
                    'stack.mobile': 'Mobile',
                    'stack.agents': 'Autonomous agents',
                    'about.bio': 'Full-stack developer. I build web applications, automations and tools for real-world needs. <strong>I work across interfaces, APIs and data, combining software development with over 15 years of professional experience in the chemical industry.</strong> Explore my products and learning projects below.',
                    'contact.open': 'Open to opportunities',
                    'contact.cv': 'CV (PDF)',
                    'proj.demo': 'View Demo',
                    'proj.code': 'View Code',
                    'a11y.openProjects': 'Open projects',
                    'a11y.openAbout': 'Open about me',
                    'a11y.openContact': 'Open contact',
                    'a11y.email': 'Email Aitor Quilez',
                    'a11y.cv': 'Download Aitor Quilez resume',
                    'a11y.linkedin': 'LinkedIn profile',
                    'a11y.github': 'GitHub profile',
                    'a11y.photo': 'Photo of Aitor Quilez',
                    'a11y.close': 'Close',
                    'a11y.card': 'View project details'
                }
            };
            const STORE = 'portafolio-lang';

            function detect() {
                try {
                    const saved = localStorage.getItem(STORE);
                    if (saved === 'es' || saved === 'en') return saved;
                } catch (e) { /* modo privado */ }
                return (navigator.language || 'es').toLowerCase().startsWith('en') ? 'en' : 'es';
            }

            function apply(lang) {
                const d = DICT[lang] || DICT.es;
                document.documentElement.lang = lang;
                document.title = d['meta.title'];
 document.getElementById('cv-download').href = `Resources/Aitor_Quilez_CV_${lang.toUpperCase()}.pdf`;

                document.querySelectorAll('[data-i18n]').forEach(el => {
                    const v = d[el.dataset.i18n];
                    if (v != null) el.textContent = v;
                });
                document.querySelectorAll('[data-i18n-html]').forEach(el => {
                    const v = d[el.dataset.i18nHtml];
                    if (v != null) el.innerHTML = v;
                });
                document.querySelectorAll('[data-i18n-aria]').forEach(el => {
                    const v = d[el.dataset.i18nAria];
                    if (v != null) el.setAttribute('aria-label', v);
                });
                document.querySelectorAll('[data-i18n-alt]').forEach(el => {
                    const v = d[el.dataset.i18nAlt];
                    if (v != null) el.alt = v;
                });

                // Las descripciones viven en la propia tarjeta, no en el
                // diccionario, para que anadir un proyecto sea un solo bloque.
                const tipDesc = document.getElementById('tooltip-desc');
                document.querySelectorAll('.project-card').forEach(card => {
                    const txt = lang === 'en' ? card.dataset.descEn : card.dataset.descEs;
                    const el = card.querySelector('.card-desc');
                    if (el && txt) el.textContent = txt;
                    card.setAttribute('aria-label', d['project.visit'] + ': ' + card.dataset.title);
                    if (card.classList.contains('active') && tipDesc && txt) tipDesc.textContent = txt;
                });

                document.querySelectorAll('.lang-btn').forEach(b => {
                    b.setAttribute('aria-pressed', String(b.dataset.lang === lang));
                });

                try { localStorage.setItem(STORE, lang); } catch (e) { /* modo privado */ }
            }

            document.addEventListener('click', e => {
                const btn = e.target.closest('.lang-btn');
                if (!btn) return;
                e.preventDefault();
                e.stopPropagation();
                apply(btn.dataset.lang);
            });

            window.portafolioLang = () => document.documentElement.lang === 'en' ? 'en' : 'es';
            // Selector temporalmente retirado: mostrar siempre español.
            apply('es');
        })();
