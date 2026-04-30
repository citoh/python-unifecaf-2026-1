import re

def validar_cpf(cpf: str) -> bool:
    # Remove tudo que não for número
    cpf = re.sub(r'\D', '', cpf)

    # Deve ter 11 dígitos
    if len(cpf) != 11:
        return False

    # Elimina CPFs com todos os números iguais
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    return cpf[-2:] == f"{digito1}{digito2}"


