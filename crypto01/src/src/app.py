import os
from flask import Flask, render_template, request, make_response
import json
import random

app = Flask(__name__)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted_flag = "QSGOFSIGOJOIBQWTFOFWCGWAWZS"

def encrypt(plaintext, key):
    assert key < len(alphabet) and key > 0
    ciphertext = ""
    for c in plaintext:
        ciphertext += alphabet[(alphabet.index(c) + key) % 26] 

    return ciphertext

@app.route("/")
def index():
    resp = make_response(render_template("index.html", encrypted_flag="".join(str(encrypted_flag))))
    return resp

@app.route("/encrypt/<your_supposed_secret>/<key>")
def get_encrypted_message(your_supposed_secret, key):
    try:
        enc = encrypt(your_supposed_secret, int(key))
        return enc
    except:
        return "Input sbagliato. Il messaggio deve contenere solo lettere maiuscole e la chiave deve essere un numero compreso tra 1 e 26."
    

# SKIP
if __name__ == "__main__":
    app.run(debug=True)
