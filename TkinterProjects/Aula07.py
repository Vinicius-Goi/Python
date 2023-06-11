from tkinter.ttk import * #é importante colocar exatamente nesse ordem
from tkinter import *


#cores
bg_color = "#282a36" #azul meio escuro, sla
text_color1 = "#bd93f9" #roxo
text_color2 = "#6272a4" #azul mais claro
text_color3 = "#d1d1cf" #cinza
title_color1 = "#de6db0" #rosa
title_color2 = "#ffb86c" #laranja
title_color3 = "#4add71" #verde

#janela
janela = Tk()
janela.title('Combobox')
janela.geometry('600x360')
janela.config(bg=bg_color)
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='Python.png'))

#label
label_nome= Label(janela, height=2, text='Nome:', font='OCRAStd 10', anchor=W, bg=bg_color, fg=text_color2)
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=NSEW)

label_idade= Label(janela, height=2, text='Idade:', font='OCRAStd 10', anchor=W, bg=bg_color, fg=text_color2)
label_idade.grid(row=1, column=0, pady=5)

label_pais= Label(janela, height=2, text='País:', font='OCRAStd 10', anchor=W, bg=bg_color, fg=text_color2)
label_pais.grid(row=2, column=0, pady=5)

#função
def obter():
    pass


#entry
entry_nome= Entry(janela, width=25, font='OCRAStd 10', bg=text_color2, fg=bg_color, relief='sunken')
entry_nome.grid(row=0, column=1)

entry_idade= Entry(janela, width=5, font='OCRAStd 10', bg=text_color2, fg=bg_color, relief='sunken')
entry_idade.grid(row=1, column=1, sticky=W)

#combobox
combo_pais = Combobox(janela)

