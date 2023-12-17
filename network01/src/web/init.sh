#!/bin/sh

set -e -x

mkdir -p /etc/certs
openssl req -subj '/CN=SnakeCTF2023/O=MadrHacks/C=IT' -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout /etc/certs/nginx-selfsigned.key -out /etc/certs/nginx-selfsigned.crt

nginx -g "daemon off;"