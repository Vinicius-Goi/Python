#estamos importando tudo q tenha a ver com o tkinter para o app usando o *
from tkinter import *

#cores
bg_color = "#282a36" #azul meio escuro, sla
text_color1 = "#bd93f9" #roxo
text_color2 = "#6272a4" #azul mais claro
text_color3 = "#d1d1cf" #cinza
title_color1 = "#de6db0" #rosa
title_color2 = "#ffb86c" #laranja
title_color3 = "#4add71" #verde


#criando uma instância da janela do tkinter
janela = Tk()
janela.title("Olá Mundo!")#definindo um titulo para a janela

#configurando o tamanho da janela
janela.geometry('300x250')#primeiro valor é a largura e o segundo é a altura

#alterar a cor de fundo da janela
janela.config(bg= bg_color)#bg chama a função para definir o background
#vc pode definir a cor do bg tanto usando o nome por exemplo "red", quanto o codigo em hexadecimal nesse caso o "#282a36" ou usando uma variavel

#alterando o icone da janela
janela.iconphoto(False, PhotoImage(file='Python.png'))
#usamos o false para dasativar o icone q já está na janela de padrão e usamos o PhotoImage para definirmos a proxima imagem

#tornar a janela NÃO redimensionavel
janela.resizable(width=False, height=False) #desabilitando a função de escalonar a janela


janela.mainloop()