import random

BITS = 5

def apply_poly(x, a, b, secret):
    return a*(x**2) + b*x + secret

def PSS_get_point(secret, a, b):
    x_coordinate = random.randint(-2**BITS, 2**BITS)
    y_coordinate = apply_poly(x_coordinate, a, b, secret)
    return (x_coordinate, y_coordinate)

