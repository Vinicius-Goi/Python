from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#importando pillow

from PIL import ImageTk, Image


#importando strings

import string
import random


#cores
bg_color = "#282a36" #azul meio escuro, sla
text_color1 = "#bd93f9" #roxo
text_color2 = "#6272a4" #azul mais claro
text_color3 = "#d1d1cf" #cinza
title_color1 = "#de6db0" #rosa
title_color2 = "#ffb86c" #laranja
title_color3 = "#4add71" #verde
bg_color2 = "#1b1d28" #azul escuro

#janela
janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.iconphoto(False, PhotoImage(file='Python.png'))
janela.configure(bg=bg_color2)
janela.resizable(width=False, height=False)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#frames - dividindo a tela em dois frames
frame_cima = Frame(janela, width=295, height=50, bg=bg_color2, padx= 0, pady= 0, relief='flat')
frame_cima.grid(row= 0, column= 0, sticky= NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=bg_color2, padx= 0, pady= 0, relief='flat')
frame_baixo.grid(row= 1, column= 0, sticky= NSEW)

#trabalhando no frame cima
img = Image.open('GeradorDeSenha.png')
img = img.resize((35, 35), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, height=60, image=img, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=bg_color2)
app_logo.place(x= 2, y= 0)

app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, font='OCRAStd 15', height=1, padx=0, relief='flat', anchor='nw', fg=text_color3, bg=bg_color2)
app_nome.place(x= 40, y= 15)

app_linha = Label(frame_cima, text='', width=295, font='OCRAStd 1', height=1, padx=0, relief='flat', anchor='nw', fg=text_color3, bg=text_color2)
app_linha.place(x= 0, y= 45)


#função gerar senha
def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '1234567890'
    simbolos = '[]{}()*;/,_-!"#$%&+.:<=>?@\^_`|~'

    global combinar
    combinar = ''
    #condições
    if estado_1.get() == alfabeto_maior:
        combinar = combinar + alfabeto_maior
    else:
        pass


    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
        pass


    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass


    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))

    app_senha['text'] = senha

    def copiar_senha():
        info = senha
        frame_baixo.clipboard_clear()
        frame_baixo.clipboard_append(info)

        messagebox.showinfo("Sucesso!", "Copiado!")

    botao_copiar_senha = Button(frame_baixo,command=copiar_senha, text='Copiar', font='OCRAStd 10', width=7, height=2, relief='raised',
                                overrelief='solid', anchor='center', fg=title_color3, bg=bg_color2,
                                activebackground=bg_color, activeforeground=text_color3)
    botao_copiar_senha.grid(row=0, column=1, sticky=NW, padx=5, pady=10, columnspan=1)















#trabalhando no frame baixo
app_senha = Label(frame_baixo, text='- - -', width=22, font='OCRAStd 10', height=2, padx=0, relief='solid', anchor='center', fg=title_color3, bg=bg_color2)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx= 5, pady= 10)

app_info = Label(frame_baixo, text='Número total de caracteres na senha:', font='OCRAStd 7', height=1, padx=0, relief='flat', anchor='nw', fg=text_color2, bg=bg_color2)
app_info.grid(row=1, column=0, columnspan=2, sticky=NSEW, padx= 5, pady= 1)

#spinbox
var = IntVar()
var.set(8) #valor inicial para a spin box
spin = Spinbox(frame_baixo, from_=0 , to=20, width=5, textvariable=var, bg=bg_color, fg=text_color3, insertbackground=text_color3)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, pady=8, padx=5)



#variavies
alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '1234567890'
simbolos = '[]{}()*;/,_-!"#$%&+.:<=>?@\^_`|~'



frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=bg_color2, padx= 0, pady= 0, relief='flat')
frame_caracteres.grid(row= 3, column= 0, sticky= NSEW, columnspan= 3)


#letras maiusculas
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width= 1, var=estado_1, onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=bg_color2, activebackground=bg_color)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caracteres, text='ABC Letras maiusculas', font='OCRAStd 8', relief='flat', anchor='nw', fg=title_color1, bg=bg_color2)
app_info.place(x= 30, y= 10)


#letras minusculas
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width= 1, var=estado_2, onvalue=alfabeto_menor, offvalue='off', relief='flat', bg=bg_color2, activebackground=bg_color)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caracteres, text='abc Letras minusculas', font='OCRAStd 8', relief='flat', anchor='nw', fg=title_color1, bg=bg_color2)
app_info.place(x= 30, y= 45)


#numeros
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width= 1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=bg_color2,activebackground=bg_color)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caracteres, text='123 Números', font='OCRAStd 8', relief='flat', anchor='nw', fg=title_color1, bg=bg_color2)
app_info.place(x= 30, y= 80)


#simbolos
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width= 1, var=estado_4, onvalue=simbolos, offvalue='off', relief='flat', bg=bg_color2, activebackground=bg_color)
check_4.grid(row=3, column=0, sticky=NW, padx=2, pady=5)

app_info = Label(frame_caracteres, text='!@# Simbolos', font='OCRAStd 8', relief='flat', anchor='nw', fg=title_color1, bg=bg_color2)
app_info.place(x= 30, y= 115)


#botao
botao_gerar_senha = Button(frame_caracteres, command= criar_senha, text='Gerar Senha', font='OCRAStd 10', width= 30, relief='flat',overrelief='solid', anchor='center', fg=text_color1, bg=text_color2, activebackground=bg_color, activeforeground=text_color3)
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW, padx=7, pady=20, columnspan=5)














janela.mainloop()

