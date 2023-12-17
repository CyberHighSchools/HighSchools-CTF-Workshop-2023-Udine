FROM alpine:latest

RUN apk --no-cache add sharutils s-nail tcpdump

COPY ./flag.png /
COPY ./chall.sh /

CMD [ "/chall.sh"]