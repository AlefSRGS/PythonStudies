presents= []
friends = {}
qnt_friends = int(input())
for i in range(qnt_friends):
        x = input().split()
        friend = x[0]
        present1 = x[1]
        present2 = x[2]
        present3 = x[3]
        presents.append(present1)
        presents.append(present2)
        presents.append(present3)
        friends[friend] = presents
        presents = []
while True:
    x = input()
    suggest = x.split()
    if x.upper() == 'FIM':
        break
    friend = suggest[0]
    present = suggest[1]
    if present in friends[friend]:
        print('Uhul! Seu amigo secreto vai adorar')
    else:
        print('Tente Novamente!')
    