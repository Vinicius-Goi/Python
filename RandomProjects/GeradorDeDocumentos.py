from random import randint
op = ' '
while op not in "123":
    op = input("""
[ 1 ] Para Registro Geral (RG)
[ 2 ] Para Cadastro de Pessoas Físicas (CPF)
[ 3 ] Para Cadastro Nacional da Pessoa Jurídica (CNPJ)
Escolha: """)
    match op:

        case "1":
            doc = randint(0, 9)
            print(doc)