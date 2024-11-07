from old_dragon_tool.utils import dice

def get_navigation(local, have_bad_weather = False, have_natural_light = True, night_travel = False):
    
	ground_type = {
		'planicie' : -1,
		'colina' : -2,
		'floresta' : -2,
		'deserto' : -2,
		'geleira' : -3,
		'pantano' : -3,
		'montanha' : -4,
    }
	
	test_mod = ground_type[local]
 
	#Situational:
	if have_bad_weather:
		test_mod -= 4
	
	if not have_natural_light:
		test_mod -= 2
  
	if night_travel:
		test_mod -= 4
  
	dice_test = dice.roll(2, 6) + test_mod	
	
	#Navigation
	if dice_test < -3:
		return f'Seguem para direção Indesejada. - 🡣'
	elif dice_test == -2:
		return f'Seguem para direção Indesejada. - 🡦'
	elif dice_test == -1:
		return f'Seguem para direção Indesejada. - 🡧'
	elif dice_test == 0:
		return f'Seguem para direção Indesejada. - 🡤'
	elif dice_test == 1:
		return f'Seguem para direção Indesejada. - 🡥'
	else:
		return f'Seguem para direção Desejada. - 🡡'
