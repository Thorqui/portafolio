# ================================================================
# portafolio — HTML + CSS + JS estático
# Sin build step, serve directo con nginx alpine
# ================================================================

FROM nginx:alpine-slim

COPY index.html /usr/share/nginx/html/index.html
COPY assets/ /usr/share/nginx/html/assets/
COPY Resources/*.webp Resources/favicon.png Resources/og-image.png Resources/Aitor_Quilez_CV_ES.pdf Resources/Aitor_Quilez_CV_EN.pdf /usr/share/nginx/html/Resources/
COPY nginx.docker.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
