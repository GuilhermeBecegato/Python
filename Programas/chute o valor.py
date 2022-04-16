import random

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

escolha = random.choice(numeros)

nmr =input('Chute um número de 0 a 10 >> ')


if nmr > escolha:
    print('Seu chute foi menor que a escolha')
    print(f'Numero escolhido: {escolha}\nSeu chute: {nmr}')

elif nmr < escolha:
    print('Seu chute foi maior que a escolha')
    print(f'Numero escolhido: {escolha}\nSeu chute: {nmr}')

elif nmr == escolha:
    print('Você acertou!!')