import qrcode

data = input('Digite o que você quer transformar em um QRCode: ')

img = qrcode.make(data)

img.save('C:/Users/vinic/PycharmProjects/QRCodes/meuqrcode.png')