import random
from palavra import palavras
import string


def palavra_valida(palavras):
    palavra = random.choice(palavras) #randomizar escolhas na lista
    while '-' in palavra or ' ' in palavra:
        palavra = random.choice(palavras)

    return palavra.upper()


def hangman():
    palavra = palavra_valida(palavras)
    letras_palavras = set(palavra) #letras na palavra
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set() #o que o usuario adivinhou

    vidas = 6

    #obtendo uma entrada do usuario
    while len(letras_palavras) > 0 and vidas > 0:
        # letras usadas
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('\033[1mVocê tem', vidas, 'vidas e usou essas letras: \033[m', ' '.join(letras_usadas))

        #Qual é a palavra atual (P - L - V R -)
        lista_de_palavras = [letras if letras in letras_usadas else '-' for letras in palavra]
        print('Palavra atual: ', ' '.join(lista_de_palavras))

        letra_usuario = input('Adivinhe uma letra: ').upper()
        if letra_usuario in alfabeto - letras_usadas:
            letras_usadas.add(letra_usuario)
            if letra_usuario in letras_palavras:
                letras_palavras.remove(letra_usuario)

            else:
                vidas = vidas - 1 #tirando uma vida com a letra errada
                print('Essa letra \033[4;31mNÃO\033[m está na palavra!')

        elif letra_usuario in letras_usadas:
            print('Você já usou esse caractere! Por favor, tente novamente.')

        else:
            print('Caractere \033[4;31mINVÁLIDO\033[m! Por favor, tente novamente.')

    #conseguindo onde len(letras_palavras) == 0 OU quando a vida == 0
    if vidas == 0:
        print('Você \033[4;31mMORREU\033[m. A palavra era', palavra)
    else:
        print('Você \033[4;32mADIVINHOU\033[m a palavra', palavra,'!!' )

hangman()