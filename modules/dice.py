from random import randint

def roll(qtd = 1, sides = 2):
    sides = qtd*sides
    result = randint(qtd, sides)
    return result
