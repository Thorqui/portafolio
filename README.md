# Portafolio de Aitor Quilez

Bienvenido al repositorio de mi portafolio personal, una página web interactiva diseñada para mostrar mis proyectos como desarrollador web especializado en JavaScript y Three.js. Este proyecto utiliza un diseño minimalista con animaciones de partículas y menús desplegables responsivos para ofrecer una experiencia visual moderna y fluida.

## Descripción

Este portafolio presenta mis proyectos de desarrollo web, información personal y datos de contacto de manera interactiva. Utiliza Three.js para crear un fondo dinámico de partículas y menús desplegables con posiciones relativas que se adaptan a diferentes tamaños de pantalla. El diseño es responsivo, accesible y optimizado para un rendimiento eficiente.

## Características

- **Fondo interactivo**: Animación de partículas en 3D usando Three.js, con 2000 partículas en el fondo y 15 partículas por ícono.
- **Menús desplegables**:
  - **Proyectos**: Centrado en la página (`top: 70%; left: 50%` en escritorio, `top: 50%; left: 50%` en móviles), con dos columnas para proyectos de estudios y propios.
  - **Info**: Posicionado en `top: 40%; left: 10%` (escritorio) o `top: 5%; left: 5%` (móviles).
  - **Contacto**: Posicionado en `top: 30%; right: 10%` (escritorio) o `top: 5%; right: 5%` (móviles), con enlace a correo y descarga de currículum en PDF.
- **Tooltip interactivo**: Al hacer clic en un proyecto, se muestra una vista previa con un GIF, descripción y enlaces a demo y código fuente.
- **Responsividad**: Diseño adaptado para móviles (<768px), tablets y pantallas grandes (>1440px) usando unidades relativas (`vw`, `%`) y `clamp` para fuentes.
- **Optimización de rendimiento**:
  - Reducción de partículas (2000 en fondo, 15 por ícono).
  - Límite de 30 FPS en animaciones.
  - Carga diferida de imágenes (`loading="lazy"`) y scripts (`defer`).
  - Desactivación de antialiasing y ajuste de `pixelRatio` en móviles.
- **Accesibilidad**: Soporte para navegación por teclado, atributos ARIA y compatibilidad con `prefers-reduced-motion`.
- **SEO**: Metadatos optimizados y favicon personalizado en escala de grises.

## Tecnologías utilizadas

- **HTML5** y **CSS3** para la estructura y estilos.
- **JavaScript** y **Three.js** (v0.157.0) para animaciones 3D.
- **Bootstrap Icons** (v1.13.1) para íconos.
- **Popper.js** (v2.11.8) para posicionamiento de tooltips.
- **Google Fonts** (Space Mono) para tipografía.
- **Markdown** para este README.

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio


Asegurar dependencias:

No se requieren dependencias locales, ya que los recursos (Three.js, Popper.js, Bootstrap Icons) se cargan desde CDN.
Asegúrate de tener una conexión a internet para cargar:

https://unpkg.com/three@0.157.0/build/three.module.js
https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js
https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css




Añadir recursos locales:

Coloca un favicon en escala de grises en el directorio raíz (favicon.png).
Sube tu currículum en PDF al directorio ./assets/curriculum.pdf.


Servir la página:

Usa un servidor local para pruebas (por ejemplo, con Python):
bashpython -m http.server 8000

O abre index.html directamente en un navegador (nota: algunas funciones, como la carga del PDF, requieren un servidor).


Desplegar (opcional):

Sube el proyecto a un servidor o plataforma como GitHub Pages, Netlify o Vercel.
Asegúrate de que el directorio ./assets/ esté incluido.



Uso

Abre la página en un navegador moderno (Chrome, Firefox, Edge, Safari).
Interacciones:

Fondo: Mueve el ratón para interactuar con las partículas.
Menús: Pasa el cursor o haz clic en los íconos (bi-code-slash, bi-person, bi-envelope) para abrir los menús desplegables.
Proyectos: Haz clic en un proyecto para ver un tooltip con vista previa, descripción y enlaces a demo/código.
Contacto: Usa los enlaces para enviar un correo o descargar el currículum.


Navegación por teclado:

