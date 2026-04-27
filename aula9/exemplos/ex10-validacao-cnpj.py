import re

def char_para_valor(c):
    if c.isdigit():
        return int(c)
    return ord(c.upper()) - 55  # A=10, B=11, ..., Z=35

def validar_cnpj(cnpj: str) -> bool:
    # Remove caracteres inválidos
    cnpj = re.sub(r'[^A-Za-z0-9]', '', cnpj)
    
    # Deve ter 14 caracteres
    if len(cnpj) != 14:
        return False
    
    # Elimina sequências repetidas
    if cnpj == cnpj[0] * 14:
        return False

    # Converte para valores numéricos
    valores = [char_para_valor(c) for c in cnpj]

    # Pesos
    pesos1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    pesos2 = [6] + pesos1
    
    # Primeiro dígito
    soma = sum(valores[i] * pesos1[i] for i in range(12))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Segundo dígito
    soma = sum(valores[i] * pesos2[i] for i in range(13))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    return valores[-2:] == [digito1, digito2]