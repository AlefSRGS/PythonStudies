qnt_pessoas = 0
qnt_contas = 0
pessoas = {}
contas = {}

qnt_pessoas = int(input('quantidade pessoas serao cadastradas: '))
for i in range(qnt_contas):
    nome = input('nome da pessoa a ser cadastrada: ')
    renda = int(input('renda da pessoa: '))
    pessoas[nome] = renda

qnt_contas = int(input('quantidade de contas que seram cadastradas'))
for i in range(qnt_contas):
    nome_conta = input('Nome da conta:')
    valor_conta = input('valor da conta: ')
    contas[nome_conta] = valor_conta

valor_pessoas = str
for i in pessoas.values():
    valor_pessoas = i + valor_pessoas

valor_contas = int
for i in contas.values():
    valor_contas = i + valor_contas

if valor_conta > valor_pessoas:
    print('a familia deve fazer corte de gastos')

else:
    for pessoa in pessoas.keys():
        porcentagem = pessoas(pessoa)/valor_pessoas
        valor_pagar = porcentagem * valor_conta
        print(f'{pessoa} tem {porcentagem:.1f} da renda e deve pegar {valor_pagar:.2f}')