Usa Tab para navegar entre íconos y enlaces.
Presiona Enter o Espacio para abrir/cerrar menús y tooltips.
Usa Esc para cerrar tooltips.



Estructura del proyecto
texttu-repositorio/
├── index.html           # Página principal
├── favicon.png          # Favicon en escala de grises
├── assets/
│   └── curriculum.pdf   # Currículum en PDF
└── README.md            # Documentación
Optimización y rendimiento

Carga inicial:

Spinner de carga visible mientras se inicializa Three.js.
Carga diferida de imágenes (loading="lazy") y scripts (defer).


Rendimiento:

Partículas reducidas (2000 en fondo, 15 por ícono).
Animación limitada a 30 FPS.
Antialiasing desactivado y pixelRatio limitado en móviles.


Pruebas:

Probado en Chrome, Firefox y Safari (escritorio y móvil).
Verifica la consola del navegador (F12) para errores en caso de problemas.



Problemas conocidos

Carga lenta en conexiones lentas: Los recursos de CDN (Three.js, Popper.js) pueden tardar en cargar. Considera alojar Three.js localmente si es necesario.
Rendimiento en dispositivos antiguos: En móviles de baja potencia, las animaciones pueden ser menos fluidas. Puedes reducir aún más las partículas (por ejemplo, a 1000) en index.html.

Contribuir
Si deseas contribuir:

Haz un fork del repositorio.
Crea una rama (git checkout -b mejora-nueva).
Realiza tus cambios y haz commit (git commit -m "Añadir mejora").
Sube los cambios (git push origin mejora-nueva).
Abre un Pull Request.

Créditos

Aitor Quilez: Desarrollador y creador del portafolio.
Three.js: Biblioteca para animaciones 3D.
Bootstrap Icons: Iconos utilizados en los menús.
Popper.js: Posicionamiento de tooltips.
Google Fonts: Tipografía Space Mono.
Grok (xAI): Asistencia en la optimización del código y redacción del README.

Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

© 2025 Aitor Quilez | Zaragoza, España








### README.md en Inglés

```markdown
# Aitor Quilez Portfolio

Welcome to the repository of my personal portfolio, an interactive webpage designed to showcase my projects as a web developer specializing in JavaScript and Three.js. This project features a minimalist design with particle animations and responsive dropdown menus for a modern and smooth visual experience.

## Description

This portfolio displays my web development projects, personal information, and contact details interactively. It uses Three.js to create a dynamic particle background and dropdown menus with relative positioning that adapt to different screen sizes. The design is responsive, accessible, and optimized for efficient performance.

## Features

- **Interactive Background**: 3D particle animation using Three.js, with 2000 background particles and 15 particles per icon.
- **Dropdown Menus**:
  - **Projects**: Centered on the page (`top: 70%; left: 50%` on desktop, `top: 50%; left: 50%` on mobile), with two columns for academic and personal projects.
  - **Info**: Positioned at `top: 40%; left: 10%` (desktop) or `top: 5%; left: 5%` (mobile).
  - **Contact**: Positioned at `top: 30%; right: 10%` (desktop) or `top: 5%; right: 5%` (mobile), with links to email and a downloadable PDF resume.
- **Interactive Tooltip**: Clicking a project displays a preview with a GIF, description, and links to demo and source code.
- **Responsiveness**: Adapted for mobile (<768px), tablets, and large screens (>1440px) using relative units (`vw`, `%`) and `clamp` for fonts.
- **Performance Optimization**:
  - Reduced particles (2000 for background, 15 per icon).
  - Animation capped at 30 FPS.
  - Lazy loading of images (`loading="lazy"`) and scripts (`defer`).
  - Antialiasing disabled and `pixelRatio` limited on mobile.
- **Accessibility**: Keyboard navigation support, ARIA attributes, and compatibility with `prefers-reduced-motion`.
- **SEO**: Optimized metadata and grayscale favicon.

## Technologies Used

- **HTML5** and **CSS3** for structure and styling.
- **JavaScript** and **Three.js** (v0.157.0) for 3D animations.
- **Bootstrap Icons** (v1.13.1) for icons.
- **Popper.js** (v2.11.8) for tooltip positioning.
- **Google Fonts** (Space Mono) for typography.
- **Markdown** for this README.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository