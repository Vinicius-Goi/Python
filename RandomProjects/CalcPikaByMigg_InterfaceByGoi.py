from tkinter import *

def buttonClick(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator=""


main = Tk()
main.title("Calculadora")

operator = ""
input_value = StringVar()
display_text = Entry(main, font=("arial",20,"bold"),textvariable=input_value, bd=30, insertwidth=4,
                            bg="powder blue", justify=RIGHT)
display_text.grid(columnspan=4)

# Row 1 | 7 8 9 +

btn_7 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="7",command=lambda: buttonClick(7))
btn_7.grid(row=1,column=0)

btn_8 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="8",command=lambda: buttonClick(8))
btn_8.grid(row=1,column=1)

btn_9 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="9",command=lambda: buttonClick(9))
btn_9.grid(row=1,column=2)

btn_add = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="+",command=lambda: buttonClick('+'))
btn_add.grid(row=1,column=3)

#Row 2 | 4 5 6 -
btn_4 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="4",command=lambda: buttonClick(4))
btn_4.grid(row=2,column=0)

btn_5 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="5",command=lambda: buttonClick(5))
btn_5.grid(row=2,column=1)

btn_6 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="6",command=lambda: buttonClick(6))
btn_6.grid(row=2,column=2)

btn_minus = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="-",command=lambda: buttonClick('-'))
btn_minus.grid(row=2,column=3)

#Row 3 | 1 2 3 *
btn_1 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="1",command=lambda: buttonClick(1))
btn_1.grid(row=3,column=0)

btn_2 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="2",command=lambda: buttonClick(2))
btn_2.grid(row=3,column=1)

btn_3 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="3",command=lambda: buttonClick(3))
btn_3.grid(row=3,column=2)

btn_mult = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="*",command=lambda: buttonClick('*'))
btn_mult.grid(row=3,column=3)

#Row 4 | 0 C = /
btn_0 = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="0",command=lambda: buttonClick(0))
btn_0.grid(row=4,column=0)

btn_C = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="C",command=lambda: buttonClear())
btn_C.grid(row=4,column=1)

btn_equals = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="=",command=lambda: buttonEqual())
btn_equals.grid(row=4,column=2)

btn_div = Button(main, padx=16,bd=8,fg="black",font=("arial",20,"bold"),text="/",command=lambda: buttonClick('/'))
btn_div.grid(row=4,column=3)

main.mainloop()


