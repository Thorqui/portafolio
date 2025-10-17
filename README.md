### Aitor Quilez Portafolio

Portafolio web interactivo de Aitor Quilez Herrero, desarrollador web especializado en JavaScript y Three.js. Una experiencia visual inmersiva con efectos 3D, partículas animadas y navegación intuitiva.

## ✨ Características Principales

Fondo 3D Interactivo: Sistema de partículas con Three.js que responde al movimiento del mouse
Efectos de Partículas: Animaciones dinámicas en los iconos interactivos
Diseño Responsive: Adaptación completa a dispositivos móviles y desktop
Accesibilidad: Soporte ARIA, navegación por teclado y enfoque visual
Tooltips Interactivos: Previsualización de proyectos con imágenes y enlaces
Animaciones Suaves: Transiciones CSS y efectos de Three.js optimizados
Carga Optimizada: Preloading de fuentes y manejo de errores de imágenes

## 🛠️ Tecnologías Utilizadas

Frontend: HTML5, CSS3, Vanilla JavaScript
3D: Three.js (versión 0.157.0)
UI: Bootstrap Icons, Google Fonts (Space Mono)
Herramientas: Popper.js para tooltips
Optimización: Lazy loading, throttling de renderizado

```text
📁 Estructura del Proyecto
text├── index.html          # Archivo principal
├── Resources/
│   ├── favicon.png     # Icono del sitio
│   ├── Aitor.jpg       # Foto personal
│   ├── Arete.png       # Imágenes de proyectos
│   ├── Street_Figther.png
│   ├── Breaking_Bad_Table.png
│   ├── eSports.png
│   ├── Puzzle.png
│   ├── Lista_Compra.png
│   ├── Docker.png
│   ├── Python.png
│   └── CV_QHA.pdf      # Currículum vitae
```


## 🎮 Interactividad
Navegación

- Iconos Principales: Clic o hover para expandir secciones (Proyectos, Info, Contacto)
- Proyectos: Clic en cualquier proyecto muestra tooltip con demo y código fuente
- Teclado: Navegación completa con Enter/Espacio y Escape para cerrar

Efectos Visuales

- Partículas de Fondo: 4000 partículas rotando y siguiendo el mouse
- Efectos en Iconos: Sistema de partículas activado al hover/focus
- Tooltips Dinámicos: Posicionamiento inteligente con Popper.js
- Loading Spinner: Indicador de carga inicial

## 📱 Responsive Design

Mobile First: Optimizado para pantallas ≤768px  
Breakpoints:

480px: Ajustes para pantallas muy pequeñas  
768px: Layout móvil completo  
1440px+: Contenidos más amplios  


Performance: Renderizado throttled a 30fps en móviles

## ♿ Accesibilidad

ARIA Labels: Atributos semánticos en todos los elementos interactivos  
Navegación por Teclado: Focus management y activación con Enter/Espacio  
Reduced Motion: Respeto a preferencias del sistema operativo  
Contraste: Colores optimizados para legibilidad  
Screen Reader: Estructura semántica y descripciones  

## 🔧 Personalización
Variables CSS  
css:root {
    --dark-grey: #1a1a1a;    /* Fondo principal */  
    --light-grey: #f0f0f0;   /* Texto principal */  
    --mid-grey: #888;        /* Texto secundario */  
    --dark-grey-border: #444; /* Bordes */  
}  

Configuración Three.js

particleCount: Número de partículas de fondo (4000 por defecto)  
frameInterval: FPS objetivo (30fps)  
sizeAttenuation: Escala de partículas según distancia  

## 📋 Proyectos Mostrados
Studies Projects

. Arete Dance: Web moderna para academia de baile  
. Street Fighter: Recreación de pantalla de selección  
. Breaking Bad API: Consumo de API oficial  
. Tournament eSports UML: Sistema de gestión de torneos  

Own Projects

. Brain Puzzle: Rompecabezas matemático
. Shopping_list: App lista de la compra
. DockerApp: Sitio estático con Docker
. DockerApp 2.0: Con backend Flask
. Script_Files: Organizador de descargas

## 🐛 Solución de Problemas
Canvas no se renderiza

Verificar WebGL support en el navegador  
Comprobar conexión a CDN de Three.js  
Revisar console para errores de import  

Imágenes no cargan

Verificar ruta ./Resources/  
Comprobar onerror fallback de imágenes  
Usar servidor local para evitar CORS  

Performance baja

Reducir particleCount en dispositivos móviles
Desactivar antialias en móviles
Usar prefers-reduced-motion

## 📄 Licencia
Proyecto personal - © 2025 Aitor Quilez Herrero (Thorqui)  

##🤝 Contacto
Email: aitorquilez@gmail.com  
GitHub: Thorqui  
LinkedIn: Aitor Quilez  
