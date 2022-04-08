numero_noms = int(input())
notas = list()
pesos = list()

for i in range(numero_noms):
    nota = float(input())
    notas.append(nota)

for i in range(numero_noms):
    peso = float(input())
    pesos.append(peso)

notas_vezes_pesos = list()
for i in range(numero_noms):
    notas_vezes_pesos.append(notas[i] * pesos[i])

media_ponderada = sum(notas_vezes_pesos) / sum(pesos)
print(f'{media_ponderada:.2f}')
