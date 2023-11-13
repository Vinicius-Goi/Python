f = "Quero férias"
print(f'{"/.count()/":-^40}')
print(f'A frase "{f}" tem {f.count("r")} letras "r"')

f = "Queremos ter férias"

print(f'A frase "{f} tem {f.count("e",0, 7)} letras "e"\n')

print(f'{"/=EXEÇÃO=/":-^40}')
print(f'A frase "{f} tem {f.count("R")} letras "R"\n')
f = "Queremos ter férias"

print(f'{"/.find()/":-^40}')
print(f'Frase: {f}')
print(f'O trecho "remos" se inicia na {f.find("remos")}º casa')
print(f'O trecho "er" se inicia na {f.find("er", 7, 12)}º casa\n')




print(f'O trecho "vamos" se inicia na {f.find("vamos")}º casa\n')
quantL = input("Digite quantos números o dado vai ter: ")
if quantL.find('.') != -1:
    print('-=' * 30)
    print(f'\033[1:31m{"DIGITE UM NÚMERO INTEIRO!":^60}\033[m')
    print('-=' * 30)

print(f'{"/.rfind()/":-^40}')
f="um tigre, dois tigres, três tigres"
print("Frase:", f)
print(f"A palavra 'tigres' da direita para a esquerda está localizada na {f.rfind('tigres')}º casa\n")

print(f'{"/in/":-^40}')
f = "Queremos ter férias"
print(f'Frase: {f}')
print("férias" in f)
print("vamos" in f)

print(f'{"/len()/":-^40}')
f = "Quero férias"
print(f'A frase "{f}" tem {len(f)} caracteres (CONTANDO COM OS ESPAÇOS)\n')

print(f'{"/Exercício/":-^40}')
print("""Faça um programa que leia uma frase digitada pelo usuário e mostre na tela:
	- Calcule o comprimento total da frase;
	- Conte quantas vezes cada vogal aparece na frase;
	- Conte quantos espaços a frase teve;
	- Encontre a posição da aparição da letra "v";
	- Encontre a posição da última aparição da letra "p".
""")

print(f'{"/Resolução/":-^40}')
frase = input("Digite uma frase: ").lower()
print(f"O comprimento total da frase é: {len(frase)}")
# print(f"A vogal 'a' apareceu: {frase.count('A') + frase.count('a')}")
# print(f"A vogal 'e' apareceu: {frase.count('E') + frase.count('e')}")
# print(f"A vogal 'i' apareceu: {frase.count('I') + frase.count('i')}")
# print(f"A vogal 'o' apareceu: {frase.count('O') + frase.count('o')}")
# print(f"A vogal 'u' apareceu: {frase.count('U') + frase.count('u')}")
print(f"""A vogal 'a' apareceu: {frase.count('A') + frase.count('a')}
A vogal 'e' apareceu: {frase.count('e')}
A vogal 'i' apareceu: {frase.count('I')}
A vogal 'o' apareceu: {frase.count('o')}
A vogal 'u' apareceu: {frase.count('u')}""") #Vogais
print(f'Na frase teve: {frase.count(" ")} espaços')
print("Não foi achado nenhuma letra 'v'." if frase.find('v') == -1 else f"Foi achado a primeira aparição da letra 'v' no índice {frase.find('v')}.")
print("Não foi achado nenhuma letra 'p'." if frase.rfind('p') == -1 else f"Foi achado a última aparição da letra 'p' no indice {frase.rfind('p')}")