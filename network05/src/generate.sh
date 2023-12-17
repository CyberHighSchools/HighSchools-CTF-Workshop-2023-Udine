#!/bin/bash

sudo docker compose up -d --build
sleep 10
sudo chown -R 1000:1000 ./out
cp ./out/mail.pcap ../attachments/mail.pcap