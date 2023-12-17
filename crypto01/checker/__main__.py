#!/bin/python3

import os
import requests
from pwn import *
import logging
logging.disable()

def encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    assert key < len(alphabet) and key > 0
    ciphertext = ""
    for c in plaintext:
        ciphertext += alphabet[(alphabet.index(c) + key) % 26] 

    return ciphertext

# Per le challenge web
URL = os.environ.get("URL", "http://caesar.challs.cyberhighschools.it")
if URL.endswith("/"):
   URL = URL[:-1]

# solver
r = requests.get(URL) 
t = r.text
ciphertext = (t[t.index("<h2>FLAG CIFRATA</h2>")+56:t.index("<h2>FLAG CIFRATA</h2>")+83])
print("flag{"+encrypt(ciphertext, 12)+"}")
