import os
from flask import Flask, render_template, request, make_response, session
from flask_session import Session
import json
import random
from hashlib import sha256

app = Flask(__name__)
# app.secret_key = sha256(os.urandom(16)).hexdigest()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

flag = os.environ["FLAG"]


def xor(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])


@app.route("/")
def index():
    if not session.get("Secret"):
        session["Secret"] = int.from_bytes(os.urandom(1), byteorder='big')

    if not session.get("KEY_INT"):
        session["KEY_INT"] = int.from_bytes(os.urandom(1), byteorder='big')

    if not session.get("attempts"):
        session["attempts"] = 0

    cookie = int(request.cookies.get('Encrypted Secret'), 2) if request.cookies.get('Encrypted Secret') else session["Secret"] ^ session["KEY_INT"]

    decrypted_secret = cookie ^ session["KEY_INT"]
    public_key = pow(decrypted_secret, 4) + pow(decrypted_secret, 3) + decrypted_secret + 1
    # This is a hack to get the source code of this file, excluding the SKIP
    resp = make_response(render_template("index.html", public_key="".join(str(public_key))))
    resp.set_cookie('Encrypted Secret', bin(cookie)[2:].zfill(8))

    return resp

@app.route("/get_flag/<your_supposed_secret>")
def get_flag(your_supposed_secret):
    
    if session["attempts"] > 20:
        session.pop("Secret", None)
        session.pop("KEY_INT", None)
        session.pop("attempts", None)
        return "Hai finito i tentativi (20). La chiave verrà rigenerata."
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
