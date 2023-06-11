from datetime import date
a = int(input('Em que ano você nasceu? '))
calc = date.today().year - a
if calc < 18:
    calc = 18 - calc
    print('Você ainda vai se alistar no exército, faltam {} anos.'.format(calc))
elif calc == 18:
    print('Já está na hora de se alistar no exército.')
else:
    calc = calc - 18
    print('Já passou da hora de você se alistar no exército, já se passaram {} anos.'.format(calc))