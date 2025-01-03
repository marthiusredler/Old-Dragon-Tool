from utils.dice import NewDice

def makeNavigationTest(local, have_bad_weather = False, have_natural_light = True, night_travel = False):
    result = ''
    testModificator = 0
    twoD6 = NewDice(2, 6)
    
    if have_bad_weather:
        testModificator -= 4
	
    if not have_natural_light:
        testModificator -= 2
  
    if night_travel:
        testModificator -= 4 

    ground_type = {
		'planicie' : -1,
		'colina' : -2,
		'floresta' : -2,
		'deserto' : -2,
		'geleira' : -3,
		'pantano' : -3,
		'montanha' : -4,
    }
	
    testModificator += ground_type[local]
    testResult = twoD6.roll() + testModificator	
	
	#Navigation1
    if testResult < -3:
        result = f'Seguem para direção Indesejada. - 🡣'
    elif testResult == -2:
        result = f'Seguem para direção Indesejada. - 🡦'
    elif testResult == -1:
        result = f'Seguem para direção Indesejada. - 🡧'
    elif testResult == 0:
        result = f'Seguem para direção Indesejada. - 🡤'
    elif testResult == 1:
        result = f'Seguem para direção Indesejada. - 🡥'
    else:
        result = f'Seguem para direção Desejada. - 🡡'
    
    return result