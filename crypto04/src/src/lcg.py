import random

class SimpleLinearCongruentialGenerator:
    def __init__(self, modulo):
        self.modulo = modulo
    
    def generate(self):
        self.value = (self.a*self.value + self.b) % self.modulo
        return self.value

    def init(self):
        self.value = random.randint(1,self.modulo)
        self.a = random.randint(1,self.modulo)
        self.b = random.randint(1,self.modulo)
    