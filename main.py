from modules import encounter, navigation, journey_points, camping
from data.acess_water_and_food import get_water_result, get_forage_result, get_hunt_result



print(journey_points.get_action_result('montanha', 'viajar'))
print(encounter.test_encounter('colina', 'easy', 'beginner', 'normal'))
print('')
print(encounter.get_encounter('geleira', 'easy', 'beginner'))
print('')
print(navigation.get_navigation('floresta', True))
print('')
print(camping.verifica_acampamento())
print('')
print(get_water_result('planicie', 'primavera', 'temperado'))

    