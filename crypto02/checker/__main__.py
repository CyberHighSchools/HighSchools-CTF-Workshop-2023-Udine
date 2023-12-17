#!/bin/python3

import os
import requests
from pwn import *
import logging
import math
logging.disable()

def simple_factor(value):
   factors = []
   for i in range(2, 1024):
      if value % i == 0:
         factors.append(i)

   return factors


# Per le challenge web
URL = os.environ.get("URL", "http://factorization.challs.cyberhighschools.it")
if URL.endswith("/"):
   URL = URL[:-1]

s = requests.session() 
t = s.get(URL)
html = t.text
tmp = html[html.index("<h2>Segreto cifrato</h2>")+59:]
value = int(tmp[0:tmp.index("</code>")])
secret = max(simple_factor(value))-17

print(s.get(URL+f"/get_flag/{secret}").text)