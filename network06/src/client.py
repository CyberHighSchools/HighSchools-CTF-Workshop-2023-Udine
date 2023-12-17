import turtle as t

from morse import MORSE_CODE_DICT
from requests import post

SERVER_URL = "http://localhost:5000"


def pendown():
    t.pendown()
    post(f"{SERVER_URL}/pen", json={"action": "down"})


def penup():
    t.penup()
    post(f"{SERVER_URL}/pen", json={"action": "up"})


def forward(n):
    t.forward(n)
    post(f"{SERVER_URL}/forward", json={"amount": n})


def draw_dot():
    pendown()
    forward(10)
    penup()
    forward(10)


def draw_dash():
    pendown()
    forward(30)
    penup()
    forward(10)


def draw_letter_sep():
    penup()
    forward(30)
    pendown()


def draw_flag(flag):
    assert all(c in MORSE_CODE_DICT for c in flag)
    for c in flag:
        print(c, MORSE_CODE_DICT[c])
        for d in MORSE_CODE_DICT[c]:
            if d == ".":
                draw_dot()
            else:
                draw_dash()
        draw_letter_sep()


with open("../flags.txt") as f:
    flag = f.read().strip()

draw_flag(flag)

t.mainloop()
