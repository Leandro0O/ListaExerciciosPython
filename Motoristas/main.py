# Faça um algoritmo que leia o nome, a idade, e se tem carteira de motorista de 15 pessoas. Implemente as seguintes regras:

# Caso a idade seja menor que 18 anos, não pergunte se tem carteira de motorista.
# Precisamos de dois motoristas para dirigir em uma viagem.
# Ao identificar os dois primeiros, pare o questionário.
# Ao final, exiba o nome dos motoristas ou caso não encontre os dois, exiba: viagem não será realizada devido falta de motoristas.

motoristas = []
c = 0
while(c < 2 and range(15)):

    nome = input('Qual o seu nome? \n')
    idade = int(input('Qual a sua idade?\n '))
    if(idade >= 18):
        carteira = input('Você tem carteira de motorista?\nS --> SIM\nN --> NÃO\n')
        if(carteira.lower() == 's'):
            motoristas.append(nome)
            c+=1

if(motoristas == None):
    print('Viagem não será realizada devido falta de motoristas')
else:
    print('Seus motoristas são:')
    for i in motoristas:
        print(i)
        


