from flask import Flask, abort, request

app = Flask(__name__)


@app.route("/pen", methods=["POST"])
def pen():
    if "action" not in request.json:
        return abort(400)
    if request.json["action"] == "down":
        print("pendown")
        pass
    elif request.json["action"] == "up":
        print("penup")
    else:
        return abort(400)
    return {"response": "ok"}


@app.route("/forward", methods=["POST"])
def forward():
    if "amount" not in request.json:
        return abort(400)
    amount = request.json["amount"]
    if not isinstance(amount, int):
        return abort(400)
    print(f"forward {amount}")
    return {"response": "ok"}


if __name__ == "__main__":
    app.run(port=5000)
