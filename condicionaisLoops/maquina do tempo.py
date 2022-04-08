x = input().split(' ')
A = int(x[0])
B = int(x[1])
C = int(x[2])

if A == B or A == C or B == C:
    print('S')
elif A == B + C or B == A + C or C == B + A:
    print('S')
else:
    print('N')