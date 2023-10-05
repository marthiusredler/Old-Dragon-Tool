from modules.dice import roll
from data.acess import find_result

def get_encounter(local, difficulty, level):
    """
    Function that gets local, difficulty and level based in Tabelas de Monstros from Guia de Campanhas: Ermos and Livro Basico III: Monstros e Inimigos

    Args:
        local (_string_): _Local that players will be, can be: planicie, montanha, colina, pantano, geleira, floresta, deserto, oceano, qualquer, in same have: animais, extraplanares and humanos_
        difficulty (_string_): _description_
        level (_strings_): _description_

    Returns:
        _string_: _generate encounter basead in args_
    """    
    try:
        exceptions = ['animais', 'qualquer', 'extraplanar', 'humano']
        not_have_exception = True
        monster = ''
        min_m = '0'
        
        for item in exceptions:
            if item == local:
                not_have_exception = False
                break
        
        if not_have_exception:
            resultado = find_result(local, difficulty, level)
            monster, min_m, max_m = resultado

        
        #treatament for animals
        if monster == 'animais' or local == 'animais':
            resultado = find_result('animais', difficulty, level)
            monster, min_m, max_m = resultado

        
        #treatament for "Qualquer" type 
        if monster == 'qualquer' or local == 'qualquer':
            if not min_m == '0':
                min_m = str(min_m)
                resultado = find_result('qualquer', difficulty, min_m)
                monster, min_m, max_m = resultado
            else:
                resultado = find_result('qualquer', difficulty, level)
                monster, min_m, max_m = resultado

        #treatament for "Extraplanar" type 
        if monster == 'extraplanar' or local == 'extraplanar':
            if not min_m == '0':
                min_m = str(min_m)
                resultado = find_result('extraplanar', difficulty, min_m)
                monster, min_m, max_m = resultado
            else:
                resultado = find_result('extraplanar', difficulty, level)
                monster, min_m, max_m = resultado

        #treatament for "humano & semi-humanos" type 
        if monster == 'humano' or local == 'humano':
            resultado = find_result('humano', difficulty, level)
            monster, min_m, max_m = resultado
            if monster == "especial":
                resultado = find_result('humano', difficulty, 'especial')
                monster, min_m, max_m = resultado

        return f'Foi encontrado {roll(min_m, max_m)} {monster.capitalize()}.'

    except Exception as error:
        print(error)
        return f"Ocorreu Um Erro!"

def test_encounter(local, difficulty, level, danger):
    
    try:
        result = "" #Test results
    
        #Determines the chance of encounter based on table 3.1 of the Guia de Campanha: Ermos.
        encounter_chance = {
            'planicie' : 6,
            'colina' : 6,
            'floresta' : 10,
            'deserto' : 8,
            'geleira' : 8,
            'pantano' : 8,
            'montanha' : 10,
        }
        
        # Get the encounter_mod based in danger type based in Guia de Campanha: Ermos.
        if danger == 'perigoso':
            encounter_mod = 2
        elif danger == 'extremo':
            encounter_mod = 3
        else:
            encounter_mod = 1
        
        #roll dice result based in choice local.
        dice_test = roll(1, encounter_chance[local]) 
        
        #Based in dice test and hex danger, get the result of table, Guia de Campanha: Ermos.
        if dice_test <= encounter_mod:
            result += f'Há um Encontro\n{get_encounter(local, difficulty, level)}'
        else:
            result = 'Não há um encontro'

        return result
    
    except Exception as error:
        print(type(error))
        print(error.args)
        print(error)
        return 'Houve um Erro'
    