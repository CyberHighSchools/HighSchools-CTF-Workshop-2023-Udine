import os
from flask import Flask, session, render_template, request, make_response
from flask_session import Session
import json
import random
from hashlib import sha256
from PSS import *

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#app.secret_key = sha256(os.urandom(16)).hexdigest()
Session(app)

flag = os.environ["FLAG"]


@app.route("/")
def index():
    session["Secret"] = random.randint(-2**BITS,2**BITS)
    session["attempts"] = 0

    a = random.randint(-2**BITS,2**BITS)
    b = random.randint(-2**BITS,2**BITS)


    Alice_point = PSS_get_point(session["Secret"], a, b)
    Bob_point = PSS_get_point(session["Secret"], a, b)
    while Bob_point == Alice_point:
        Bob_point = PSS_get_point(session["Secret"], a, b)

    Frank_point = PSS_get_point(session["Secret"], a, b)
    while Frank_point == Bob_point or Frank_point == Alice_point:
        Frank_point = PSS_get_point(session["Secret"], a, b)

    resp = make_response(render_template("index.html", alice=f"({Alice_point[0]} , {Alice_point[1]} )", bob=f"({Bob_point[0]} , {Bob_point[1]} )", frank=f"({Frank_point[0]} , {Frank_point[1]} )"   ))
    return resp



@app.route("/check_secret/<your_supposed_secret>")
def check_secret(your_supposed_secret):
    if session.get("attempts") is None:
        return "Errore interno: il segreto viene rigenerato."

    if session.get("attempts") > 2:
        return "Hai finito i tentativi. Il segreto viene rigenerato."
    session["attempts"] += 1
    try:
        if int(your_supposed_secret) == session["Secret"]:
            return flag
        else:
            return "Sbagliato"
    except Exception as e:
        return str(e)



# SKIP
if __name__ == "__main__":
    app.run(debug=True)
