#!/bin/python3

import os
import requests
from pwn import *
import logging
logging.disable()

# LEVEL 0
def level_0(a, b, n, v_1):
    return (a*v_1 + b) % n

def level_1(a, n, v_1, v_2):
    b = (v_2 - a*v_1) % n
    return (a*v_2 + b) % n

def level_2(b, n, v_1, v_2):
    a = (v_2 - b)*(pow(v_1, -1, n))
    return (a*v_2 + b) % n

# Per le challenge web
URL = os.environ.get("URL", "http://lcg.challs.cyberhighschools.it")
if URL.endswith("/"):
   URL = URL[:-1]

s = requests.session()

# LEVEL 1
t = s.get(URL) 
# getting values
html = t.text
tmp = html[html.index("<h2>Valori</h2>")+50:]
values = (tmp[0:tmp.index("</code>")]).split()
values = [int(s) for s in values]
# getting parameters
tmp = html[html.index("<code class=\"lang-python\">")+26:html.index("</code>")]
a = int(tmp[tmp.index("a = ")+4:tmp.index("b =")-5])
b = int(tmp[tmp.index("b = ")+4:tmp.index("modulo =")-5])
modulo = int(tmp[tmp.index("modulo = ")+9:-4])
value = level_0(a, b, modulo, values[0])
s.get(URL+f"/check_level/0/{value}")


# LEVEL 2
t = s.get(URL) 
# getting values
html = t.text
tmp = html[html.index("<h2>Valori</h2>")+50:]
values = (tmp[0:tmp.index("</code>")]).split()
values = [int(s) for s in values]
# getting parameters
tmp = html[html.index("<code class=\"lang-python\">")+26:html.index("</code>")]
a = tmp[tmp.index("a = ")+4:tmp.index("b =")-5]
b = tmp[tmp.index("b = ")+4:tmp.index("modulo =")-5]
modulo = tmp[tmp.index("modulo = ")+9:-4]
a = int(a) if a != "unknown" else ""
b = int(b) if b != "unknown" else ""
modulo = int(modulo) if modulo != "unknown" else ""
value = level_1(a, modulo, values[0], values[1])
s.get(URL+f"/check_level/1/{value}").text

# LEVEL 3
t = s.get(URL) 
# getting values
html = t.text
tmp = html[html.index("<h2>Valori</h2>")+50:]
values = (tmp[0:tmp.index("</code>")]).split()
values = [int(s) for s in values]
# getting parameters
tmp = html[html.index("<code class=\"lang-python\">")+26:html.index("</code>")]
a = tmp[tmp.index("a = ")+4:tmp.index("b =")-5]
b = tmp[tmp.index("b = ")+4:tmp.index("modulo =")-5]
modulo = tmp[tmp.index("modulo = ")+9:-4]
a = int(a) if a != "unknown" else ""
b = int(b) if b != "unknown" else ""
modulo = int(modulo) if modulo != "unknown" else ""
value = level_2(b, modulo, values[0], values[1])
s.get(URL+f"/check_level/2/{value}")
print(s.get(URL).text.strip())