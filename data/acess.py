import sqlite3
from modules import dice
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'encounter_table.db'
DB_FILE = ROOT_DIR / DB_NAME

def find_result(local, difficulty, level):
    
    #Connection with DB
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    #animals must have other treatment
    if local == "animais":
        dice_value = dice.roll(1, 6)
        cursor.execute(
            f"""
            SELECT encounter, min_creatures, max_creatures
            FROM 'animais' WHERE dice_value = '{dice_value}'
            """
        )
        
        result = cursor.fetchall()
        result = result[0]
        
        cursor.close()
        connection.close()
        
        return result
    
    
    #QUALQUER must have other treatment
    elif local == "qualquer":
        
        if level == '1':
            level = 'beginner'
        elif level == '2':
            level = 'heroic'
        elif level == '3':
            level = 'advanced'
        else:
            pass
        
        dice_value = dice.roll(1, 12)
        cursor.execute(
            f"""
            SELECT encounter, min_creatures, max_creatures
            FROM 'qualquer' WHERE level = '{level}' AND dice_value = '{dice_value}'
            """
        )
        
        result = cursor.fetchall()
        result = result[0]
        
        cursor.close()
        connection.close()
        
        return result

    #humans must have other treatment
    elif local == "humano":
        dice_value = dice.roll(2, 6)
        cursor.execute(
            f"""
            SELECT encounter, min_creatures, max_creatures
            FROM 'humano' WHERE level = '{level}' AND dice_value = '{dice_value}'
            """
        )
        
        result = cursor.fetchall()
        result = result[0]
        
        cursor.close()
        connection.close()
        
        return result
    
    #extraplanar must have other treatment
    elif local == "extraplanar":
        
        if level == 'beginner':
            level = 1 
        elif level == 'heroic':
            level = 2
        elif level == 'advanced':
            level = 3
        else:
            pass
            
        dice_value = dice.roll(1, 8)
        cursor.execute(
            f"""
            SELECT encounter, min_creatures, max_creatures
            FROM 'extraplanar' WHERE level = '{level}' AND dice_value = '{dice_value}'
            """
        )
        
        result = cursor.fetchall()
        result = result[0]
        
        cursor.close()
        connection.close()
        
        return result
    
    #Define Result
    
    if difficulty == 'easy':
        difficulty = dice.roll(1, 6)
    elif difficulty == 'normal':
        difficulty = dice.roll(1, 10)
    elif difficulty == 'hard':
        difficulty = dice.roll(1, 12)

    cursor.execute(
        f"""
        SELECT encounter, min_creatures, max_creatures
        FROM {local} WHERE level = '{level}' AND dice_value = '{difficulty}'
        """
    )   
    
    result = cursor.fetchall()
    result = result[0]
    
    #close DB connection and cursor
    cursor.close()
    connection.close()
    
    return result
