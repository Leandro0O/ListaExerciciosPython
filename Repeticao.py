import math


class Repeticao:
    def __init__(self) -> None:
        pass

    # Criar um algoritmo que apresente o quadrado dos números inteiros de 15 a 200.
    def ex1():
        for i in range(15, 200):
            print(f'{pow(i,2)}')

    # Criar um algoritmo que apresente na tela os números de 1 a 50 em ordem decrescente.
    def ex2():
        for i in range(50, 0, -1):
            print(f'{i}')

    # Criar um algoritmo que calcule e apresente na tela a tabuada do 8 (1 a 10).
    def ex3():
        print(f'A tabuada do 8 é\n')
        for i in range(1, 11):
            print(f'8 x {i} = {(i*8)}')

    # Criar um algoritmo que leia um número inteiro positivo e apresente na tela a sua tabuada (1 a 10).
    def ex4():
        num = int(input('Informe um numero para saber a tabuada:\n'))
        print(f'A tabuada de {num} é\n')
        for i in range(1, 11):
            print(f'{num} x {i} = {(i*num)}')

    # Criar um algoritmo que apresente na tela o total da soma dos cem primeiros números inteiros positivos (1 + 2 + 3 + ... + 98 + 99 + 100).
    def ex5():
        soma = 0
        for i in range(0, 101):
            soma = soma + i
        print(f'A soma é {soma}')

    # Criar um algoritmo que apresente os valores da conversão de polegadas para centímetros, de 3 em 3, iniciando a contagem em 1 polegada e terminando em 13 polegadas. Uma polegada equivale a aproximadamente 2,54 centímetros.
    def ex6():
        for i in range(1, 14):
            cm = i * 2.54
            i += 3
            print(cm)

    # O número 3025 possui a seguinte característica:  e . Criar um algoritmo que apresente na tela todos os números de quatro algarismos que possuem a característica citada.
    def ex7():
        for i in range(1000, 9999):
            num1 = int(i / 100)
            num2 = int(i % 100)
            soma = num1+num2
            quad = int(soma * soma)
            if i == quad:
                print(i)

    # Criar um algoritmo que leia um número inteiro e apresente na tela o seu fatorial. (Dica: 5! = 5x4x3x2x1 = 120).
    def ex8():
        num = int(input('Informe um numero para saber o fatorial:\n'))
        fatorial = 1
        for i in range(1, num+1):
            fatorial *= i
        print(f'{num}! = {fatorial}')

    # Criar um algoritmo que leia um valor N e apresente na tela todos os valores inteiros entre 1 e N. Considere que o valor de N será sempre maior que zero.
    def ex9():
        num = int(input('Informe um numero:\n'))
        for i in range(1, num):
            print(i)

    # Criar um algoritmo que efetue a leitura de 10 valores numéricos inteiros e, ao final, apresente na tela a soma e a média dos valores lidos.
    def ex10():
        soma = 0
        for i in range(1, 11):
            num = int(input(f'Informe o {i}° numero:\n'))
            soma += num
        media = soma/10
        print(f'Soma: {soma}\nMédia: {media}')

    # Criar um algoritmo que leia o número de horas trabalhadas diárias (NH) de um funcionário por um período de 20 dias (ele trabalhou todos os 20 dias) e apresente na tela o total de horas trabalhadas por ele nesse período.
    def ex11():
        th = 0
        for i in range(1, 21):
            ht = int(input(f'Informe as horas trabalhadas no {i}° dia:\n'))
            th += ht
        print(f'O funcionario trabalhou {th} horas durante os 20 dias')

    # Um professor possui 3 turmas, e cada turma possui 5 alunos. Criar um algoritmo que leia a nota dos alunos de cada uma das turmas e apresente a média das notas por turma.
    def ex12():
        for i in range(1, 4):
            print(f'Inform as notas da {i}° turma\n')
            for j in range(1, 6):
                total = 0
                nota = float(input(f'Informe a {j}° nota:\n'))
                total += nota
            media = total/5
            print(f'A media das notas da {i}° turma é {media}\n')

    # Criar um algoritmo que apresente na tela a tabuada dos números de 1 a 9.
    def ex13():
        for i in range(1, 11):
            print(f'A tabuada de {i} é\n')
            for j in range(1, 11):
                print(f'{i} x {j} = {(i*j)}\n')

    # Criar um algoritmo que leia um número inteiro e repita a operação de multiplicar o número por 3 (apresentando o novo valor) até que o número seja maior que 100. Por exemplo, se o usuário informar 5, o algoritmo deve apresentar na tela a seguinte sequência: 5 15 45 135.
    def ex14():
        num = int(input('Informe um numero:\n'))
        while num < 100:
            num *= 3
            print(f'{num}')

    # O quadrado de um número natural N é dado pela soma dos N primeiros números ímpares consecutivos. Por exemplo, , , , , etc. Criar um algoritmo que leia um número inteiro positivo maior que zero, calcule e apresente na tela seu quadrado usando a soma de ímpares ao invés de produto.
    def ex15():
        num = int(input('Informe um numero::\n'))
        i = 0
        quad = 0
        while i < num*2:
            i += 2
            quad = i
        print(f'{num}² = {quad}')

    # Uma loja está levantando o valor total de todas as mercadorias em estoque. Criar um algoritmo que permita a entrada dos seguintes dados:
    # o número total de mercadorias no estoque;
    # o valor de cada mercadoria.
    # Ao final, apresentar na tela o valor total em estoque e a média dos valores das mercadorias.

    def ex16():
        quant = int(input('Informe a quantidade de mercadoria no estoque:\n'))
        cont = 0
        soma = 0
        while cont < quant:
            valor = float(input('Informe o valor da mercadoria:\n'))
            soma+=valor
            cont+=1
        media = soma/quant
        print(f'Valor total produtos R$ {soma:.2f}\nMedia valor R$ {media:.2f}')

    
    # Um número inteiro é perfeito se o dobro dele é igual à soma de todos os seus divisores. Por exemplo, como os divisores de 6 são 1, 2, 3 e 6 e 1 + 2 + 3 + 6 = 12, 6 é perfeito. A matemática ainda não sabe se a quantidade de números perfeitos é ou não finita. Criar um algoritmo que leia um número inteiro positivo N e apresente na tela a lista de todos os números inteiros positivos perfeitos menores N.
    def ex17():
        cont = 1
        num = int(input('Informe um numero:\n'))
        while cont < num:
            if num % cont == 0:
                print(f'{cont}')
                cont+=1

    # Criar um algoritmo que leia um número inteiro positivo e apresente na tela o número de algarismos deste número.
    def ex18():
        cont = 0
        num = input('Informe um numero:\n')
        for i in range(len(num)):
            cont+=1
        print(f"o {num} possui {cont} {'algarismos' if len(num) > 1 else 'algarismo'}")

    # Criar um algoritmo que apresente na tela os valores da conversão de graus Celsius em Fahrenheit, de 10 em 10, iniciando a contagem em 10 graus em terminando em 200 graus. A fórmula de conversão é: 
    def ex19():
        for i in range(10,201,+10):
            f = i * 1.8 + 32
            print(f'{i} °C = {f:.2f} °F')
    
    # Criar um algoritmo que apresente na tela os valores da conversão de graus Fahrenheit em Celsius, de 2 em 2, iniciando a contagem em 50 graus e terminando em 66 graus. A fórmula de conversão é: .
    def ex20():
        for i in range(50,67,+2):
            c = (i - 32) / 1.8
            print(f'{i} °F = {c:.2f} °C ')
    
    # Criar um algoritmo que leia dois números inteiros (positivos e maiores que zero) e apresente na tela o resultado da multiplicação dos números. Não utilize o operador de multiplicação "*". Use para a solução deste problema estrutura de repetição (laço).
    def ex21():
        num1 = int(input('Informe o primeiro número:\n'))
        num2 = int(input('Informe o segundo número:\n'))
        soma = 0
        for i in range(num2):
           soma+=num1 
        print(f'{num1} x {num2} = {soma}')
    
    # Criar um algoritmo que leia dois números inteiros (positivos e maiores que zero) e apresente na tela o resultado inteiro da divisão do primeiro pelo segundo número. Não utilize qualquer operador de divisão nem qualquer função para obter o resultado inteiro da divisão. Use para a solução deste problema estrutura de repetição (laço).
    def ex22():
        num1 = int(input('Informe o primeiro número:\n'))
        num2 = int(input('Informe o segundo número:\n'))
        div = 1
        i = num1
        while i > num2:
            div+=1
            i-=num2
        
        print(f'{num1} / {num2} = {div}')
    
    #  Criar um algoritmo que leia uma base e um expoente e apresente na tela o valor da potência da base pelo expoente. Considere apenas a entrada de valores inteiros e positivos (maiores que zero). Não utilize qualquer função para calcular a potência. Use para a solução deste problema estrutura de repetição (laço)
    def ex23():
        base = int(input('Informe uma base:\n'))
        expo = int(input('Informe o expoente:\n'))
        soma = 1
        for i in range(expo):
            soma*=base
        print(f'{base} ^ {expo} = {soma}')
    
    # Criar um algoritmo que apresente na tela a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é formada pela seqüência: 1, 1, 2, 3, 5, 8, 13, 21, 34, ... etc., caracterizando-se pela soma de um termo posterior com o seu anterior subseqüente.
    def ex24():
        n1 =1 
        n2 = 0
        print(n1)
        for i in range(15):
            n1+=n2
            n2 = n1 - n2
            print(n1)
    
    #  Criar um algoritmo que apresente todos os números inteiros divisíveis por 4 existentes na faixa de 1 a 200
    def ex25():
        for i in range(1,201):
            if i % 4 == 0:
                print(i)
    
    # Criar um algoritmo que apresente todos os números inteiros ímpares, existentes na faixa de 0 a 25.
    def ex26():
        for i in range(1,25,+2):
            print(i)
    
    # Criar um algoritmo que apresente a média dos números inteiros divisíveis por 5 existentes na faixa de 0 a 136.
    def ex27():
        numeros = []
        for i in range(0,136):
            if i % 5 == 0:
                numeros.append(i)
        media = sum(numeros) / len(numeros)
        print(f'A media é : {media:.2f}')

    # Criar um algoritmo que apresente a média dos números inteiros divisíveis por 7 existentes na faixa de 0 a 128.
    def ex28():
        numeros = []
        for i in range(0,128):
            if i % 7 == 0:
                numeros.append(i)
        media = sum(numeros) / len(numeros)
        print(f'A media é : {media:.2f}')
    
    # Criar um algoritmo que conte de 1 a 100 e a cada múltiplo de 10 apresenta a mensagem Múltiplo de 10.
    def ex29():
        for i in range(1,100):
            if i % 10 == 0:
                print(f'{i} é multiplo de 10')
    
    # Criar um algoritmo que apresente o resultado da soma e da média aritmética dos valores inteiros pares situados na faixa numérica de 50 a 70.
    def ex30():
        numeros = []
        for i in range(50,70):
            numeros.append(i)
        
        media = sum(numeros) / len(numeros)
        print(f'Media: {media:.2f}\nSoma: {sum(numeros)}')
    
    # Criar um algoritmo que leia 15 números inteiros e apresente a soma dos números divisíveis por 3.
    def ex31():
        soma = []
        for i in range(1,16):
            num = int(input(f'Informe o {i}° numero:\n'))
            if num % 3 == 0:
                soma.append(num)
        print(f'Soma: {sum(soma)}')

    # Criar um algoritmo que leia a idade de 10 pessoas e apresente a quantidade de pessoas maiores de idade (Uma pessoa é maior de idade se sua idade for maior ou igual a 18 anos).
    def ex32():
        maior = 0
        for i in range(1,11):
            idade = int(input(f'Informe a idade da {i}° pessoa:\n'))
            if idade >= 18:
                maior+=1
        print(f"{maior} {'maiores' if maior > 1 else 'maior'} de idade")
    
    # Criar um algoritmo que leia 15 valores inteiros positivos e apresente a soma dos valores menores que 40.
    def ex33():
        soma = []
        for i in range(1,16):
            num = int(input(f'Informe o {i}° numero:\n'))
            if num < 40:
                soma.append(num)
        print(f'Soma: {sum(soma)}')
    
    # Criar um algoritmo que leia 10 valores inteiros e apresente a quantidade de números negativos.
    def ex34():
        negativo = 0
        for i in range(1, 11):
            num = int(input(f'Informe o {i}° numero:\n'))
            if num < 0:
                negativo+=1
        print(f'Numeros negativos: {negativo}')
    
    # Criar um algoritmo que leia 10 valores inteiros e apresente na tela quantos destes valores estão no intervalo [10,20] e quantos deles estão fora deste intervalo.
    def ex35():
        dentro = 0
        fora = 0
        for i in range(1,11):
            num = int(input(f'Informe o {i}° numero:\n'))
            if num in range(10,20):
                dentro+=1
            else:
                fora+=1
        print(f'Dentro do intervalo de 10 a 20: {dentro}\nFora do intervalor de 10 a 20: {fora}')