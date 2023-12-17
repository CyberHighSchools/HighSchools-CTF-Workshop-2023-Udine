FROM nginx:alpine

RUN apk add --no-cache openssl

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY init.sh /docker-entrypoint.d/init.sh
COPY html /usr/share/nginx/html
