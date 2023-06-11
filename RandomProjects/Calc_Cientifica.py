#importando o tkinter como tk, ou seja, para puxar ele, não é necessario mais tkinter. e sim tk.
import tkinter as tk
import math

#"pre-set" dos botões
botao_config = {
    "bg":"#242742",
    "fg":"#d1d2de",
    "font":("Consolas bold", 12),
    "height":"2",
    "width":"7",
    "relief":"flat",
    "activebackground":"#313454"
    }

#esses digitos vão receber um tratamento especial para passar na biblioteca math
digitos = ["√", "x²", "C", "n!", "sin", "cos", "tan", "sin-¹", "cos-¹", "tan-¹"]

#deg e inversa_deg fazem referencia a função de inverter o resultado das trigonometricas de radianos para graus, e vice versa
deg = inversa_deg = 1
#já a variavel cnt é a variavel de controle para essa conversão de graus para radiano
cnt = 0

class Calculdora:
    #metodo construtor q é iniciado automaticamente (com a ajuda do init) assim q criarmos uma instancia da nossa classe
    def __init__(self, master):
        self.master = master
        #janela base, master, podemos utilizar essa janela em qualquer metodo q esteja na classe calculadora

        #iremos fazer 2 displays, um q exibe o visor da calculadora e o outro, os botões
        #Display visor
        self.displayFrame = tk.Frame(self.master)
        self.displayFrame.pack()

        #Display botões
        self.buttonsFrame = tk.Frame(self.master)
        self.buttonsFrame.pack()

        #o display será feito com uma entrada de dados
        #ent criaremos essa entrada com o Entry()

        self.output = tk.Entry(self.displayFrame,
                               width=30,relief="sunken",bd=3,font=("Consolas bold",17), fg="#c9c9c5",bg="#242742")
        # sunken é um tipo de relevo
        self.output.grid(row = 0, column= 0)

        self.converte = tk.Button(self.displayFrame,
                                  botao_config, width=3, height= 0, text="DEG", bg="#e35124", command= self.degreesRadians)

        self.converte.grid(row=0, column=1)

        self.criarBotoes()

    def criarBotoes(self):
        #para n criarmos cada botão de forma manual, iremos fazer um array 2D para determinarmos a coluna e a linha dele
        self.botoes = [
            #matriz de botões, parecido com um rascunho para se "guiar"
            ["√", "x²", "**", "(", ")", "/"],
            ["sin", "cos", "7", "8", "9", "+"],
            ["sin-¹", "cos-¹", "4", "5", "6", "-"],
            ["tan", "tan-¹", "1", "2", "3", "*"],
            ["n!", "π", ".", "0", "=", "C"]
            ]
        for linha in range(len(self.botoes)):
            for coluna in range(len(self.botoes[linha])):
                texto = self.botoes[linha] [coluna]

                #criando os botões
                #a cada iteração vamos criar um novo botão com um texto diferente, de acordo com o indice q os "for's" estão acessando

                # por conta da criação de botões ser em loop, n podemos add o "command=" pois todos eles teriam a mesma função
                #para evitar poderiamos passar um argumento para o tratamento de eventos, porem em teoria o tkinter n possibilita essa passagem de argumentos para uma função chamada pelo "command="
                #porem na pratica podemos usar as funções anonimas: lambda

                #lambda = ele permite a declaração de uma expressão sem a necessidade de criar um def (metodo) função
                #(sintaxe) lambda x,y : expressão

                b = tk.Button(self.buttonsFrame, botao_config, text=texto, command= lambda x = texto: self.acaoBotoes(x))
                b.grid(row=linha, column=coluna)

    def acaoBotoes(self, texto):
        #novamente acessando as variaveis fora do escopo da classe
        global deg
        global inversa_deg
        #aqui ocorre um erro, onde o lambda vai sobreescrever o lambda anterior, ou seja qualquer botão aqui aparecerá como o "C", já q ele é a ultima str tratada e passado para o metodo acaoBotoes
        #e para resolver isso é só colocar cada interação para cada um botão diferente

        #toda a funcionalidade vai ser baseada em if, elif e else
        if texto != "=":
            if texto not in digitos:
                #metodo para colocar/concatenar no display os digitos digitados, podendo ser definido como 0 (da esquerda para direita) ou 'end', q é ao contrario
                self.output.insert('end', texto)
            else:
                if texto == "√":
                    self.addValor(math.sqrt(float(self.output.get())))
                elif texto == "n!":
                    self.addValor(math.factorial(float(self.output.get())))
                elif texto == "x²":
                    self.addValor(float(self.output.get()) ** 2)
                elif texto == "C":
                    self.addValor("")
                elif texto == "π":
                    self.addValor(3.1415926535897932)
                elif texto == "sin":
                    self.addValor(math.sin(float(self.output.get()) * deg))
                elif texto == "cos":
                    self.addValor(math.cos(float(self.output.get()) * deg))
                elif texto == "tan":
                    self.addValor(math.tan(float(self.output.get()) * deg))
                elif texto == "sin-¹":
                    self.addValor(math.asin(float(self.output.get()) * inversa_deg))
                elif texto == "cos-¹":
                    self.addValor(math.acos(float(self.output.get()) * inversa_deg))
                elif texto == "tan-¹":
                    self.addValor(math.atan(float(self.output.get()) * inversa_deg))
        else:
            #eval é uma função pronta do python que adquire uma expressão no formato str e calcula
            #ou seja se digitarmos a str 4+4 ele vai fazer a soma normalmente e retornar 8, que será passado para o addValor que será passado para o display
            self.addValor(eval(self.output.get()))

    def addValor(self, valor):
        '''# para conseguir o valor digitado no display, devemos utilizar o metodo get armazenado numa variavel "valor"
        # LEMBRANDO QUE O METODO GET RETORNA O VALOR EM STR
        valor = float(self.output.get())'''
        #limpando o output para os valores n se concatenarem e assim n ficar um resultado junto exemplo "√25=255.0" o 25 q foi o valor digitado está concatenando o 5 q é o valor final
        self.output.delete(0, 'end')
        self.output.insert('end', valor)


    def degreesRadians(self):
        #acessando os valores fora do escopo da nossa calculadora
        global deg
        global inversa_deg
        global cnt

        #de radianos para graus
        if (cnt==0):
            #deg serve para as trigonometricas normais, seno, cosseno e tangente
            deg = math.pi / 180
            inversa_deg = 180 / math.pi
            #trocando o texto do botão para RAD
            self.converte['text'] = "RAD"
            cnt = 1
        else:
            deg = 1
            inversa_deg = 1
            self.converte['text'] = "DEG"
            cnt = 1


raiz = tk.Tk()

Calculdora(raiz)

raiz.mainloop()