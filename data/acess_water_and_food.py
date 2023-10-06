import sqlite3
from modules import dice
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'water_and_food.db'
DB_FILE = ROOT_DIR / DB_NAME

def get_forage_result(local, season, climate = 'temperado', ranger_points = 0):
    
    #Connection wtih DB
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    bonus = 0 + ranger_points
    dice_test = dice.roll(1, 6)
 
    #Mod by Climate
    if climate == 'tropical':
        bonus += 1
    elif climate == 'polar':
        bonus -= 1
    
    cursor.execute(
		f"""
		SELECT {season}
  		FROM 'forage' WHERE local = '{local}'
  		"""
	)
    
    for i in cursor.fetchall():
        margin_value = i[0]
    
    cursor.close()
    connection.close()
        
    if dice_test <= margin_value + bonus:
        return f'Foi encontrado alimentos, um total de {1 + (ranger_points-1)} Ração(es) de Viagem.'
    else:
        return f'Não foi encontrado alimentos.'

def get_hunt_result(local, season, climate = 'temperado', ranger_points = 0, more_people = False):
    
    #Connection wtih DB
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    bonus = 0 + ranger_points
    dice_test = dice.roll(1, 6)
    dice_bonus = 0
    
    if more_people:
        bonus -= 1
        dice_bonus += 1
        
    #Mod by Climate
    if climate == 'tropical':
        bonus += 1
    elif climate == 'polar':
        bonus -= 1
    
    cursor.execute(
		f"""
		SELECT {season}
  		FROM 'hunt' WHERE local = '{local}'
  		"""
	)
    
    for i in cursor.fetchall():
        margin_value = i[0]
    
    cursor.execute(
		f"""
		SELECT amount_dice, side_dice
  		FROM 'hunt_result' WHERE dice_value = '{dice_test+dice_bonus}'
  		"""
	)
    
    for i in cursor.fetchall():
        dice_info = i
        
    amount, sides = dice_info
    
    cursor.close()
    connection.close()
        
    if dice_test <= margin_value + bonus:
        return f'Foi bem sucedida a caça, rendendo um total de {dice.roll(amount, sides)} Ração(es) de Viagem.'
    else:
        return f'Não foi encontrado alimentos.'

def get_water_result(local, season, climate = 'temperado', ranger_points = 0):
    
    if local == 'geleira':
        return f'Foi encontrado Água Potavel no Local.'
    
    #Connection wtih DB
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    bonus = 0 + ranger_points
    dice_test = dice.roll(1, 6)
    if local == 'deserto':
        dice_test = dice.roll(2, 6)
    
    #Mod by Climate
    if climate == 'tropical':
        bonus += 1
    elif climate == 'polar':
        bonus -= 1
    
    cursor.execute(
		f"""
		SELECT {season}
  		FROM 'water' WHERE local = '{local}'
  		"""
	)
    
    for i in cursor.fetchall():
        margin_value = i[0]
    
    cursor.close()
    connection.close()
        
    if dice_test <= margin_value + bonus:
        return f'Foi encontrado Água Potavel no Local.'
    else:
        return f'Não foi encontrado Água Potavel no Local.'
