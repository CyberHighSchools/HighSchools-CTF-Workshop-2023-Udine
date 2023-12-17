#!/bin/python3

import os
import requests
from pwn import *
import logging
logging.disable()

def get_shared_secret(x1, y1, x2, y2, x3, y3):
		denom = (x1-x2) * (x1-x3) * (x2-x3)
		A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom
		B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom
		C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom

		return C # only the secret

# Per le challenge web
URL = os.environ.get("URL", "http://parabolic.challs.cyberhighschools.it")
if URL.endswith("/"):
   URL = URL[:-1]

s = requests.session()

# LEVEL 1
t = s.get(URL) 
# getting values
html = t.text
# getting parameters
tmp = html[html.index("<code class=\"lang-python\">")+26:html.index("</code>")]
P1 = eval(tmp[tmp.index("Alice = ")+8:tmp.index("Bob")-5])
P2 = eval(tmp[tmp.index("Bob = ")+6:tmp.index("Frank")-5])
P3 = eval(tmp[tmp.index("Frank = ")+8:-3])

secret = get_shared_secret(P1[0], P1[1], P2[0], P2[1], P3[0], P3[1])
print(s.get(URL+f"/check_secret/{int(secret)}").text)