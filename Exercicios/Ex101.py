from datetime import datetime
def voto(a):
    if sub == 16 or sub == 17 or sub > 70:
        return f"Com {sub} anos: VOTO OPCIONAL"
    if sub >= 18 or sub <= 70:
        return f"Com {sub} anos: VOTO OBRIGATÓRIO"
    if sub < 16:
        return f"Com {sub} anos: VOTO NEGADO"


print('-'*30)

ano = int(input("Em que ano você nasceu? "))
sub = datetime.today().year - ano
print(voto(ano))