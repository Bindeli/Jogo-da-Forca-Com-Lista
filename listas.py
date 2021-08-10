"""
Listas em Python - há índices
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

"""
"""

texto = 'valor'
lista = [1, 2, 3, 4, 5, 'Lucas', 10.50]
#               0          1    2    3    4    5
lista1 = ['LucasBindeli', 'A', 'B', 'C', 'D', 'E']
#              -5         -4   -3   -2    -1   0

print(lista)

print(lista1[2])

lista1[5] = 'Qualquer outra coisa'
print(lista1[5])

print('Fatiamento:')

print(lista1[0:3])
print(lista1[::2])
print(lista1[::-1])

#

lista2 = [1, 2, 3]
lista3 = [4, 5, 6]

print(lista2)
print(lista3)

lista4 = lista2 + lista3
print(f'Lista4: {lista4}')

# extend

lista.extend(lista4)

print(f'Lista: {lista}')
lista.extend('a')
print(f'Lista modificada: {lista}')

# adicinando append, adiciona um novo valor ao final da lista

lista2.append('b')
print(f'Lista2 modificada com append: {lista2}')

# insert , inserir o valor em um determinado lugar

lista2.insert(1, 'banana')

print(f'Lista2 modificada com insert: {lista2}')

# pop, utilizando para remover um valor da lista
# caso não mencione, irá eliminar o ultimo

lista2.pop()
print(f'Lista2 removendo com pop: {lista2}')

#indices  0 1 2 3 4 5 6 7 8 9
lista5 = [1,2,3,4,5,6,7,8,9,10]

# irá remover do indice 3 até o 5
del(lista5[3:5])

print(lista5)

lista5.insert(0,'banana')
print(lista5)

del(lista5[0])
print(lista5)

# max e min

lista6 = [1,2,3,4,5,6,7,8]
print("Max e Min")
print( max(lista6))
print( min(lista6))

# Adicionando com range

# função builtin que converte a função iterável em uma lista

lista7 = range(0, 10)
print('Range')
# irá aparecer apenas range(0, 9)
print(lista7)

lista7 = list(range(0, 10))

print(f'Modificado com a função list : {lista7}')

# for valor in lista7:
#    print(valor)

# somando
print('soma')
soma = 0

for valor in lista7:
    soma = soma + valor

print(soma)

lista8 = ['String', True, 10, -20.5]
print('Pritando o tipo:')
for elemento in lista8:
    print(f' O tipo de {elemento} é {type(elemento)}')
print('')
print('Jogo da forca: ')
# jogo para adivinhar a palavra
# a pessoa irá digitar letra por letra
# se digitar f, irá aparecer que tem a letra
#

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('')
        print('Você perdeu!')
        break

    print(f'Você ainda tem {chances} chances!')

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('')
        print('Digite apenas uma letra')
        continue
    # salvar cada letra que o usuário digitou
    digitadas.append(letra)

    if letra not in secreto:
        chances -= 1

    # se a letra digitada tiver em secreto
    if letra in secreto:
        print(f'Acertou uma palavra! Letra {letra} existe na palavra secreta')
    else:
        print(f'Não acertou! Letra {letra} não pertence a palavra secreta')
        # para que não salve a letra incorreta na lista
        # o ultimo elemento adicionado será removido
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'


    if secreto_temporario == secreto:
        print('')
        print(f'Você Acertou! A palavra final é {secreto}')
        print('Fim')
        break
    else:
        print('')
        print(f'A palavra está assim: {secreto_temporario}')
        continue

