peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
IMC = peso/(altura*altura)
if IMC < 18.5:
    print('Você está \033[4;31mABAIXO\033[m do peso!')
elif IMC >= 18.5 and IMC < 25:
    print('Você está no peso \033[4;31mIDEAL!\033[m')
elif IMC >= 25 and IMC < 30:
    print('Você está com \033[4;31mSOBREPESO!\033[m')
elif IMC >= 30 and IMC < 40:
    print('Você está com \033[4;31mOBESIDADE!\033[m')
else:
    print('Você está com \033[4;31mOBESIDADE MÓRBIDA!\033[m')