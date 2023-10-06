from modules import dice

def verifica_acampamento():
  
    tipo_acampamento = ""
    teste = dice.roll(1, 6)

  
    if teste in range(1, 2):
        tipo_acampamento = "seguro"
    elif teste in range(3, 5):
        tipo_acampamento = "normal"
    else:
        tipo_acampamento = "perigoso"
    
    tabela = {
        "seguro" : dice.roll(1, 12),
        "normal" : dice.roll(1, 6),
        "perigoso" : dice.roll(1, 4),
    }
    
    if tabela[tipo_acampamento] == 1:
        return f"Em um Acampamento {tipo_acampamento}, Há um Encontro."
    elif tabela[tipo_acampamento] == 2:
        return f"Em um Acampamento {tipo_acampamento}, Há uma Ocorrencia"
    else:
        return f"Em um Acampamento {tipo_acampamento}, Nada Ocorre"
