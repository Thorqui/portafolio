# ================================================================
# portafolio — HTML + CSS + JS estático
# Sin build step, serve directo con nginx alpine
# ================================================================

FROM nginx:alpine-slim

COPY . /usr/share/nginx/html
COPY nginx.docker.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
