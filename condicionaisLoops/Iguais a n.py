list_num = []
for i in range(101):
    n = int(input())
    list_num.append(n)
    if i == 100:
        last_num = n

for i in range(len(list_num)):
    if i == 100:
        break
    elif list_num[i] == last_num:
        print(i)