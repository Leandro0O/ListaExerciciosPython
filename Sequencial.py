class Sequencial:
    def __init__(self) -> None:
        pass

    # Criar um algoritmo que leia um número inteiro e apresente na tela o seu antecedente e o seu sucessor.
    def ex1():
        num = int(input('Informe um número:\n'))
        print(f'O sucessor de {num} é {num + 1} e o antecessor é {num - 1}')

    # Criar um algoritmo que lê dois números inteiros e imprime os números consecutivos desses números. (Por exemplo: se o usuário digitar 2 e ­9, a saída deverá ser 3 e ­8, porque 3 é consecutivo de 2. –8 é consecutivo de –9).
    def ex2():
        num1 = int(input('Informe um número:\n'))
        num2 = int(input('Informe outro número:\n'))
        print(f'{num1 + 1}\n{num2 + 1}')

    # Criar um algoritmo que leia dois números inteiros e apresenta na tela a soma, subtração, multiplicação e divisão dos respectivos números.
    def ex3():
        num1 = int(input('Informe um número:\n'))
        num2 = int(input('Informe outro número:\n'))
        print(f'{num1} + {num2} = {num1 + num2}')
        print(f'{num1} - {num2} = {num1 - num2}')
        print(f'{num1} x {num2} = {num1 * num2}')
        print(f'{num1} / {num2} = {num1 / num2}')

    # Criar um algoritmo que leia dois números inteiros e apresente na tela o resto da divisão do primeiro pelo segundo número.
    def ex4():
        num1 = int(input('Informe um número:\n'))
        num2 = int(input('Informe outro número:\n'))
        print(f'{num1} % {num2} = {num1 % num2}')

    # Criar um algoritmo que leia a idade de uma pessoa expressa em anos e apresente na tela esta idade expressa em meses e dias.
    def ex5():
        anos = int(input('Informe sua idade em anos:\n'))
        meses = anos * 12
        dias = anos * 365
        print(f'Sua idade em:\nAnos: {anos}\nMeses: {meses}\nDias: {dias}')

    # Criar um algoritmo que leia a idade de uma pessoa expressa em anos, mês e dias e apresente na tela a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
    def ex6():
        print('Informe sua idade')
        anos = int(input('Anos:\n'))
        meses = int(input('Meses:\n'))
        dias = int(input('Dias:\n'))
        anos*=365
        meses*=30
        idade = anos + meses + dias
        print(f'Sua idade é {idade} dias')  

    # Criar um algoritmo que leia a idade de uma pessoa expressa em dias e apresente na tela a idade dessa pessoa expressa em anos, meses e dias. Considerar ano com 365 dias e mês com 30 dias.
    def ex7():
        idade = int(input('Informe sua idade em dias:\n'))
        anos = idade / 365
        meses = (idade % 365) / 30
        dias = (idade % 365) % 30
        print(f'Você tem:\nAnos: {round(anos)}\nMeses: {round(meses)}\nDias: {round(dias)}')