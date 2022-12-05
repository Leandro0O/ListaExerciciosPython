
import math
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
        anos *= 365
        meses *= 30
        idade = anos + meses + dias
        print(f'Sua idade é {idade} dias')

    # Criar um algoritmo que leia a idade de uma pessoa expressa em dias e apresente na tela a idade dessa pessoa expressa em anos, meses e dias. Considerar ano com 365 dias e mês com 30 dias.
    def ex7():
        idade = int(input('Informe sua idade em dias:\n'))
        anos = idade / 365
        meses = (idade % 365) / 30
        dias = (idade % 365) % 30
        print(
            f'Você tem:\nAnos: {round(anos)}\nMeses: {round(meses)}\nDias: {round(dias)}')

    #Criar um algoritmo que receba uma determinada hora (hora e minutos separados) e apresente na tela a hora em minutos.
    def ex8():
        horas = int(input('Informe as horas:'))
        minutos = int(input('Informe os minutos:'))
        total = (horas * 60) + minutos
        print(f'{horas}Hs e {minutos} min = {total} min ')

    # Criar um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e apresente-o na tela expresso em horas, minutos e segundos.
    def ex9():
        duracao = int(input('Informe a duração do evendo em segundos:\n'))
        horas = duracao / 3600
        minutos = (duracao % 3600) / 60
        segundos = (duracao % 3600) % 60
        print(f'Duração do evendo foi de\nHoras: {round(horas)}\nMinutos: {round(minutos)}\nSegundos: {round(segundos)}')

    # Criar um algoritmo que leia uma velocidade fornecida em m/s (metros por segundo) e apresente na tela a velocidade em km/h. Para efetuar a conversão, multiplique o valor em m/s por 3.6.
    def ex10():
        ms = float(input('Informe a velocidade em metros por segundo:\n'))
        km = ms * 3.6
        print(f'{ms} M/s = {km} Km/h' )

    # Criar um algoritmo que leia uma distância e o total de litros de combustível gasto por um automóvel para percorrê-la, calcule e apresente na tela o consumo médio de combustível.
    def ex11():
        d = float(input('Informe a distancia percorrida:\n'))
        l = float(input('Informe a quantidade de combustível consumida:\n'))
        cm = d / l
        print(f'O consumo medio foi: {cm:.2f} L')

    # Criar um algoritmo que receba o valor do salário de um funcionário e o valor do salário mínimo e apresente na tela quantos salários mínimos ganha esse funcionário.
    def ex12():
        s = float(input('Informe o valor do seu salario:\n'))
        sm = float(input('Informe o valor do salario minimo:\n'))
        ts = s / sm
        print(f"Voce recebe {ts:.0f} {'salarios' if ts > 1 else 'salario'}")

    #  Criar um algoritmo que receba três notas de um aluno e apresente na tela a média aritmética entre essas notas.
    def ex13():
        n1 = float(input('Informe a primeira nota:\n'))
        n2 = float(input('Informe a segunda nota:\n'))
        n3 = float(input('Informe a terceira nota:\n'))
        media = (n1+n2+n3) / 3
        print(f'A média das notas é {media:.2f}')

    # Criar um programa que calcule e apresente na tela a área de um retângulo. Fórmula: .

    def ex14():
        b = float(input('Informe a base do retangulo:\n'))
        h = float(input('Informe a altura do retangulo:\n'))
        a = b*h
        print(f'A área do retangulo é {a}')

    # Criar um programa que calcule e apresenta na tela a área de um triângulo. Fórmula: .
    def ex15():
        b = float(input('Informe a base do retangulo:\n'))
        h = float(input('Informe a altura do retangulo:\n'))
        a = (b*h) / 2
        print(f'A área do retangulo é {a}')

    # Criar um algoritmo que calcule e apresente na tela o volume de uma esfera de raio R, em que R é um dado fornecido pelo usuário. O volume de uma esfera é dado por .
    def ex16():
        r = float(input('Informe o raio da esfera:\n'))
        v = 4/3 * math.pi * pow(r,2)
        print(f'O volume da esfera é {v:.2f}')

    # Criar um algoritmo que calcule e apresente na tela a área de um trapézio. Fórmula: .
    def ex17():
        bm = float(input('Informe a base maior:\n'))
        bme = float(input('Informe a base menor:\n'))
        h = float(input('Informe a altura:\n'))
        a = ((bm + bme) * h) / 2
        print(f'A área do trapezio é {a:.2f}')

    # Criar um algoritmo que calcule e apresente na tela o volume de uma caixa retangular, utilizando a fórmula: .
    def ex18():
        c = float(input('Informe o comprimento da  caixa:\n'))    
        l = float(input('Informe a largura da  caixa:\n'))    
        h = float(input('Informe a altura da  caixa:\n'))    
        v = c * l * h
        print(f'O volume da caixa é {v:.2f}')

    # Criar um algoritmo que lê dois números, a base e o expoente, e imprime a potência (base elevada ao expoente).
    def ex19():
        b = int(input('Informe a base:\n'))
        e = int(input('Informe o expoente:\n'))
        p = pow(b,e)
        print(f'{b} ^ {e} = {p}')

    # Criar um algoritmo que lê dois números e imprime a soma dos quadrados dos dois números. O quadrado de um número A é representado por .
    def ex20():
        num1 = int(input('Informe o primeiro número:\n'))
        num2 = int(input('Informe o segundo número:\n'))
        soma = pow(num1,2) + pow(num2,2)
        print(f'A soma dos quadrados é {soma}')

    # Criar um algoritmo que apresenta o valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deve solicitar o valor da cotação do dólar e também a quantidade de dólares disponível com o usuário.
    def ex21():
        qd = float(input('Informe a quantidade de dolares:\n'))
        cd = float(input('Informe a cotação do dolar R$:\n'))
        tr = qd * cd
        print(f'$ {qd:.2f} = R$ {tr:.2f}')
    
    #  Criar um algoritmo que leia três valores inteiros e apresente na tela o valor da soma dos quadrados dos três valores lidos.
    def ex22():
        num1 = int(input('Informe o primeiro número:\n'))
        num2 = int(input('Informe o segundo número:\n'))
        num3 = int(input('Informe o terceiro número:\n'))
        soma = pow(num1,2) + pow(num2,2) + pow(num3,2)
        print(f'A soma dos quadrados é {soma}')

    # Criar um algoritmo que leia três valores inteiros e apresente na tela o valor do quadrado da soma dos três números lidos.
    def ex23():
        num1 = int(input('Informe o primeiro número:\n'))
        num2 = int(input('Informe o segundo número:\n'))
        num3 = int(input('Informe o terceiro número:\n'))
        soma =  pow((num1+num2+num3),2)
        print(f'A soma dos quadrados é {soma}')

    # Criar um algoritmo que leia os dias letivos de uma instituição qualquer, calcule e apresenta na tela a quantidade máxima de faltas que um aluno pode possuir. Um aluno pode faltar até 25% dos dias letivos.
    def ex24():
        dias = int(input('Informe os dias letivos:\n'))
        faltas = dias + (dias * 0.25) - dias
        print(f'Voce pode ter {round(faltas)} faltas no ano')
    
    # Criar um algoritmo que leia o valor correspondente ao salário mensal de um trabalhador e também o valor do percentual de reajuste a ser atribuído ao salário. Apresente na tela o valor do novo salário
    def ex25():
        s = float(input('Informe o salário:\n'))
        reajuste = float(input('Informe o valor do reajuste:\n'))
        ns = s+(s*(reajuste/100))
        print(f'O novo salario é R$ {ns:.2f}')
    
    # Criar um algoritmo que leia a metragem (altura e base) de um muro e o valor do metro quadrado cobrado pelo pedreiro, calcule e apresente na tela o custo da mão-de-obra para levantá-lo.
    def ex26():
        h = float(input('Informe a altura do muro:\n'))
        b = float(input('Informe a base do muro:\n'))
        vm = float(input('Informe o valor do metro quadrado:\n'))
        total = (b*h) * vm
        print(f'O valor do serviço sera R$ {total:.2f}')

    # Sabe-se que  de carpete custa R$ 35,00. Criar um algoritmo que leia o comprimento e a largura de uma sala, em metros, calcule e apresente na tela o valor que será gasto para forrar todo o seu piso.
    