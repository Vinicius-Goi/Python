def maior(*num):
    print('-='*30)
    print('Analisando os valores passados...')
    for c in num:
        print(c, end=' ')
        mai = c
        if c > mai:
            mai = c
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {c}.')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()