after = ''
before = ''
text1 = input('ensira o texto: ').split(".")
command = input('O que você quer fazer com o texto( c - escrever; r - ler; u - modificar; d - deletar): ')

while True:
    if command == 'c':
        text2 = input('digite o texto a ser adicionado: ')
        text1.append(text2)
        print(text1)
        command = input('O que você quer fazer com o texto( c - escrever; r - ler; u - modificar; d - deletar): ')
    elif command == 'r':
        print(text1)
        command = input('O que você quer fazer com o texto( c - escrever; r - ler; u - modificar; d - deletar): ')
    elif command == 'u':
        index = int(input('informe o index da frase a ser modificada: '))
        word_mod1 = input('palavra que sera modificada: ')
        word_mod2 = input('palavra que vai substituir: ')
        phrase = text1[index]
        before = text1[:phrase]
        after = text1[phrase:]
        before = ".".join(before)
        after = ".".join(after)
        phrase = phrase.replace(word_mod1, word_mod2)
        text1 = f"{before}, {phrase}, {after}"
        if not before:
            text1 = f"{before}, {after}"
        elif not after:
            text1 = phrase
        if not after:
            text1 = f"{before}, {phrase}"
        print(text1)
        command = input('O que você quer fazer com o texto( c - escrever; r - ler; u - modificar; d - deletar): ')
    elif command == 'd':
        index = int(input('informe o index da frase a ser removida: '))
        phrase = text1[index]
        text1.remove(phrase)
        print(text1)
        command = input('O que você quer fazer com o texto( c - escrever; r - ler; u - modificar; d - deletar): ')