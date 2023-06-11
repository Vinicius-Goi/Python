import random
n = 'm'
p = 0
while p == 0:

    titulo = 'jogo da forca'
    print('-=-' * 10)
    print(titulo.center(30).title())
    print('-=-' * 10)


    n = str(input('Qual é o seu nome? ')).strip().capitalize()
    print('Muito bem-vindo {} ao jogo da forca!'.format(n))
    while True:
        print('-'*15)
        p = int(input('Escolha:\n1 para saber as regras.\n2 para iniciar o jogo.\n3 para sair.\n'))

        if p == 1:

            execucao = True

            while execucao:
                r = str(input('\nO jogo funciona da seguinte forma:'
                                  '\nA maquina irá escolher um tema e depois escolherá algo referente a esse tema, ele irá exibir a quantidade de letras da palavra/objeto e a forca.'
                                  '\nSe você acertar a letra, ele marcará a letra na determinada casa da palavra, se você errar, a maquina desenhará partes do corpo do boneco de palito, quando completar o boneco o jogador perderá a rodada.'
                                  '\nVocê entendeu as regras? [S/N].\n')).lower().strip()
                if r == 's':
                    break

        if p == 2:
            lista = ['Linguagem de promagração']
            sorteio_tema = str(random.choice(lista))

            str(print('O tema é: \033[31m{}\033[m'.format(sorteio_tema)))
            if sorteio_tema == 'Animes':
                subAnimes = ['Komi-San', 'Kaguya-Sama', 'Naruto', 'One Piece', 'One Punch', 'Dragon Ball']
                sorteio_subtema = str(random.choice(subAnimes)).lower()
                while True:
                    desenhar = print('''
______
|    |
|    
|   
|   
|''')
                    palavra = int(len(sorteio_subtema))
                    cont = palavra
                    #print('_'*palavra)
                    print(sorteio_subtema)
                    tentativa = str(input('Digite uma letra: ')).lower()
                    verificar = sorteio_subtema.count(tentativa)

                    if verificar == True:
                        print('Você \033[32mACERTOU!\033[m')

                    else:
                            print('''
______
|    |
|    O
|   
|   
|\nVocê \033[31mERROU!\033[m''')


            elif sorteio_tema == 'Filmes':
                subFilmes = ['Vingadores', 'Homem-Aranha', 'The Batman', 'High School Musical']
                sorteio_subtema = str(random.choice(subFilmes)).lower()
                while True:
                    desenhar = print('''
______
|    |
|    
|   
|   
|''')
                    palavra = int(len(sorteio_subtema))
                    cont = palavra
                    #print('_'*palavra)
                    print(sorteio_subtema)
                    tentativa = str(input('Digite uma letra: ')).lower()
                    verificar = sorteio_subtema.count(tentativa)

                    if verificar == True:
                        print('Você \033[32mACERTOU!\033[m')

                    else:
                        print('''
______
|    |
|    O
|   
|   
|\nVocê \033[31mERROU!\033[m''')



            elif sorteio_tema == 'Pessoas da sala':
                subPessoas = ['Here', 'Goi', 'Shelly', 'Migg', 'Tut', 'Ayumi', 'Barone', 'Igor', 'Isa', 'Rua', 'Luh', 'Mari', 'May',
                                    'Nathan', 'Raissa', 'Vihh']
                sorteio_subtema = str(random.choice(subPessoas)).lower()
                while True:
                    desenhar = print('''
______
|    |
|    
|   
|   
|''')
                    palavra = int(len(sorteio_subtema))
                    cont = palavra
                    #print('_'*palavra)
                    print(sorteio_subtema)
                    tentativa = str(input('Digite uma letra: ')).lower()
                    verificar = sorteio_subtema.count(tentativa)

                    if verificar == True:
                        print('Você \033[32mACERTOU!\033[m')

                    else:
                            print('''
______
|    |
|    O
|   
|   
|\nVocê \033[31mERROU!\033[m''')



            elif sorteio_tema == 'Objetos':
                subObj = ['Colher', 'Garfo', 'Faca', 'Prato', 'Garrafa', 'Pilha', 'Carregador', 'Fone']
                sorteio_subtema = str(random.choice(subObj)).lower()
                while True:
                    desenhar = print('''
______
|    |
|    
|   
|   
|''')
                    palavra = int(len(sorteio_subtema))
                    cont = palavra
                    #print('_'*palavra)
                    print(sorteio_subtema)
                    tentativa = str(input('Digite uma letra: ')).lower()
                    verificar = sorteio_subtema.count(tentativa)

                    if verificar == True:
                        print('Você \033[32mACERTOU!\033[m')

                    else:
                        print('''
______
|    |
|    O
|   
|   
|\nVocê \033[31mERROU!\033[m''')



            else:
                    subProgramas = ['Python', 'Java', 'JavaScript', 'Html', 'Css', 'C#', 'C+']
                    sorteio_subtema = str(random.choice(subProgramas)).lower()
                    while True:
                        desenhar = print('''
______
|    |
|    
|   
|   
|''')
                        palavra = int(len(sorteio_subtema))
                        cont = palavra
                        #print('_'*palavra)
                        print(sorteio_subtema)
                        tentativa = str(input('Digite uma letra: ')).lower()
                        verificar = sorteio_subtema.count(tentativa)

                        if verificar == True:
                            print('Você \033[32mACERTOU!\033[m')

                        else:
                                print('''
______
|    |
|    O
|   
|   
|\nVocê \033[31mERROU!\033[m''')



        if p == 3:
            exit('\033[35mObrigado por jogar! :)\033[m\n\n\033[7mJogo feito por Goi do 1ªDS\033[m')
            break


