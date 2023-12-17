#!/bin/python3

import os
import requests
from pwn import *
import logging
logging.disable()

def get_public_key(session: requests.session, cookie):
   if cookie is None:
      t = session.get(URL)
   else:
      sess = session.cookies["session"]
      session.cookies.clear()
      t = session.get(URL,cookies= {"session": sess, "Encrypted Secret": cookie})
   html = t.text
   tmp =  html[html.index("<code class=\"lang-python\">")+26:html.index("</code>")]
   return int(tmp)

# Per le challenge web
URL = os.environ.get("URL", "http://xororacle.challs.cyberhighschools.it")
if URL.endswith("/"):
   URL = URL[:-1]

s = requests.session()

PK_original = get_public_key(s, None)
encrypted_secret_key_original = s.cookies["Encrypted Secret"]

cookie = "0"*8
PK0 = get_public_key(s, cookie)

recovered_key_bits = []
for i in range(1,9):
   cookie = "0"*(8-i)+"1"+"0"*(i-1)
   PK = get_public_key(s, cookie)
   if PK > PK0:
      recovered_key_bits.append(0)
   else:
      recovered_key_bits.append(1)
   
key = int("".join([str(x) for x in recovered_key_bits[::-1]]), 2)
encrypted_secret_key_original = int(encrypted_secret_key_original, 2)
secret = key^encrypted_secret_key_original

print(s.get(URL+f"/get_flag/{secret}").text.strip())