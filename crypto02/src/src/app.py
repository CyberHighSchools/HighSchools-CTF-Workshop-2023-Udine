import os
from flask import Flask, render_template, request, make_response, session
from flask_session import Session
import json
import random
from Crypto.Util.number import isPrime
from hashlib import sha256

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


def search_value():
    l = []
    for i in range(200,1024):
        if isPrime(i-1) and isPrime(i**2+1) and isPrime(i-3) and isPrime(i+17):
            l.append(i)
    return l

flag = os.environ["FLAG"]
possible_secrets = search_value()



def encrypt(value):
    return (value-1)*(value**2+1)*(value-3)*(value+17)
    

@app.route("/")
def index():
    session["Secret"] = random.choice(possible_secrets)
    session["attempts"] = 0
    session["encrypted"] = encrypt(session["Secret"])
    resp = make_response(render_template("index.html", encrypted="".join(str(session["encrypted"]))))
    return resp

@app.route("/get_flag/<your_supposed_secret>")
def get_encrypted_message(your_supposed_secret):
    
    if session.get("attempts") > 5:
        return "Hai finito i tentativi. Il segreto verrà rigenerato"
    session["attempts"] += 1
    try:
        value = int(your_supposed_secret)
        if value == session["Secret"]:
            return flag
        else:
            return "Sbagliato"
    except:
        return "Input sbagliato"

if __name__ == "__main__":
    app.run(debug=True)
