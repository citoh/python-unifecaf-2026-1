import re
from datetime import datetime

# -------------------------------
# FUNÇÕES DE VALIDAÇÃO
# -------------------------------

def validar_nome(nome):
    # seu código aqui
    return False


def validar_data(data):
    # seu código aqui
    return False


def validar_email(email):
    # seu código aqui
    return False


def validar_telefone(telefone):
    # seu código aqui
    return False


def validar_endereco(endereco):
    # seu código aqui
    return False


def validar_cep(cep):
    # seu código aqui
    return False


def validar_cpf(cpf):
    # seu código aqui
    return False


def validar_cnpj(cnpj):
    # seu código aqui
    return False


# -------------------------------
# DADOS PARA TESTE
# -------------------------------

nome = "João Silva"
data = "15/08/2000"
email = "joao.silva@email.com"
telefone = "(11)91234-567"
endereco = "Rua das Flores, 123"
cep = "12345-678"
cpf = "529.982.247-25"
cnpj = "12.345.678/0001-95"


# -------------------------------
# TESTES
# -------------------------------

print("Nome válido:", validar_nome(nome))
print("Data válida:", validar_data(data))
print("Email válido:", validar_email(email))
print("Telefone válido:", validar_telefone(telefone))
print("Endereço válido:", validar_endereco(endereco))
print("CEP válido:", validar_cep(cep))
print("CPF válido:", validar_cpf(cpf))
print("CNPJ válido:", validar_cnpj(cnpj))