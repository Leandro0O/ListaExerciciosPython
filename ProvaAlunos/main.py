from random import randint

# Enunciado
# Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são os números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas corretas, além de quais o aluno acertou.

for i in range(5):
    a = randint(0,100)
    b = randint(0,100)
    quest = int(input(f'Qual a soma de {a} + {b} ?\n'))
    if(quest == (a + b)):
        print('Muito bem, você acertou!!!')
    else:
        print(f'Você errou!!\nA resposta certa é:\n{(a + b)}')
