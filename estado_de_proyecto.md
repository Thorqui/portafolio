# Estado del proyecto — 2026-09-15

## Ramas

- `main`: conservada en f08ccff.
- `portfolio-improvements`: versión avanzada guardada en 2f587a8, incluyendo todos los cambios y recursos que estaban pendientes al iniciar la nueva propuesta.
- `codex/portfolio-showcase`: propuesta con contenido visible mediante scroll y fondo espacial opcional.

## Propuesta implementada

Portada full-stack, navegación por anclas, proyectos con enlaces directos y detalles en diálogo nativo, bio ES/EN actualizada y CV por idioma. HTML, estilos, traducciones, interacción y fondo separados. Menos partículas y pausa con movimiento reducido o pestaña oculta. Docker con copia explícita de recursos y caché revalidable para CSS/JS.

## Pendiente editorial

Confirmar las tecnologías de cada proyecto, ampliar los destacados con casos de estudio, validar el contenido de los CV ES/EN y confirmar dominio definitivo. No se inventaron métricas, clientes ni responsabilidades específicas.

## Vista previa

`python3 -m http.server 4173 --bind 127.0.0.1`

Los scripts Python antiguos son transformaciones de un solo uso: no ejecutarlos.

## 2026-09-16 — Proyectos separados y vídeos beta

- `#proyectos` dividido en dos bloques: **Ecosistema Blothor** (Blothor, Control
  de Clases y las tarjetas beta con vídeo: Travel, Blothy, CRM, Safe, Tasks,
  Blog, Research Intelligence, Private-chat) y **Proyectos personales y de
  formación** (resto). Etiqueta común «Fase Beta · Próximamente» (i18n).
- Vídeos en `assets/media/<slug>.mp4` (H.264 1600 px, 24 fps, sin audio,
  faststart) con portada `<slug>.webp`. Originales en `~/Blothor/videos_nuevos/`.
- Sin commitear (incluye los cambios previos de Research/Private-chat).
