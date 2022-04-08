def juizoFinal(result):
    if result >= 7:
        print('Parabens o aluno está aprovado')
    elif result < 7 and result > 3:
        print('O aluno tera que fazer a prova final')
    elif result < 3:
        print('Aluno foi reprovado')
while True:
    NotaP1 = float(input('Digite a nota da primeira prova: '))
    if NotaP1 < 0 or NotaP1 > 10:
        print('Por favor digite uma entrada valida')
        break
    NotaListaM1 = float(input('Digite a nota da primeira lista: '))
    if NotaListaM1 < 0 or NotaListaM1 > 10:
        print('Por favor digite uma entrada valida')
        break
    PesoM1 = float(input('Digite a nota do peso 1: '))
    if PesoM1 < 0 or PesoM1 > 10:
        print('Por favor digite uma entrada valida')
        break
    NotaP2 = float(input('Digite a nota da segunda prova: '))
    if NotaP2 < 0 or NotaP2 > 10:
        print('Por favor digite uma entrada valida')
        break
    NotaListaM2 = int(input('Digite a nota da lista 2: '))
    if NotaListaM2 < 0 or NotaListaM2 > 10:
        print('Por favor digite uma entrada valida')
        break
    PesoM2 = float(input('Digite a nota do peso 2: '))
    if PesoM2 < 0 or PesoM2 > 10:
        print('Por favor digite uma entrada valida')
        break

    first_nota = (NotaP1 + NotaListaM1) / PesoM1
    second_nota = (NotaP2 + NotaListaM2) / PesoM2
    result = (first_nota + second_nota) /  2

    juizoFinal(result)