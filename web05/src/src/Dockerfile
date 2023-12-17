FROM wyveo/nginx-php-fpm:php82

ARG FLAG

RUN rm -rf /usr/share/nginx/html/*
COPY . /usr/share/nginx/html/
RUN echo -n "${FLAG}" >> /flag.txt
