#1. Faça um Programa que peça dois números e imprima o maior deles.
'''
num1= int(input("Digite o 1º número: "))
num2= int(input("Digite o 2º número: "))
if num1 > num2:
    print(f"O maior número é {num1}.")
elif num2 > num1:
    print(f"O maior número é {num2}.")
else:
    print(f"Os número são iguais.")
'''

#2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
num = float(input("Digite um número: "))
if num < 0:
    print(f"O valor digitado, {num}, é negativo.")
else:
    print(f'O valor digitado, {num}, é positivo')
'''

#3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = input("Informe seu sexo [F/M]: ")
if sexo != "":
    if sexo in "Ff":
        print(f"O seu sexo é feminino!")
    elif sexo == "M" or sexo == "m":
        print(f'O seu sexo é masculino!')     
    else:
        print(f"Digite uma opção válida!")
else:
    print(f"Digite uma opção válida!")
'''

#4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input("Digite uma letra: ")[0]
if letra not in "0123456789":
    if letra in "aeiouAEIOU":
        print(f"A letra digitada, '{letra}', é uma vogal.")
    else:
        print(f"A letra digitada, '{letra}', é uma consoante.")
'''

'''
#5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;

    A mensagem "Reprovado", se a média for menor do que sete;

    A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
'''
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2)/2

if media == 10:
    print(f"Aprovado com distinção com uma média de {media:.2f}!")
elif media >= 7:
    print(f'Aprovado com uma média de {media:.2f}!')
else:
    print(f"Reprovado com uma média de {media:.2f}!")
'''

#6. Faça um Programa que leia três números e mostre o maior deles.
'''
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 > num2 and num1 > num3:
    print(f"O número, {num1}, é maior")
elif num2 > num1 and num2 > num3:
    print(f"O número, {num2}, é maior")
elif num3 > num1 and num3 > num2:
    print(f"O número, {num3}, é maior")
else:
    print("Os números são iguais!")
'''

#7. Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

#MAIOR
if num1 > num2 and num1 > num3:
    print(f"O número, {num1}, é maior")
elif num2 > num1 and num2 > num3:
    print(f"O número, {num2}, é maior")
elif num3 > num1 and num3 > num2:
    print(f"O número, {num3}, é maior")

#MENOR
if num1 < num2 and num1 < num3:
    print(f"O número, {num1}, é o menor!")
elif num2 < num1 and num2 < num3:
    print(f"O número, {num2}, é o menor!")
elif num3 < num1 and num3 < num2:
    print(f"O número, {num3}, é o menor!")
else:
    print("Os números são iguais!")
'''

#8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
'''
num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))

if num1 < num2 and num1 < num3:
    print(f"Compre o 1º produto!")
elif num2 < num1 and num2 < num3:
    print(f"Compre o 2º produto!")
elif num3 < num1 and num3 < num2:
    print(f"Compre o 3º produto!")
else:
    print("Os preços são iguais!")
'''

#9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
lista = [n1, n2, n3]
lista.sort(reverse=True)

for num in lista:
    print(f"{num} ", end='')
'''

#10.Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem: "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso
"""
pEstudo = input('''Digite:
[ M ] Para horário Matutino;
[ V ] Para horário Vespertino;
[ N ] Para horário Noturno.''')
if pEstudo in "Mm":
    print("Bom Dia!")
elif pEstudo in "Vv":
    print("Boa Tarde!")
elif pEstudo in "Nn":
    print("Boa Noite!")
else:
    print("Digite um valor válido!")
"""

#11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes
'''
sal = float(input("Informe seu salário: R$"))
if sal <= 280:
    novo_sal = sal + (sal * 20/100)
    print(f"""Salário antes do aumento: R${sal:.2f}
Salário depois do aumento de 20%: {novo_sal:.2f}
Valor do aumento: {novo_sal-sal:.2f}""")

elif sal > 280 and sal <= 700:
    novo_sal = sal + (sal * 15/100)
    print(f"""Salário antes do aumento: R${sal:.2f}
Salário depois do aumento de 15%: {novo_sal:.2f}
Valor do aumento: {novo_sal-sal:.2f}""")


elif sal > 700 and sal <= 1500:
    novo_sal = sal + (sal * 10/100)
    print(f"""Salário antes do aumento: R${sal:.2f}
Salário depois do aumento de 10%: {novo_sal:.2f}
Valor do aumento: {novo_sal-sal:.2f}""")

else:
    novo_sal = sal + (sal * 5/100)
    print(f"""Salário antes do aumento: R${sal:.2f}
Salário depois do aumento de 10%: {novo_sal:.2f}
Valor do aumento: {novo_sal-sal:.2f}""")
'''

