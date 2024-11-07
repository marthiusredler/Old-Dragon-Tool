from random import randint

def roll(qtd = 1, sides = 2):
    """
    function that receives the quantity of dice and then the number of faces to return the result of a roll.

    Args:
        qtd (_int_): _quantity of dice that will be tested_
        sides (_int_): _number of sides on each dice_
    
    Returns:
        _int_: _generate an result based in quantity and sides_
    """
    sides = qtd*sides
    result = randint(qtd, sides)
    return result
