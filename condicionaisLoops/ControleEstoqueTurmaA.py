entrada = input()
estoque = dict()
while entrada != '9999':
    values = entrada.split()
    codigo = int(values[0])
    quantidade = int(values[1])
    estoque[codigo] = quantidade
    entrada = input()

# Processar os pedidos
entrada = input()
while entrada != '9999':
    values = entrada.split()
    codigo = int(values[1])
    quantidade = int(values[2])
    disponivel = estoque.get(codigo, 0)
    if quantidade <= disponivel:
        print("OK")
        estoque[codigo] = disponivel - quantidade
    else:
        print("ESTOQUE INSUFICIENTE")
    entrada = input()

for codigo,disponivel in estoque.items():
    print(codigo, disponivel)