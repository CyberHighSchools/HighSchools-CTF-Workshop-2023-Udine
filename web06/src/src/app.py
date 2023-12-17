from flask import Flask, render_template, request, redirect, session
import mariadb
import os
from flask_session import Session
from functools import wraps

app = Flask(__name__)

conn = mariadb.connect(
    host=os.environ.get("DATABASE_HOST"),
    port=int(os.environ.get("DATABASE_PORT")),
    user=os.environ.get("DATABASE_USER"),
    password=os.environ.get("DATABASE_PASSWORD"),
    database=os.environ.get("DATABASE_DB"),
)


def authenticated(f):
    @wraps(f)
    def authenticated_wrapper(*args, **kwargs):
        if session.get("user", None) is not None:
            return f(*args, **kwargs)
        else:
            return redirect("/login")

    return authenticated_wrapper


@app.get("/")
def index():
    user = session.get("user", None)
    return render_template("index.html", user=user)


@app.get("/login")
def login_page():
    return render_template("login.html")


@app.post("/login")
def login():
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (request.form["username"], request.form["password"]),
        )
        row = cur.fetchone()
        if row is None:
            return render_template("login.html", error="Accesso fallito")
        user = {
            "id": row[0],
            "username": row[1],
            "password": row[2],
            "is_admin": row[3],
        }
        session["user"] = user
    except mariadb.Error as e:
        return render_template("login.html", error=str(e))

    return redirect(f"/account/{user['id']}")


@app.get("/register")
def register_page():
    return render_template("register.html", error=None)


@app.post("/register")
def register():
    cur = conn.cursor()
    # Insert user
    try:
        cur.execute(
            "INSERT INTO users(username, password, is_admin) VALUES (?,?,?)",
            (request.form["username"], request.form["password"], False),
        )
        conn.commit()
    except mariadb.Error as e:
        return render_template(
            "register.html", error="Esiste già un utente con questo nome"
        )
    return redirect("/login")


@app.get("/account")
@authenticated
def account():
    return redirect(f"/account/{session['user']['id']}")


@app.get("/account/<int:id>")
@authenticated
def account_from_id(id):
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM users WHERE id = ?", (id,))
        row = cur.fetchone()
        if row is None:
            return render_template("404.html")
        user = {
            "id": row[0],
            "username": row[1],
            "password": row[2],
            "is_admin": row[3],
        }
        cur.execute("SELECT content FROM posts WHERE user_id = ?", (user["id"],))
        posts = cur.fetchall()
        posts = [x[0] for x in posts]
        return render_template("account.html", user=user, posts=posts)
    except mariadb.Error as e:
        return str(e)
    return render_template("404.html")


@app.post("/account/<int:id>")
@authenticated
def create_post(id):
    cur = conn.cursor()
    try:
        if id == session["user"]["id"]:
            cur.execute(
                "INSERT INTO posts (content, user_id) VALUES (?,?)",
                (
                    request.form["content"],
                    session["user"]["id"],
                ),
            )
            conn.commit()
            return redirect(f"/account/{session['user']['id']}")
    except mariadb.Error as e:
        return str(e)
    return redirect("/")


@app.get("/logout")
@authenticated
def logout():
    session.pop("user")
    return redirect("/")


if __name__ == "__main__":
    app.secret_key = os.environ.get("SECRET_KEY")
    app.run(host="0.0.0.0", port=3000)
    Session(app)