'''import math

op = "e"

while True:
    if op == "s" or op == "S":
        print("----------------------------------------")
        print("Tenha um Bom Dia!")
        break

    print("----------------------------------------")
    nome = input("Digite seu Nome: ")

    while True:
        print("----------------------------------------")
        print("Olá {}, Digite".format(nome))
        op = input("""+ para Adição
- para Subtração
* para Multiplicação
/ para Divisão
// para Divisão Inteira
> para Exponenciação
|| para Radiciação
< para Logaritmo
T para Trocar de Sessão
S para Sair
: """)

        if op == "s" or op == "S" or op == "t" or op == "T":
            break

        elif op == "+":
            print("----------------------------------------")
            n1 = input("Digite o primeiro Número à ser Somado: ")
            i = False

            while not i:
                try:
                    n1 = float(n1)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o primeiro Número à ser Somado: ")

            n2 = input("Digite o segundo Número à ser Somado: ")
            i = False

            while not i:
                try:
                    n2 = float(n2)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n2 = input("Digite o segundo Número à ser Somado: ")
            n2 = float(n2)

            nf = n1 + n2
            print("----------------------------------------")
            print("A soma de {} com {} é {}.".format(n1, n2, nf))

        elif op == "-":
            print("----------------------------------------")
            n1 = input("Digite o Número que sofrerá Subtração: ")
            i = False

            while not i:
                try:
                    n1 = float(n1)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o Número que sofrerá Subtração: ")
            n1 = float(n1)

            n2 = input("Digite o Número à ser Subtraído: ")
            i = False

            while not i:
                try:
                    n2 = float(n2)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n2 = input("Digite o Número à ser Subtraído: ")
            n2 = float(n2)

            nf = n1 - n2
            print("----------------------------------------")
            print("A subtração de {} em {} é {}.".format(n2, n1, nf))

        elif op == "*":
            print("----------------------------------------")
            n1 = input("Digite o primeiro Número à ser Multiplicado: ")
            i = False

            while not i:
                try:
                    n1 = float(n1)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o primeiro Número à ser Multiplicado: ")
            n1 = float(n1)

            n2 = input("Digite o segundo Número à ser Multiplicado: ")
            i = False

            while not i:
                try:
                    n2 = float(n2)
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n2 = input("Digite o segundo Número à ser Multiplicado: ")
            n2 = float(n2)

            nf = n1 * n2
            print("----------------------------------------")
            print("A multiplicação de {} com {} é {}.".format(n1, n2, nf))

        elif op == "/":
            print("----------------------------------------")
            n1 = input("Digite o Número que sofrerá Divisão: ")
            i = False

            while not i:
                try:
                    n1 = input(n1)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o Número que sofrerá Divisão: ")
            n1 = float(n1)

            n2 = input("Digite o Número de Divisões: ")
            i = False

            while not i:
                try:
                    n2 = float(n2)
                    if n2 != 0:
                        i = True
                    else:
                        print("----------------------------------------")
                        print("Digite um Valor Válido.")
                        print("----------------------------------------")
                        n2 = input("Digite o Número de Divisões: ")
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n2 = input("Digite o Número de Divisões: ")
            n2 = float(n2)

            nf = n1 / n2
            print("----------------------------------------")
            print("A divisão de {} em {} é {}.".format(n2, n1, nf))

        elif op == "//":
            print("----------------------------------------")
            n1 = input("Digite o Número que sofrerá Divisão: ")
            i = False

            while not i:
                try:
                    n1 = input(n1)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o Número que sofrerá Divisão: ")
            n1 = float(n1)

            n2 = input("Digite o Número de Divisões: ")
            i = False

            while not i:
                try:
                    n2 = float(n2)
                    if n2 != 0:
                        i = True
                    else:
                        print("----------------------------------------")
                        print("Digite um Valor Válido.")
                        print("----------------------------------------")
                        n2 = input("Digite o Número de Divisões: ")
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n2 = input("Digite o Número de Divisões: ")
            n2 = float(n2)

            nf = n1 // n2
            ne = n1 % n2
            print("----------------------------------------")
            print("A divisão inteira de {} em {} é {} com resto {}.".format(n2, n1, nf, ne))

        elif op == ">":
            print("----------------------------------------")
            n1 = input("Digite o Número à ser Elevado: ")
            i = False

            while not i:
                try:
                    n1 = float(n1)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o Número à ser Elevado: ")

            n2 = input("Digite o Número de Elevações: ")
            i = False

            while not i:
                try:
                    n2 = float(n2)
                    i = True
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n2 = input("Digite o Número de Elevações: ")

            nf = math.pow(n1, n2)
            print("----------------------------------------")
            print("{} elevado à {} é {}.".format(n1, n2, nf))

        elif op == "||":
            print("----------------------------------------")
            n1 = input("Digite o Número à ser Radiciado: ")
            i = False

            while not i:
                try:
                    n1 = float(n1)
                    if n1 >= 0:
                        i = True
                    else:
                        print("----------------------------------------")
                        print("Digite um Valor Válido.")
                        print("----------------------------------------")
                        n1 = input("Digite o Número à ser Radiciado: ")
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o Número à ser Radiciado: ")
            n1 = float(n1)

            nf = math.sqrt(n1)
            print("----------------------------------------")
            print("A raiz quadrada de {} é {}.".format(n1, nf))

        elif op == "<":
            print("----------------------------------------")
            n1 = input("Digite o Número à ser Logaritmado: ")
            i = False

            while not i:
                try:
                    n1 = float(n1)
                    if n1 > 1:
                        i = True
                    else:
                        print("----------------------------------------")
                        print("Digite um Valor Válido.")
                        print("----------------------------------------")
                        n1 = input("Digite o Número à ser Logaritmado: ")
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n1 = input("Digite o Número à ser Logaritmado: ")
            n1 = float(n1)

            n2 = input("Digite o Número da Base: ")
            i = False

            while not i:
                try:
                    n2 = float(n2)
                    if n2 >= 0:
                        i = True
                    else:
                        print("----------------------------------------")
                        print("Digite um Valor Válido.")
                        print("----------------------------------------")
                    n2 = input("Digite o Número da Base ")
                except ValueError:
                    print("----------------------------------------")
                    print("Digite um Valor Válido.")
                    print("----------------------------------------")
                    n2 = input("Digite o Número da Base ")
            n2 = float(n2)

            nf = math.log(n1, n2)
            print("----------------------------------------")
            print("O logaritmo de {} na base {} é {}.".format(n1, n2, nf))

        else:
            print("----------------------------------------")
            print("Digite um Valor Válido.")
'''