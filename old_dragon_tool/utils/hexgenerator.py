from utils.dice import NewDice

def generateHex(terreno, clima):
    d6 = NewDice(1, 6)
    danger = "(=)"

    hextable = {
        "polar": {
            "oceano": ["oceano", "geleira", "planicie", "colina"],
            "geleira": ["geleira", "planicie", "oceano", "montanha"],
            "pantano": ["pantano", "geleira", "floresta", "planicie"],
            "floresta": ["floresta", "geleira", "colina", "montanha"],
            "planicie": ["planicie", "geleira", "floresta", "colina"],
            "deserto": ["deserto", "geleira", "colina", "montanha"],
            "colina": ["colina", "geleira", "planicie", "floresta"],
            "montanha": ["montanha", "geleira", "floresta", "planicie"],
        },
        "temperado": {
            "oceano": ["oceano", "pantano", "planicie", "colina"],
            "geleira": ["geleira", "planicie", "oceano", "montanha"],
            "pantano": ["pantano", "colina", "floresta", "planicie"],
            "floresta": ["floresta", "planicie", "colina", "montanha"],
            "planicie": ["planicie", "floresta", "pantano", "colina"],
            "deserto": ["deserto", "planicie", "colina", "montanha"],
            "colina": ["colina", "montanha", "planicie", "floresta"],
            "montanha": ["montanha", "colina", "floresta", "geleira"],
        },
        "tropical": {
            "oceano": ["oceano", "pantano", "floresta", "deserto"],
            "geleira": ["pantano", "planicie", "oceano", "floresta"],
            "pantano": ["pantano", "colina", "floresta", "planicie"],
            "floresta": ["floresta", "planicie", "colina", "montanha"],
            "planicie": ["planicie", "floresta", "pantano", "colina"],
            "deserto": ["deserto", "planicie", "colina", "floresta"],
            "colina": ["colina", "montanha", "planicie", "floresta"],
            "montanha": ["montanha", "colina", "floresta", "planicie"],
        },
    }

    detailstable = {
        "oceano": {
            "vegetacao": ["nenhuma", "gramíneas e cactos", "árvores esparsas", "árvores esparsas", "mata fechada", "mangue"],
            "solo": ["praia arenosa", "praia de casscalho", "baía", "laguna", "falésias", "cabo/pontal"],
        },
        "geleira": {
            "vegetacao": ["nenhuma", "nenhuma", "gramíneasx e musgo", "gramíneas e arbustos", "arbustos e musgos", "pinheiro erparsos"],
            "solo": ["deserto gelado", "deserto gelado", "glaciar", "glaciar", "moraina", "fiorde"],
        },
        "pantano": {
            "vegetacao": ["poucas árvores", "vegetação rasteira", "mato alto aquático", "bosque alagado", "floresta alagado", "turfeira"],
            "solo": ["lamaçal", "lagoas esparsas", "alagado e raso", "alagado e raso", "alagado e profundo", "alagado e profundo"],
        },
        "floresta": {
            "vegetacao": ["bosque", "floresta heterogênea", "floresta heterogênea", "pinheiros", "pinheiros", "selva fechada"],
            "solo": ["plano e regular", "plano e regular", "levemente irregular", "ondulações constantes", "rochoso e irregular", "acidentado c/ ravinas"],
        },
        "planicie": {
            "vegetacao": ["gramíneas", "mato alto e fechado", "arbustos esparsos", "árvores perquenas isoladas", "pequenos bosques", "árovres grandes esparsas"],
            "solo": ["plano e regular", "levemente irregular", "ondulações contantes", "acidentado c/ ravinas", "cânions", "leito rachado de lago seco"],
        },
        "deserto": {
            "vegetacao": ["nenhuma", "nenhuma", "gramíneas", "arbustos esparsos", "árvores isoladas e retorcidas", "cactos"],
            "solo": ["plano e arenoso", "dunas de ariea fofas", "acidentado com pedras", "deserto de sal plano", "acidentado c/ ravina", "cânion profundos"],
        },
        "colina": {
            "vegetacao": ["gramíneas", "nenhuma", "gramíneas", "arbustos esparsos", "árvores isoladas e retorcidas", "cactos"],
            "solo": ["plano e regular", "levemente irregular", "ondulações constantes", "acidentado c/ ravinas", "platôs do tipo mesa", "irregular c/ vales rasos"],
        },
        "montanha": {
            "vegetacao": ["nenhuma", "nenhuma", "gramíneas", "mato alto e fechado", "arbustos esparsos", "árvores isoladas"],
            "solo": ["rochoso e liso", "cascalho solto", "rochas pontudas", "rochas lisas com reentrâncias", "rochas escorregadias", "desfiladeiro"],
        },
    }
    
    #Verifica se dangerResult é negativo e define como 0 se for
    dangerResult = max((d6.roll() - 3), 0)  
    hexagono = hextable[clima][terreno][dangerResult]
    
    #Verifica baseado no dangerResultado das tabelas a periculosidade 
    if dangerResult == 2:
        danger = "(↓)"
    if dangerResult == 3:
        danger = "(↑)"
    
    #Verifica os detalhes do hexagono gerado
    vegetacao = detailstable[hexagono]["vegetacao"][d6.roll() - 1]
    solo = detailstable[hexagono]["solo"][d6.roll() - 1]

    result = (f'Foi encontrado um hexagono do tipo: {hexagono} {danger}.\nCom Vegetação do Tipo: {vegetacao}\nSolo do tipo: {solo}')
    
    return result