#definindo os valores para o combobox
combo_pais['value'] = ('Afeganistão',
'África do Sul',
'Akrotiri',
'Albânia',
'Alemanha',
'Andorra',
'Angola',
'Anguila',
'Antárctida',
'Antígua e Barbuda',
'Arábia Saudita',
'Arctic Ocean',
'Argélia',
'Argentina',
'Arménia',
'Aruba',
'Ashmore and Cartier Islands',
'Atlantic Ocean',
'Austrália',
'Áustria',
'Azerbaijão',
'Baamas',
'Bangladeche',
'Barbados',
'Barém',
'Bélgica',
'Belize',
'Benim',
'Bermudas',
'Bielorrússia',
'Birmânia',
'Bolívia',
'Bósnia e Herzegovina',
'Botsuana',
'Brasil',
'Brunei',
'Bulgária',
'Burquina Faso',
'Burúndi',
'Butão',
'Cabo Verde',
'Camarões',
'Camboja',
'Canadá',
'Catar',
'Cazaquistão',
'Chade',
'Chile',
'China',
'Chipre',
'Clipperton Island',
'Colômbia',
'Comores',
'Congo-Brazzaville',
'Congo-Kinshasa',
'Coral Sea Islands',
'Coreia do Norte',
'Coreia do Sul',
'Costa do Marfim',
'Costa Rica',
'Croácia',
'Cuba',
'Curacao',
'Dhekelia',
'Dinamarca',
'Domínica',
'Egipto',
'Emiratos Árabes Unidos',
'Equador',
'Eritreia',
'Eslováquia',
'Eslovénia',
'Espanha',
'Estados Unidos',
'Estónia',
'Etiópia',
'Faroé',
'Fiji',
'Filipinas',
'Finlândia',
'França',
'Gabão',
'Gâmbia',
'Gana',
'Gaza Strip',
'Geórgia',
'Geórgia do Sul e Sandwich do Sul',
'Gibraltar',
'Granada',
'Grécia',
'Gronelândia',
'Guame',
'Guatemala',
'Guernsey',
'Guiana',
'Guiné',
'Guiné Equatorial',
'Guiné-Bissau',
'Haiti',
'Honduras',
'Hong Kong',
'Hungria',
'Iémen',
'Ilha Bouvet',
'Ilha do Natal',
'Ilha Norfolk',
'Ilhas Caimão',
'Ilhas Cook',
'Ilhas dos Cocos',
'Ilhas Falkland',
'Ilhas Heard e McDonald',
'Ilhas Marshall',
'Ilhas Salomão',
'Ilhas Turcas e Caicos',
'Ilhas Virgens Americanas',
'Ilhas Virgens Britânicas',
'Índia',
'Indian Ocean',
'Indonésia',
'Irão',
'Iraque',
'Irlanda',
'Islândia',
'Israel',
'Itália',
'Jamaica',
'Jan Mayen',
'Japão',
'Jersey',
'Jibuti',
'Jordânia',
'Kosovo',
'Kuwait',
'Laos',
'Lesoto',
'Letónia',
'Líbano',
'Libéria',
'Líbia',
'Listenstaine',
'Lituânia',
'Luxemburgo',
'Macau',
'Macedónia',
'Madagáscar',
'Malásia',
'Malávi',
'Maldivas',
'Mali',
'Malta',
'Man, Isle of',
'Marianas do Norte',
'Marrocos',
'Maurícia',
'Mauritânia',
'México',
'Micronésia',
'Moçambique',
'Moldávia',
'Mónaco',
'Mongólia',
'Monserrate',
'Montenegro',
'Mundo',
'Namíbia',
'Nauru',
'Navassa Island',
'Nepal',
'Nicarágua',
'Níger',
'Nigéria',
'Niue',
'Noruega',
'Nova Caledónia',
'Nova Zelândia',
'Omã',
'Pacific Ocean',
'Países Baixos',
'Palau',
'Panamá',
'Papua-Nova Guiné',
'Paquistão',
'Paracel Islands',
'Paraguai',
'Peru',
'Pitcairn',
'Polinésia Francesa',
'Polónia',
'Porto Rico',
'Portugal',
'Quénia',
'Quirguizistão',
'Quiribáti',
'Reino Unido',
'República Centro-Africana',
'República Dominicana',
'Roménia',
'Ruanda',
'Rússia',
'Salvador',
'Samoa',
'Samoa Americana',
'Santa Helena',
'Santa Lúcia',
'São Bartolomeu',
'São Cristóvão e Neves',
'São Marinho',
'São Martinho',
'São Pedro e Miquelon',
'São Tomé e Príncipe',
'São Vicente e Granadinas',
'Sara Ocidental',
'Seicheles',
'Senegal',
'Serra Leoa',
'Sérvia',
'Singapura',
'Sint Maarten',
'Síria',
'Somália',
'Southern Ocean',
'Spratly Islands',
'Sri Lanca',
'Suazilândia',
'Sudão',
'Sudão do Sul',
'Suécia',
'Suíça',
'Suriname',
'Svalbard e Jan Mayen',
'Tailândia',
'Taiwan',
'Tajiquistão',
'Tanzânia',
'Território Britânico do Oceano Índico',
'Territórios Austrais Franceses',
'Timor Leste',
'Togo',
'Tokelau',
'Tonga',
'Trindade e Tobago',
'Tunísia',
'Turquemenistão',
'Turquia',
'Tuvalu',
'Ucrânia',
'Uganda',
'União Europeia',
'Uruguai',
'Usbequistão',
'Vanuatu',
'Vaticano',
'Venezuela',
'Vietname',
'Wake Island',
'Wallis e Futuna',
'West Bank',
'Zâmbia',
'Zimbabué')#lista de países
combo_pais.current(0)#aqui ele vai passar o indice dos valores, para aparecer ao iniciar o programa

combo_pais.grid(row=2, column=1, sticky=W)

#botao
botao_registro= Button(janela,height=2, text='Registrar',bg=text_color2, fg=bg_color, font='OCRAStd 10 bold', command=obter)
botao_registro.place(x=245, y=150)



janela.mainloop()