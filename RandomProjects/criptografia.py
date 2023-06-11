from cryptography.fernet import Fernet

arq = input('Digite o arquivo e a sua extensão para \033[1mCRIPTOGRAFAR\033[m o arquivo: ')

with open('chave.key', 'rb') as filekey:
    chave = filekey.read()

fernet = Fernet(chave)

with open(arq, 'rb') as arquivo:
    conteudo_arquivo = arquivo.read()

criptografado = fernet.encrypt(conteudo_arquivo)

with open(arq, 'wb') as arquivo_criptografado:
    arquivo_criptografado.write(criptografado)