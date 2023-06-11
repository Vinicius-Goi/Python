from tkinter import  *

#cores
bg_color = "#282a36" #azul meio escuro, sla
text_color1 = "#bd93f9" #roxo
text_color2 = "#6272a4" #azul mais claro
text_color3 = "#d1d1cf" #cinza
title_color1 = "#de6db0" #rosa
title_color2 = "#ffb86c" #laranja
title_color3 = "#4add71" #verde

janela = Tk()
janela.title("Gerentes de geometria: place()/pack()/grid()")

janela.geometry('550x550')

janela.iconphoto(False, PhotoImage(file='Python.png'))

janela.config(bg=bg_color)
janela.resizable(width=False, height=False)

#eles usam 3 tipos de geometrias: place, pack e grid (geometria seria a forma q vamos movimentar o label, buttons etc)
#o place() usa coordenadas absolutas em pixels
#o pack() coloca os widgets em um dos quadros lados. Novos widgets são colocados ao lado de widgets existentes.
#o grid() coloca os widgets em uma grade semelhante a uma planilha de redimensionamento dinâmico.

label_1 = Label (janela, width=20, text='Nome:', font='OCRAStd 12', bg=text_color2, fg=text_color3)
#label_1.place(x=10, y=10)
#label_1.pack(side=LEFT)#o pack ele cria as janelas no meio da janela do aplicativo
label_1.grid(row=0,column=0,pady=10)

nome = Label (janela, width=20, text='Vinícius', font='OCRAStd 12', bg=text_color2, fg=text_color3)
#nome.place(x=165, y=10)
#nome.pack(side=LEFT)#da para determinar o comportamento usando o side=
nome.grid(row=0,column=1, pady= 10, padx=5)

label_2 = Label (janela, width=20, text='Idade:', font='OCRAStd 12', bg=text_color2, fg=text_color3)
#label_2.place(x=10, y=50)
#label_2.pack()#o pack n é mt usado por conta da sua dificuldade de colocar as coisas no lugar
label_2.grid(row=1,column=0,pady=15, padx=5)

idade = Label (janela, width=20, text='16', font='OCRAStd 12', bg=text_color2, fg=text_color3)
#idade.place(x=165, y=50)
#idade.pack()
idade.grid(row=1,column=1,pady=10, padx=5)

label_3 = Label (janela, width=20, text='País:', font='OCRAStd 12', bg=text_color2, fg=text_color3)
#label_3.place(x=10, y=90)
#label_3.pack()
label_3.grid(row=2,column=0,pady=15, padx=5)

pais = Label (janela, width=20, text='Brasil', font='OCRAStd 12', bg=text_color2, fg=text_color3)
#pais.place(x=165, y=90)
#pais.pack()
pais.grid(row=2,column=1,pady=10, padx=5)




janela.mainloop()