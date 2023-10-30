from playsound import playsound

user = input('Usuário: ') == "Goi"
senha = input("Senha: ") == "senha"

while user != "Goi" and senha != "senha":
    playsound("acesso negado")
    input()

else:
    playsound("acesso liberado")
    input("")