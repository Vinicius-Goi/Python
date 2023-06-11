'''
valores = []

for i in range(5):
    linha = []
    for j in range(4):
        num = int(input("Digite um número: "))
        linha.append(num)
    valores.append(linha)

print("Ordem lida:")
for linha in valores:
    print(linha)

print("Ordem crescente:")
for linha in sorted(valores):
    print(linha)

print("Ordem decrescente:")
for linha in sorted(valores, reverse=True):
    print(linha)
'''
