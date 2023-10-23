from modules import dice

def get_action_result(local: str, action: str):
    
    actions_and_costs = {
		'viajar': 'Valor do Hex', 
		'marchar': 'Metade do Hex', 
		'explorar': 'Dobro do Hex', 
		'descansar': '1 Ponto de Jornada', 
		'acampar': 'Todos os Ponto de Jornada', 
		'forragear': '1 Ponto de Jornada.', 
		'caçar': '2 Ponto de Jornada', 
		'pescar': '1 Ponto de Jornada', 
		'forragear': '1 Ponto de Jornada', 
	}
    
    entry_cost = {
		'planicie' : 1,
		'colina' : 2,
		'floresta' : 2,
		'deserto' : 2,
		'geleira' : 3,
		'pantano' : 3,
		'montanha' : 4,
	}
    
    other = (
    	f'Em trilha: Reduz o Custo em 1.\n'\
     	f'Em Estrada: Reduz o Custo em 2.\n'\
		f'Batedor: Aumenta o custo em 1.\n'\
		f'Clima instaveis: Aumenta o custo em 1.\n'\
		f'Viagem Noturna: Aumenta o custo em 1.\n'\
		f'Reorientação: 1 Ponto de Jornada.\n'\
		f'Perigos Naturais: 1 Ponto de Jornada.\n'\
	)
    
    return (
        f'{action.capitalize()} tem o custo: {actions_and_costs[action]}\n'\
        f'Custo de Pontos para {local.capitalize()} é de {entry_cost[local]} Ponto(s).\n'\
        f'{other}')