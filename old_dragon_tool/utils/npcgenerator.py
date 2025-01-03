import json
import random
from pathlib import Path

pathNames = Path(__file__).resolve().parent.parent / "utils" / "tables" / "names.json"
pathDetais = Path(__file__).resolve().parent.parent / "utils" / "tables" / "detais.json"

with open(pathNames, "r") as namesTable:
	namesTable = json.load(namesTable)

with open(pathDetais, "r") as detaisTable:
	detaisTable = json.load(detaisTable)

class NewNPC():
	def __init__(self, name= None, gender= None, race= None):
		self.gender = gender if gender else self.getGender()
		self.race = race if race else self.getRace()
		self.name = name if name else self.getName()
		
	def getName(self):
		firstNamePart = random.choice(namesTable[self.gender][self.race]["inicio"])
		secondNamePart = random.choice(namesTable[self.gender][self.race]["fim"])
		return (firstNamePart + secondNamePart).capitalize()
	

	def getGender(self):
		newGender = ["homem","mulher"]
		return random.choice(newGender)
	
	def getRace(self):
		newRace = ["humano", "anao", "elfo", "halfling", "meio-elfo", "gnomo"]
		return random.choice(newRace)

	def getDetais(self):
		pass #Finalizar os Detalhes.


npc = NewNPC()
npc2 = NewNPC("Marthius", "homem", "elfo")
print(f"Nome: {npc.name}\nGenero: {npc.gender}\nRaca: {npc.race}\n")
print(f"Nome: {npc2.name}\nGenero: {npc2.gender}\nRaca: {npc2.race}\n")