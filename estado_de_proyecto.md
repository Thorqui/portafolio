# Estado del proyecto — Portafolio Aitor Quilez

> Actualizado: 2026-07-11. Documento para retomar en sesiones nuevas sin
> re-explorar el repo.

## Qué es

Portafolio web personal (sitio estático: `index.html` + `Resources/`) con
fondo 3D de partículas Three.js, tooltips de proyectos, responsive y
accesible. Dockerizado con nginx para despliegue.

## Estado git: ESTABLE / TERMINADO

- Rama `main`, working tree limpio. Remote `Thorqui/portafolio`.
- Últimos commits: dockerización (Dockerfile + nginx), actualización de CV
  (nuevo rol, skills y proyectos), refactor de modales/tooltips.
- Sin actividad desde junio 2026: mantenimiento puntual, no desarrollo.

## Cómo arrancar

```bash
npx serve .    # o abrir index.html; en prod: docker build + run
```

## Pendiente / siguiente

- Solo actualizaciones de contenido (CV/proyectos nuevos). Los CV fuente
  están en la raíz de Blothor (`Aitor_Quilez_CV_ES/EN.docx`, jul 2026):
  comprobar si el portafolio refleja la última versión.
