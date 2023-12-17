import os
from flask import Flask, render_template, request, make_response, session
from flask_session import Session
import json
import random
from lcg import *
from Crypto.Util.number import getPrime
from hashlib import sha256


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

flag = os.environ["FLAG"]


@app.route("/")
def index():
  
    if not session.get("modulo"):
        session["modulo"] = getPrime(8)

    if not session.get("levels") and not session.get("values_at_levels"):
        session["levels"] = [False, False, False]
        session["values_at_levels"] = [-1, -1, -1]


    if session["levels"][0] and session["levels"][1] and session["levels"][2]:
        return flag
    elif not session["levels"][0]:
        LCG = SimpleLinearCongruentialGenerator(session["modulo"])
        LCG.init()
        # a, b, module
        list_of_values = [ LCG.generate() for _ in range(1)]
        temp_values = session.get("values_at_levels")
        temp_values[0] = LCG.generate()
        session["values_at_levels"] = temp_values
        description = ""
        resp = make_response(render_template("index.html",level="".join(str(0)), a="".join(str(LCG.a)), b="".join(str(LCG.b)), modulo="".join(str(LCG.modulo)), values="\n".join([str(i) for i in list_of_values])))
        return resp
    elif not session["levels"][1]:
        LCG = SimpleLinearCongruentialGenerator(session["modulo"])
        LCG.init()
        # only a and module
        list_of_values = [ LCG.generate() for _ in range(2)]
        temp_values = session.get("values_at_levels")
        temp_values[1] = LCG.generate()
        session["values_at_levels"] = temp_values

        description = ""
        resp = make_response(render_template("index.html",level="".join(str(1)), a="".join(str(LCG.a)), b="unknown", modulo="".join(str(LCG.modulo)), values="\n".join([str(i) for i in list_of_values])))
        return resp
    else:
        LCG = SimpleLinearCongruentialGenerator(session["modulo"])
        LCG.init()
        # print third level
        list_of_values = [ LCG.generate() for _ in range(2)]
        temp_values = session.get("values_at_levels")
        temp_values[2] = LCG.generate()
        session["values_at_levels"] = temp_values
        description = ""
        resp = make_response(render_template("index.html",level="".join(str(2)), a="unknown", b="".join(str(LCG.b)), modulo="".join(str(LCG.modulo)), values="\n".join([str(i) for i in list_of_values])))
        return resp
        
        
    


@app.route("/check_level/<level>/<value>")
def check_level(level, value):
    global levels
    try:
        level = int(level)
        value = int(value)

        if not session["levels"][level]:
            if value == session["values_at_levels"][level]:
                l = session["levels"]
                l[level] = True
                session["levels"] = l
                return "Ben fatto"
            else:
                return f"Sbagliato"
        else:
            return "Livello già risolto"
            

    except:
        return "Parametri sbagliati"


@app.route("/division/<value1>/<value2>")
def division(value1, value2):
    try:
        v1 = int(value1)
        v2 = int(value2)
        v2_inverse = pow(v2, -1, session["modulo"])
        return str((v1 * v2_inverse) % session["modulo"])
    except:
        return "L'inverso modulare non esiste per questo valore."



if __name__ == "__main__":
    app.run(debug=True)
