from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/vinic/PycharmProjects/QRCodes/meuqrcode.png')

result = decode(img)

print(result)