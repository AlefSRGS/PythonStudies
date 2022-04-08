index=0
list=[]
dict={}
txt_pw= input()
txt_pw= txt_pw.title()
txt_pw = txt_pw.replace('a', '@')
txt_pw = txt_pw.replace('E', '%')
txt_pw = txt_pw.replace('e', '!')
txt_pw = txt_pw.replace('i', '@')
txt_pw = txt_pw.replace('o', '#')
txt_pw = txt_pw.replace('u', '$')
txt_pw = txt_pw.replace(' ','')
qnt_pw = int(input())

for i in range(qnt_pw+1):
    num_magi=int(input('numero magico:'))
    while num_magi<=5:
        num_magi=int(input('denovo'))
    password = f'{txt_pw[index:index+5]}{txt_pw[-5:]}{txt_pw[num_magi:num_magi+5]}' 
    for caracter in password:
        list.append(caracter)
    list.reverse()
    password=''.join(list)
    list=[]
    print(password)
    
    decision = input('continuar ?')
    if decision == 's':
        user = input('digite o nome do usuario pra senha')
        dict[user]=password
        index+=1
print(dict)