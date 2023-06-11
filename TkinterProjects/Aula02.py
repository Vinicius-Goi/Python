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
janela.title("Label")

janela.geometry('350x300')

janela.config(bg= bg_color)

janela.iconphoto(False, PhotoImage(file='Python.png'))

janela.resizable(width=False, height=False)

#criando um label
label = Label(janela,width=10, height =2, text="Olá!", font=("OCRAStd 12"), bg= bg_color, fg=text_color3)#definindo em que janela ele vai ficar, a largura e altura e o texto
#label.place(x=10, y=10) - definindo a pos x e a pos y - place tbm pode ser outra forma de posicionar na tela o label
label.grid(row=0, column=0) #outra forma para apresentar o label

#pady vai criar um espaço entre os labels, a mesma coisa iria acontecer com o padx só q seria para a horizontal
label_nome = Label(janela, width=10, height=2, text="Nome: ", font=("OCRAStd 12"), bg= bg_color, fg=text_color3) #para colocar a cor na fonte precisara chamar o fg e para o fundo é só usar o bg novamente
label_nome.grid(row=1, column=1, pady=5) #usando outros valores para n sobrepor o outro label

label_idade = Label(janela, width=10, height=2, text="Idade: ", font=("OCRAStd 12"), bg= bg_color, fg=text_color3)
label_idade.grid(row=2,column=0)

label_pais = Label(janela,width=10,height=2,text="País: ", font=("OCRAStd 12"),bg= bg_color, fg=text_color3)
label_pais.grid(row=3, column=0)



janela.mainloop()