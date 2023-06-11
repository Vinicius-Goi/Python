from tkinter import *

#cores
bg_color = "#282a36" #azul meio escuro, sla
text_color1 = "#bd93f9" #roxo
text_color2 = "#6272a4" #azul mais claro
text_color3 = "#d1d1cf" #cinza
title_color1 = "#de6db0" #rosa
title_color2 = "#ffb86c" #laranja
title_color3 = "#4add71" #verde

janela = Tk()
janela.title('Botões')

janela.geometry('550x550')
janela.iconphoto(False, PhotoImage(file='Python.png'))

janela.config(bg=bg_color)
janela.resizable(width=False, height=False)

contador = 0

def executar():

    global contador


    texto_I = 'Numero Impar: '
    texto_P = 'Numero Par: '

    if contador % 2 == 0:
        resultado = texto_P + str(contador)
        label1['text'] = resultado
        label1['fg'] = text_color1
    else:
        resultado = texto_I + str(contador)
        label1['text'] = resultado
        label1['fg'] = title_color1

    contador += 1


label1 = Label(janela, height=1, text='Oi, eu sou um label :)', font="OCRAStd 10", fg=title_color3, bg=bg_color, relief='flat')
label1.place(x=290, y=10)


#criando um botão
botao_padrao_raised = Button(janela,height=1, text='Clique aqui (Padrão/Raised)', font="OCRAStd 10", fg=text_color2, bg=bg_color, command=executar)#command= será o q puxara e executara as funções q deseja
botao_padrao_raised.place(x=10, y=10)

botao_flat = Button(janela, width=20, height=1, text='Clique aqui (Flat)', font="OCRAStd 10", fg=text_color2, bg=bg_color, relief='flat')#relief, é o relevo que pode ser usado tbm no label
botao_flat.place(x=10, y=50)

botao_sunken = Button(janela, width= 20, height=1, text='Clique aqui (Sunken)', font="OCRAStd 10", fg=text_color2, bg=bg_color, relief='sunken')
botao_sunken.place(x=10, y=90)

botao_groove = Button(janela, height=1, text='Clique aqui (Groove)', font='OCRAStd 10', fg=text_color2, bg=bg_color, relief='groove')
botao_groove.place(x=10, y=130)

botao_ridge = Button(janela, height=1, text='Clique aqui (Ridge)', font='OCRAStd 10', fg=text_color2, bg=bg_color, relief='ridge')
botao_ridge.place(x=10, y=170)

botao_solid = Button(janela, height=1, text='Clique aqui (Solid)', font='OCRAStd 10', fg=text_color2, bg=bg_color, relief='solid')
botao_solid.place(x=10, y=170)



janela.mainloop()