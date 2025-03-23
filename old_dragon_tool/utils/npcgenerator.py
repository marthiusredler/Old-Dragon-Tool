import json
import random
from pathlib import Path

pathNames = Path(__file__).resolve().parent.parent / "utils" / "tables" / "names.json"
pathDetails = Path(__file__).resolve().parent.parent / "utils" / "tables" / "details.json"

with open(pathNames, "r") as namesTable:
	namesTable = json.load(namesTable)

with open(pathDetails, "r") as detailsTable:
	detailsTable = json.load(detailsTable)

class NewNPC():
	def __init__(self, name= None, gender= None, race= None, hair= None, eyes= None, trace= None, voice= None, job= None):
		self.gender = gender if gender else self.getGender()
		self.race = race if race else self.getRace()
		self.name = name if name else self.getName()
		self.hair = hair if hair else self.getDetais("cabelo")
		self.eyes = eyes if eyes else self.getDetais("olhos")
		self.trace = trace if trace else self.getDetais("tracos")
		self.voice = voice if voice else self.getDetais("voz")
		self.job = job if job else self.getDetais("profissao")
		
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

	def getDetais(self, detail):
		return random.choice(detailsTable[self.race][detail])


npc = NewNPC()
print(f" Nome: {npc.name}\n",
	f"Genero: {npc.gender}\n",
	f"Raca: {npc.race}\n",
	f"Cabelo: {npc.hair}\n",
	f"Olhos: {npc.eyes}\n",
	f"Traços: {npc.trace}\n",
	f"Tom de Voz: {npc.voice}\n",
	f"Proffissão: {npc.job}\n",
	  )