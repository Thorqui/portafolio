# Estado del proyecto — Portafolio Aitor Quilez

> Actualizado: 2026-09-08. Documento para retomar en sesiones nuevas sin
> re-explorar el repo.

## Qué es

Portafolio web personal (sitio estático: `index.html` + `Resources/`) con
fondo 3D de partículas Three.js, tooltips de proyectos, responsive y
accesible. Dockerizado con nginx para despliegue.

## Estado git: EN CURSO

- Rama `portfolio-improvements`. Remote `Thorqui/portafolio`.
- Rediseño visual (sep 2026): proyectos como rejilla de tarjetas con
  miniatura y stack, entrada cinemática de cámara, estelas de warp al
  navegar, rótulos `01 / ...`, nebulosa de fondo, meta Open Graph e
  imágenes en WebP (5,5 MB → 308 KB).
- Selector ES/EN con persistencia en `localStorage` y detección por
  `navigator.language`. Va en un `<script>` normal, no en el módulo, para
  que siga funcionando aunque falle el CDN de Three.js.
- Móvil: objetivos táctiles de 44px, `dvh` en los paneles, botón de cierre
  en el detalle, media query de apaisado y `@media (hover: none)` para lo
  que antes solo se revelaba al pasar el ratón.
- Corregido: los iconos de navegación eran enfocables pero no activables
  con teclado (no había handler de Enter/Espacio) y `aria-expanded` nunca
  se actualizaba.
- Eliminado el botón "Volver a la órbita": pulsar fuera y Escape ya hacían
  lo mismo.
- Tarjetas con `href` real (demo, o repo si no hay demo) y año por proyecto,
  tomado de `created_at` de la API de GitHub. JSON-LD `Person` y sección de
  stack en el panel de info, ambos con datos del CV de jul-2026.

## Cómo arrancar

```bash
npx serve .    # o abrir index.html; en prod: docker build + run
```

## Detalles del rediseño

- Sin secciones: una sola rejilla, los profesionales primero. Añadidos
  Blothor (blothor.com) y Control de Clases (dev.blothor.com), ambos 2026 y
  sin repo público. Capturas generadas con Chrome headless a 1440x900 y
  convertidas a WebP.
- Los proyectos se editan en un solo sitio: los `<a class="project-card">`
  de `index.html`. Cada tarjeta es autocontenida y lleva `data-desc-es` y
  `data-desc-en`; los textos de interfaz están en el diccionario `DICT`
  del script de i18n.
- Las etiquetas de stack (`.tech-tag`) son una estimación inicial, sin
  verificar contra cada repo.
- Corregidos dos bugs de layout preexistentes: `.content-display` sin
  `box-sizing: border-box` (el padding se sumaba al `max-height`) y
  `#proyectos-dropdown` con `transform`, que lo convertía en bloque
  contenedor de su hijo `position: fixed` y descentraba el panel.
- `update_portfolio.py` y `update_particles.py` son scripts de un solo uso
  ya aplicados: sus cadenas objetivo ya no existen. No re-ejecutar.
- La URL de las meta Open Graph asume `thorqui.github.io/portafolio/`.

## Pendiente / siguiente

- **El portafolio va muy por detrás del CV.** El CV (jul-2026) describe un
  desarrollador full-stack con sistemas en producción (Zebra Ventures:
  React/Django/C#/PostgreSQL, microservicios con API de Claude) y Blothor.
  La bio del sitio sigue diciendo "en transición desde la industria química"
  y "competencias recién adquiridas", y los 9 proyectos son todos de 2025.
  Pendiente de decisión del usuario: bio nueva y qué proyectos entran.
- Repos públicos más recientes y no publicados en el portafolio:
  `class-control` (TS, 2026-04), `furnabit` (2026-06), `navy` (2026-05),
  `Retrofit-API_REST` (Kotlin, 2026-01), `QHA_ci-cd-api-001` (Java, 2026-01),
  `QHA_PMDM_2T` (Kotlin, 2026-02). Lo mejor del CV (CRM, CMS, AN, LYZER,
  `arete-dance-studio`) no está público en github.com/Thorqui.
- El JSON-LD declara `jobTitle: Desarrollador Full-Stack` (fuente: CV), lo
  que hoy contradice la bio visible. Se resuelve al actualizar la bio.
- **CV desactualizado**: `Resources/CV_QHA.pdf` es del 5-jun-2026; las
  fuentes `.docx` son del 10-jul-2026. No hay LibreOffice, pandoc ni
  soffice instalados: la conversión a PDF la tiene que hacer el usuario.
  Decidir además si se publican dos PDF (uno por idioma) o solo uno.
