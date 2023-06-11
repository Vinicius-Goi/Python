l = float(input('Digite a largura em metros:'))
a = float(input('Digite a altura em metros:'))
at = l*a
t = at/2
print('Sua parede tem a dimensão de {}x{}\nA área dessa parede é de {:.3f}m²\nSerão necessários {:.3f}L de tinta para pinta-la'.format(l, a, at, t))