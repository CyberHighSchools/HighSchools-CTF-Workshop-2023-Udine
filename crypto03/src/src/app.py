import os
from flask import Flask, render_template, request, make_response, session
from flask_session import Session
import json
import random
from cipher import *
from hashlib import sha256


app = Flask(__name__)
# app.secret_key = sha256(os.urandom(16)).hexdigest()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

flag = os.environ["FLAG"]


permutations = [
    [4, 1, 0, 3, 5, 2, 6, 7],
    [2, 6, 7, 0, 1, 3, 5, 4] ,
    [5, 2, 3, 7, 4, 0, 1, 6] ,
    [2, 6, 0, 3, 4, 7, 5, 1],
    [1, 2, 0, 4, 7, 5, 6, 3]
]

def is_binary_string(v):
    for c in v:
        if c != '0' and c != '1':
            return False
    return True

@app.route("/")
def index():
    session["Secret"] = bin(int.from_bytes(os.urandom(1), byteorder='big'))[2:].zfill(8)
    session["attempts"] = 0
    session["encrypted"] = encrypt(session["Secret"], permutations)
    assert session["Secret"] == encrypt(session["encrypted"], reverse_permutations(permutations))

    resp = make_response(render_template("index.html", encrypted="".join(str(session["encrypted"]))))
    return resp



@app.route("/get_flag/<your_supposed_secret>")
def check_flag(your_supposed_secret):
    
    if session.get("attempts") > 3:
        return "Hai finito i tentativi. Il segreto viene rigenerato."
    session["attempts"] += 1
    your_supposed_secret = your_supposed_secret.zfill(8)
    if not is_binary_string(your_supposed_secret):
        return "Input sbagliato. Dev'essere una stringa binaria."
    try:
        if your_supposed_secret == session["Secret"]:
            return flag
        else:
            return "Sbagliato"
    except Exception as e:
        return str(e)


@app.route("/permute",  methods=["POST"])
def permute():
    if not request.method == 'POST':
        return "Method not allowed"

    whitelist = [' ', ',', '0', '1', '2', '3', '4', '5', '6', '7', ']', '[']
    permutation_list = request.form.get('permutation_list')
    print(permutation_list)
    your_value = request.form.get('value')

    for i in permutation_list:
        if i not in whitelist:
            return "La permutazione è sbagliata. Dev'essere contenuta all'interno di parentesi quadre e i valori devono essere da 0 a 7 separati da una virgola."
    
    permutation_list = [i for i in eval(permutation_list)]
    if len(permutation_list) != 8:
        return "La lunghezza delle permutazioni dev'essere 8"
    
    for i in range(8):
        if i not in permutation_list:
            return f'{i} non è nella lista'
    
    if not is_binary_string(your_value):
        return "Input sbagliato. Dev'essere una stringa binaria."

    return encrypt(your_value.zfill(8), [permutation_list])




# SKIP
if __name__ == "__main__":
    app.run(debug=True)
