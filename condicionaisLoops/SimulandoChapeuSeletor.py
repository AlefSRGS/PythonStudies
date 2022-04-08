GRIFINORIA = 'Grifinoria'
SONSERINA = 'Sonserina'
CORVINAL = 'Corvinal'
LUFA_LUFA = 'Lufa-lufa'

caracteristicas_casa = dict()
caracteristicas_casa['coragem'] = GRIFINORIA
caracteristicas_casa['determinacao'] = GRIFINORIA
caracteristicas_casa['astucia'] = SONSERINA
caracteristicas_casa['ambicao'] = SONSERINA
caracteristicas_casa['inteligencia'] = CORVINAL
caracteristicas_casa['forca de vontade'] = CORVINAL
caracteristicas_casa['lealdade'] = LUFA_LUFA
caracteristicas_casa['companheirismo'] = LUFA_LUFA

numero_alunos = int(input())
casas_alunos = dict()

for i in range(numero_alunos):
    linha = input()
    indice_primeiro_espaco = linha.index(' ')
    nome = linha[0:indice_primeiro_espaco]
    caracteristica = linha[indice_primeiro_espaco+1:].lower()
    casa = caracteristicas_casa.get(caracteristica, None)
    if casa is not None:
        alunos = casas_alunos.get(casa, list())
        alunos.append(nome)
        casas_alunos[casa] = alunos


for casa in [GRIFINORIA, SONSERINA, CORVINAL, LUFA_LUFA]:
    print(f'{casa}:')
    for aluno in casas_alunos.get(casa, list()):
        print(aluno)
