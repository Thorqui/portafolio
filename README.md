# Portafolio de Aitor Quilez

Sitio estático con presentación full-stack, proyectos, perfil y contacto en español e inglés. El contenido y los enlaces funcionan sin WebGL; Three.js aporta un fondo opcional.

## Desarrollo

```sh
python3 -m http.server 4173 --bind 127.0.0.1
```

Abrir http://127.0.0.1:4173. No requiere instalación ni compilación.

## Estructura

- `index.html`: contenido, proyectos y metadatos.
- `assets/styles.css`: estilos y adaptación móvil.
- `assets/i18n.js`: traducciones y selección del CV ES/EN.
- `assets/app.js`: detalles de proyectos en un diálogo nativo con Escape y retorno del foco.
- `assets/background.js`: fondo opcional, limitado a unos 30 fps y detenido con movimiento reducido o pestaña oculta.
- `Resources/`: imágenes y PDF.

Las tarjetas mantienen enlaces directos. El botón adicional de detalles se añade con JavaScript. Para editar un proyecto, modificar su tarjeta y los atributos `data-*` en el HTML.

## Docker

```sh
docker build -t portafolio .
docker run --rm -p 8080:80 portafolio
```

La imagen copia únicamente el HTML, assets y recursos publicados. Los scripts auxiliares y CV anteriores quedan fuera. CSS y JS se revalidan porque sus nombres no llevan hash.

## Validación y contenido pendiente

Se revisaron la portada en escritorio y móvil, cambio ES/EN, selección de CV y diálogo con Escape y retorno del foco. JavaScript validado con `node --check`.

Las descripciones y tecnologías de proyectos proceden de la versión anterior: falta contrastarlas con cada producto y redactar casos de estudio con responsabilidades y resultados confirmados. Revisar el contenido de los PDF antes de publicar. La URL canónica sigue siendo la de GitHub Pages.

Los scripts `update_portfolio.py` y `update_particles.py` son históricos y no deben ejecutarse sobre esta versión.
