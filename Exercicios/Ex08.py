v = float(input('Digite o valor em metros:'))
km = v/1000
hm = v/100
dam = v/10
dm = v*10
cm = v*100
mm = v*1000
print('O valor digitado em: \n{} Km\n{} Hm\n{} Dam\n{} Dm\n{} Cm\n{} Mm'.format(km, hm, dam, dm, cm, mm))