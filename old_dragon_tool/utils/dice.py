from random import randint

class NewDice():
	def __init__(self, quantity: int, sides: int):
		self.__quantity = quantity
		self.__sides = sides

	def roll(self):
		result = randint(self.__quantity, self.__sides)
		return result

if __name__ == "__main__":
	d6 = NewDice(1, 6)
	print(d6.roll())