list_fml = []
regis_fml = {}
regis_conta = {}
qnt_people = int(input('quantas pessoas vivem na casa: '))
if qnt_people == 0 or qnt_people == str:
    print('Por favor use um numero de pessoas valido')
    qnt_people = int(input('quantas pessoas vivem na casa: '))

for i in range(qnt_people):
    name = input('')
    income = input('')
    regis_fml['name'] = name
    regis_fml['income'] = income
    list_fml.append(regis_fml)

qnt_contas = int(input('quantas contas vão ser pagas: '))
if qnt_contas == 0 or qnt_contas == str:
    print('Por favor use um numero de contas valido')
    qnt_contas = int(input('quantas contas vão ser pagas: '))

for i in range(qnt_contas):
    name_conta = input('')
    value_conta = input('')
    

    
