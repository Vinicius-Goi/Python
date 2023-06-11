from tkinter import *

#cores
bg_color = "#282a36" #azul meio escuro, sla
text_color1 = "#bd93f9" #roxo
text_color2 = "#6272a4" #azul mais claro
text_color3 = "#d1d1cf" #cinza
title_color1 = "#de6db0" #rosa
title_color2 = "#ffb86c" #laranja
title_color3 = "#4add71" #verde

#criação de janela
janela = Tk()
janela.title('Entry')
janela.config(bg=bg_color)
janela.geometry('550x550')
#janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='Python.png'))

#Função obter

def obter():
    nome = entry_nome.get()#isso serve para obter os dados vindos do entry()
    idade = entry_idade.get()
    pais = entry_pais.get()

    #colocando as informações vindas do entry para o texto ao lado
    label_nome_result['text'] = nome
    label_idade_result['text'] = idade
    label_pais_result['text'] = pais

    #apagando os dados dentro das entry
    entry_nome.delete(0,END) #passando os parametros, ou seja, do inicio (0) até o END (fim)
    entry_idade.delete(0,END)
    entry_pais.delete(0,END)


#criação de label nome
label_nome = Label(janela, height=1, text='Nome:', font='OCRAStd 10', bg=bg_color, fg=text_color2, anchor='w')#anchor serve para ajeitar o texto DENTRO DO LABEL, mas usa tbm as mesmas direções do sticky, porem n se pode usar o NSEW como no sticky
label_nome.grid(row=0, column=0, padx= 10, pady= 10, sticky=NSEW)#sticky serve para ajeitar o label DENTRO DA JANELA, N (norte), S (sul), W (Oeste), E(Leste) e combinações


#criação de label idade
label_idade = Label(janela, height=1, text='Idade:', font='OCRAStd 10', bg=bg_color, fg=text_color2, anchor='w')
label_idade.grid(row=1, column=0, padx= 10, pady= 10, sticky=NSEW)

#criação de label pais
label_pais= Label(janela, height=1, text='País:', font='OCRAStd 10', bg=bg_color, fg=text_color2, anchor='w')
label_pais.grid(row=2, column=0, padx= 10, pady= 10, sticky=NSEW)


#Na entry não é possivel alterar a altura, usamos a fonte para o python definir automaticamente a altura
#criação de caixa de entrada (entry) - entry_nome
entry_nome = Entry(janela, width=20, font='OCRAStd 10 bold', fg=bg_color, bg=text_color2, relief='sunken')
entry_nome.grid(row=0, column=1, pady= 10, sticky=W)

#criação de caixa de entrada (entry) - entry_idade
entry_idade = Entry(janela, width=20, font='OCRAStd 10 bold', fg=bg_color, bg=text_color2, relief='sunken')
entry_idade.grid(row=1, column=1,pady= 10, sticky=W)

#criação de caixa de entrada (entry) - entry_pais
entry_pais = Entry(janela, width=20, font='OCRAStd 10 bold', fg=bg_color, bg=text_color2, relief='sunken')
entry_pais.grid(row=2, column=1,pady= 10, sticky=W, state=DISABLED) #state= serve para desabilitar o entry


#resposta processando os dados dos entry
label_nome_result = Label(janela, height=1,text='Vinicius Goi', font='OCRAStd 10', fg= text_color2, bg=bg_color, relief='flat')
label_nome_result.grid(row=0, column=3, sticky=W)
label_idade_result = Label(janela, height=1,text='16', font='OCRAStd 10', fg=text_color2, bg=bg_color, relief='flat')
label_idade_result.grid(row=1, column=3, sticky=W)
label_pais_result = Label(janela, height=1,text='Brasil', font='OCRAStd 10', fg=text_color2, bg=bg_color, relief='flat')
label_pais_result.grid(row=2, column=3, sticky=W)


#criando um botão
botao = Button(janela, height=1, text="Clique aqui para enviar!", font='OCRAStd 10', bg=bg_color, fg=text_color2, relief='raised', command=obter)
botao.place(x=150, y=150)


janela.mainloop()