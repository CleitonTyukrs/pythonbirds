palavra = 'CLEYTON'.upper()
print('-=-'*20)
print('JOGO DA VELHA')
print('Digite um a letra:', end='')

for letra in palavra:
    print('_', end='')

conjunto_de_letras_palavra = set(palavra)
conjunto_de_letras_digitadas = set()
erro = 0

while not conjunto_de_letras_palavra.issubset(conjunto_de_letras_digitadas) and erro < 7:
    print('')
    print('')

    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_de_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_de_letras_palavra:
        print('A PALAVRA È: ', end='')

        for letra in palavra:
            if letra in conjunto_de_letras_digitadas:
                print(f'{letra}', end='')
            else:
                print('_', end='')

    else:
        erro +=1
        print(f'Errou..--> numeros de erros {erro} de 6 Tentativas, tente novamente!')
        print('')
        print(f'{letra} {conjunto_de_letras_digitadas}')
if erro < 7:
    print(' *** PARABENS VC ACERTOU! ***')
    print('-=-' * 20)
else:
    print('Infelismente vc perdeu!')
    print('-=-' * 20)