itens = {1 : 'Cachorro Quente', 2: 'X-Tudo', 3: 'Batata frita', 4: 'Refrigerante', 5: 'Pipoca' }
value = 0
while True:
    item = int(input())
    if item == 0:
        print('Código inválido')
        break
    qnt = int(input())
    print(f'Você escolheu {itens[item]}')
    if item == 1:
        value = qnt * 2.5
    elif item == 2:
        value = qnt * 4.75
    elif item == 3:
        value = qnt * 3.25
    elif item == 4:
        value = qnt * 2.8
    elif item == 5:
        value = qnt * 0.9
    print(f'Sua conta é de R${value}')