#!/bin/sh

echo "Starting tcpdump"
tcpdump -i eth0 -w /out/mail.pcap -G 10 "tcp port 25" &

echo "Waiting"
sleep 2

echo "Sending mail"
uuencode /flag.png flag.png | mail -s "Ecco una bellissima flag!" -r pippo@test.paier.xyz -S mta=smtp://mailserver:25 debug@test.paier.xyz

echo "Waiting"
sleep 5
echo "Exiting"