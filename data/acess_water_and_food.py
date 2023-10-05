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
        
    if dice_test < margin_value + bonus:
        return f'Foi encontrado alimentos, um total de {1 + (ranger_points-1)} Ração(es) de Viagem.'
    else:
        return f'Não foi encontrado alimentos.'