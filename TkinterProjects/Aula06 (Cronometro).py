from tkinter import *
import tkinter #não é necessario, mas é para previnir

#cores
bg_color = "#282a36" #azul meio escuro, sla
text_color1 = "#bd93f9" #roxo
text_color2 = "#6272a4" #azul mais claro
text_color3 = "#d1d1cf" #cinza
title_color1 = "#de6db0" #rosa
title_color2 = "#ffb86c" #laranja
title_color3 = "#4add71" #verde

#configurando a janela
janela = Tk()
janela.title("")#é possivel deixar vazio :)
janela.geometry('600x360')
janela.config(bg=bg_color)#config e configure dá no mesmo
janela.resizable(width=False, height=False)
janela.iconphoto(False,PhotoImage(file='Python.png'))

#definindo variaveis globais

global tempo
global rodar
global contador
global limitador

limitador = 60
tempo = '00:00:00'
rodar = False #definindo se o cronometro vai iniciar ou n
contador = -5 #timer de 5s para iniciar o contador

#função iniciar
def iniciar():
    global tempo
    global contador
    global limitador


    if rodar:
        #antes do cronometro começar
        if contador <= -1:
            inicio = f'Começando em {contador}'
            label_tempo['font'] = 'OCRAStd 30'
            label_tempo['text'] = inicio
            label_tempo['fg'] = title_color1

        else:
            #depois de começar
            label_tempo['font'] ="OCRAStd 50 bold"

            temporaria = str(tempo)
            h, m, s = map(int, temporaria.split(':'))#escanear a str até achar um : e assim vai substituir para uma das variaveis
            h = int(h)
            m = int(m)
            s = int(contador)

            if s >= limitador:
                contador = 0
                m += 1

            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            #atualizando os valores atuais
            temporaria = str(h[-2:])+':'+str(m[-2:])+":"+str(s[-2:])#o -2 serve para pegar os dois ultimos caracteres da variavel h (hora)
            label_tempo['text'] = temporaria
            tempo = temporaria


        label_tempo.after(1000, iniciar)#1000 = 1s, a cada 1000 milisegundos, ele vai rodar a função iniciar
        contador += 1

#função para dar inicio ao rodar
def start():
    global rodar
    rodar = True
    iniciar()

#função para pausar
def pausar():
    global rodar
    rodar = False

#função para reiniciar
def reiniciar():
    global contador
    global tempo
    global rodar

    #reiniciando o tempo e o contador
    contador = -5
    rodar = False
    tempo = '00:00:00'
    label_tempo ['text'] = tempo







#label

label_app = Label(janela, text='Cronômetro', font='OCRAStd 20', bg=bg_color, fg=text_color2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font='OCRAStd 50 bold', bg=bg_color, fg=text_color1, relief='sunken')
label_tempo.place(x=100, y=100)


#botões
botao_iniciar = Button(janela, height=2, text='Iniciar', font='OCRAStd 15', bg=bg_color, fg=text_color2, relief='raised', overrelief='sunken', command=start)#overrelief serva para trocar o estilo assim q o mouse passar por ele
botao_iniciar.place(x=20, y=240)

botao_pausar = Button(janela, height=2, text='Pausar', font='OCRAStd 15', bg=bg_color, fg=text_color2, relief='raised', overrelief='sunken', command=pausar)
botao_pausar.place(x=235, y=240)

botao_reiniciar = Button(janela, height=2, text='Reiniciar', font='OCRAStd 15', bg=bg_color, fg=text_color2, relief='raised', overrelief='sunken', command=reiniciar)
botao_reiniciar.place(x=430, y=240)






janela.mainloop()