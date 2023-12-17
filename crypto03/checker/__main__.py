#!/bin/python3

import os
import requests
from pwn import *
import logging
logging.disable()


permutations = [
    [4, 1, 0, 3, 5, 2, 6, 7],
    [2, 6, 7, 0, 1, 3, 5, 4] ,
    [5, 2, 3, 7, 4, 0, 1, 6] ,
    [2, 6, 0, 3, 4, 7, 5, 1],
    [1, 2, 0, 4, 7, 5, 6, 3]
]

# cipher code
def apply_permutation(list_of_bits, permutation):
    temp=[list_of_bits[i] for i in permutation]
    return temp

def round(list_of_bits, permutation):
    temp = apply_permutation(list_of_bits, permutation)
    return temp

# value is a binary string representing a number which is the secret
def encrypt(value, permutations):
    ROUNDS = len(permutations)
    # make the list of bits from value
    list_of_bits = [i for i in value]

    # applying permutations to list_of_bits
    for i in range(ROUNDS):
        list_of_bits = round(list_of_bits, permutations[i])
    
    # convert binary list to integer
    binary = "".join([str(i) for i in list_of_bits]).zfill(8)
    return binary

def reverse_permutation(permutation):
    temp = [0 for _ in range(len(permutation))]
    for i in range(len(permutation)):
        temp[permutation[i]] = i
    
    return temp

def reverse_permutations(permutations):
    reversed = []
    for i in range(len(permutations)-1, -1, -1):
        reversed.append(reverse_permutation(permutations[i]))
    return reversed
    

# Per le challenge web
URL = os.environ.get("URL", "http://permutation.challs.cyberhighschools.it")
if URL.endswith("/"):
   URL = URL[:-1]


s = requests.session()
t = s.get(URL)
html = t.text
tmp = html[html.index("<h2>Segreto cifrato</h2>")+59:]
value = (tmp[0:tmp.index("</code>")]).zfill(8)
inverse_permutations = reverse_permutations(permutations)
secret = encrypt(value, inverse_permutations)

print(s.get(URL+f"/get_flag/{secret}").text)