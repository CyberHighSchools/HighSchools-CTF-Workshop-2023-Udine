#!/bin/python3

import os
import requests
from pwn import *
import logging

logging.disable()

URL = os.environ.get("URL", "http://spider.challs.cyberhighschools.it")
if URL.endswith("/"):
    URL = URL[:-1]

res1 = requests.get(f"{URL}/supe3s3cretf0lder/flag1.txt")
res2 = requests.get(f"{URL}/standardNonSecretFolder/flag2.txt")
if not res1.ok or not res2.ok:
    print(f"Cannot contact {URL}")
    exit(1)

flag1 = res1.text.split("\n")[0]
flag2 = res2.text.split("\n")[0]
# Check challenge
flag = flag1 + flag2
print(flag)
