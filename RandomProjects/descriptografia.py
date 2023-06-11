from cryptography.fernet import Fernet

arq = input('Digite o arquivo e a sua extensão para \033[1mDESCRIPTOGRAFAR\033[m o arquivo: ')

with open('chave.key', 'rb') as filekey:
    chave = filekey.read()

fernet = Fernet(chave)

with open(arq, 'rb') as aquivo_criptografado:
    criptografado = aquivo_criptografado.read()

descriptografado = fernet.decrypt(criptografado)

with open(arq, 'wb') as aquivo_descriptografado:
    aquivo_descriptografado.write(descriptografado)