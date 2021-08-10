"""
Jogo da forca
Chances : 3

"""

palavra_secreta = 'asa'
digitados = []
chances = 3

print(f'Quatidade de Letras {len(palavra_secreta)}')
while True:

    if chances <= 0:
        print('')
        print('Você perdeu! O JOGO')
        break

    print(f'Você ainda tem "{chances}" chances!')

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('')
        print('Digite apenas uma letra')
        continue

    # salvando cada letra que o usuário digitou

    digitados.append(letra)
    # print(digitados)

    if letra not in palavra_secreta:
        chances -= 1

    # se a letra digitada estiver em palavra secreta
    if letra in palavra_secreta:
        print(f'Acertou! A Letra "{letra}" existe na palavra')
    else:
        print(f'Incorreta! Letra "{letra}" não pertence a palavra secreta.')
        # pop irá tirar o último elemento que foi inserido
        digitados.pop()

    formando_palavra = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in digitados:
            formando_palavra += letra_secreta
        else:
            formando_palavra += '*'

    if formando_palavra == palavra_secreta:
        print('')
        print(f'Fim de jogo! Ganhou!\nPalavra: {palavra_secreta}')
        break
    else:
        print(f'A palavra secreta está assim: {formando_palavra} ')

    print('')