#12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 8% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
'''
valor_hora = float(input("Informe o valor por hora: R$"))
quantidade_horas = int(input("Informe a quantidade de horas trabalhadas: "))
sal_bruto = quantidade_horas * valor_hora
print('-'*30)
if sal_bruto <= 1903.98:
    ir = 0
    fgts = (sal_bruto * 8/100)
    sindicato = (sal_bruto * 3/100)
    sal_liquido = sal_bruto - sindicato
    inss = (sal_bruto * 10/100)
    tot_descontos = sindicato + fgts + ir + inss
    
    print(f"""Salário Bruto: {sal_bruto:>20.2f}
IR: {ir:>31.2f}
INSS: {inss:>29.2f}
FGTS: {fgts:>29.2f}
Sindicato: {sindicato:>24.2f}
Total de desconos: {tot_descontos:>16.2f}
Salário Liquido: {sal_liquido:>18.2f}""")
    
elif sal_bruto > 1903.98 and sal_bruto <= 2836.65:
    ir = (sal_bruto * 7.5/100)
    fgts = (sal_bruto * 8/100)
    sindicato = (sal_bruto * 3/100)
    sal_liquido = sal_bruto - sindicato
    inss = (sal_bruto * 10/100)
    tot_descontos = sindicato + fgts + ir + inss
    
    print(f"""Salário Bruto: {sal_bruto:>20.2f}
IR: {ir:>31.2f}
INSS: {inss:>29.2f}
FGTS: {fgts:>29.2f}
Sindicato: {sindicato:>24.2f}
Total de desconos: {tot_descontos:>16.2f}
Salário Liquido: {sal_liquido:>18.2f}""")
    
elif sal_bruto > 2836.65 and sal_bruto <= 3751.05:
    ir = (sal_bruto * 15/100)
    fgts = (sal_bruto * 8/100)
    sindicato = (sal_bruto * 3/100)
    sal_liquido = sal_bruto - sindicato
    inss = (sal_bruto * 10/100)
    tot_descontos = sindicato + fgts + ir + inss
    
    print(f"""Salário Bruto: {sal_bruto:>20.2f}
IR: {ir:>31.2f}
INSS: {inss:>29.2f}
FGTS: {fgts:>29.2f}
Sindicato: {sindicato:>24.2f}
Total de desconos: {tot_descontos:>16.2f}
Salário Liquido: {sal_liquido:>18.2f}""")
    
elif sal_bruto > 3751.05 and sal_bruto <= 4664.68:
    ir = (sal_bruto * 15/100)
    fgts = (sal_bruto * 8/100)
    sindicato = (sal_bruto * 3/100)
    sal_liquido = sal_bruto - sindicato
    inss = (sal_bruto * 10/100)
    tot_descontos = sindicato + fgts + ir + inss
    
    print(f"""Salário Bruto: {sal_bruto:>20.2f}
IR: {ir:>31.2f}
INSS: {inss:>29.2f}
FGTS: {fgts:>29.2f}
Sindicato: {sindicato:>24.2f}
Total de desconos: {tot_descontos:>16.2f}
Salário Liquido: {sal_liquido:>18.2f}""")
    
elif sal_bruto > 4664.68:
    ir = (sal_bruto * 27.5/100)
    fgts = (sal_bruto * 8/100)
    sindicato = (sal_bruto * 3/100)
    sal_liquido = sal_bruto - sindicato
    inss = (sal_bruto * 10/100)
    tot_descontos = sindicato + fgts + ir + inss
    
    print(f"""Salário Bruto: {sal_bruto:>20.2f}
IR: {ir:>31.2f}
INSS: {inss:>29.2f}
FGTS: {fgts:>29.2f}
Sindicato: {sindicato:>24.2f}
Total de desconos: {tot_descontos:>16.2f}
Salário Liquido: {sal_liquido:>18.2f}""")
'''

#13.Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
dia = input("Digite um número (de 1 até 7): ")
match dia:
    case "1":
        print("1 - Domingo")
    case "2":
        print("2 - Segunda")
    case "3":
        print("3 - Terça")
    case "4":
        print("4 - Quarta")
    case "5":
        print("5 - Quinta")
    case "6":
        print("6 - Sexta")
    case "7":
        print("7 - Sabado")
    case _:
        print("Digite um valor válido!")
"""

#14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo.

n1 = float(input("Digite a 1ª Nota: "))
n2 = float(input("Digite a 2ª Nota: "))
md = (n1+n2)/2

if md >= 9 and md < 10:
    conce = "A"
    print("APROVADO!")
elif md >= 7.5 and md < 9:
    conce  = "B"
    print("APROVADO!")
elif md >= 6 and md < 7.5:
    conce = "C"
    print("APROVADO!")
elif md >= 4 and md < 6:
    conce = "D"
    print("REPROVADO!")
elif md < 4:
    conce = "E"
    print("REPROVADO!")