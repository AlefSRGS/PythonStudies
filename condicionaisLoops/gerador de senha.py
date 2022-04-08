i =0
list = []
decision = 's'
while decision == 's':
    txt_pw= input('Ensira a frase que ira gerar a senha: ')
    if len(txt_pw) >= 200:
        txt_pw= txt_pw.title()
        txt_pw = txt_pw.replace('a', '@')
        txt_pw = txt_pw.replace('A', '@')
        txt_pw = txt_pw.replace('I', '!')
        txt_pw = txt_pw.replace('i', '1')
        txt_pw = txt_pw.replace("\n",'')
        txt_pw = txt_pw.replace('.',"I'mGroot")
        txt_pw = txt_pw.replace(',',"I'mGroot")
        txt_pw = txt_pw.replace(';',"I'mGroot")
        txt_pw = txt_pw.replace(':',"I'mGroot")
        num_info=int(input('numero magico:'))
        if num_info > 0:
            password = f'{txt_pw[i:i+4]}{txt_pw[-4:]}{txt_pw[num_info:num_info+4]}' 
            for caracter in password:
                list.append(caracter)
            list.reverse()
            password=''.join(list)
            list=[]
            print(password)
        else:
            num_info=int(input('Por favor digite um numero magico valido:'))
    else:
        print('por favor ensira uma frase com 200 caracteres ou mais.')
    decision = input('se deseja continuar a criar senhas com essa frase digite "s"')