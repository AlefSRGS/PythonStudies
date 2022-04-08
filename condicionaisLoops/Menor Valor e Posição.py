num_element = int(input())
n_values = input().split()

list_num =[]

for i in n_values:
    i = int(i)
    list_num.append(i)

num_min = min(list_num)

min_position = list_num.index(num_min)

print(f"Menor valor: {num_min}")
print(f"Posicao: {min_position}")