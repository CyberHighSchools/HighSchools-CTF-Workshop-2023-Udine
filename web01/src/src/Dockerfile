FROM wyveo/nginx-php-fpm:php82

ARG FLAG_1
ARG FLAG_2

WORKDIR /usr/share/nginx/html
RUN rm -rf *
COPY . .
RUN echo "${FLAG_1}" >> supe3s3cretf0lder/flag1.txt
RUN echo "Ora hai la prima parte della flag, cerca la seconda!" >> supe3s3cretf0lder/flag1.txt
RUN echo "${FLAG_2}" >> standardNonSecretFolder/flag2.txt
