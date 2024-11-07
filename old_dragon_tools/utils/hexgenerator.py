from modules.dice import roll


def generateHex(terreno, clima):
    try:
        tabela4_2 = {
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

        resultado = roll(1, 6) - 3
        resultado = max(resultado, 0)  # Verifica se resultado é negativo e define como 0 se for
        tabelaterreno = tabela4_2[clima]
        tabelaresultados = tabelaterreno[terreno]
        hexagono = tabelaresultados[resultado] #Guarda o valor da checagem na tabela 4.2 do livro Ermos
        periculosidade = "(=)"
        if resultado == 2:
            periculosidade = "(↓)"
        if resultado == 3:
            periculosidade = "(↑)"
        
        tabela4_2a = {
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

        tabelatipoterreno = tabela4_2a[hexagono]
        tabelatipovegetacao = tabelatipoterreno["vegetacao"]
        tabelatiposolo = tabelatipoterreno["solo"]
        vegetacao = tabelatipovegetacao[roll(1, 6) - 1]
        solo = tabelatiposolo[roll(1, 6) - 1]
        
        return f'Foi encontrado um hexagono do tipo: {hexagono} {periculosidade}.\n\nCom Vegetação do Tipo: {vegetacao}\n\nSolo do tipo: {solo}'
    except:
        return f'Ocorreu Um Erro!'

    