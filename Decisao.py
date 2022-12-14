import math

class Decisao:
    def __init__(self) -> None:
        pass
    
    # Criar um algoritmo que lê um número e verifica se ele é negativo. Se for negativo, imprimir na tela a mensagem "Numero negativo".

    def ex1():
        num = int(input('Informe um nuumero:\n'))
        resposta = "Positivo" if num > 0 else "Negativo"
        return print(resposta)

    # Criar um algoritmo que leia dois números L e R. O programa deve verificar a maior área entre um quadrado de lado L e um círculo de raio R. Imprimir na tela qual o maior: "Quadrado" ou "Circulo".
    def ex2():
        l = int(input('Informe o lado do quadrado:\n'))
        r = int(input('Informe o raio do circulo:\n'))
        l = pow(l,2)
        r = math.pi * pow(r,2)
        resposta = "A area do quadrado é maior" if l > r else "A area do circulo é maior"
        return print(resposta)

    # Criar um algoritmo que leia três números e imprime o maior deles.
    def ex3():
        num = int(input('Informe o primeiro numero:\n'))
        num2 = int(input('Informe o segundo numero:\n'))
        num3 = int(input('Informe o terceiro numero:\n'))
        if num > num2 and num > num3:
            print(f'{num} é o maior numero')
        elif num2 > num and num2 > num3:
            print(f'{num2} é o maior numero')
        else:
            print(f'{num3} é o maior numero')
    
    # Criar um algoritmo que leia um valor e apresente na tela se esse valor é positivo ou negativo (considere o valor zero como positivo).
    def ex4():
        num = int(input('Informe um nuumero:\n'))
        resposta = f"{num} é Positivo" if num > 0 else "{num} é Negativo"
        return print(resposta)
    
    # Criar um algoritmo que leia dois números e imprime a divisão do maior pelo menor.
    def ex5():
        num1 = int(input('Informe o primeiro número:\n'))
        num2 = int(input('Informe o segundo número:\n'))
        if num1 > num2:
            print(f'{num1} / {num2} = {num1/num2}')
        else:
            print(f'{num2} / {num1} = {num2/num1}')    

    # Criar um algoritmo que leia uma velocidade e caso o valor lido seja maior que 70 apresentar na tela Multado.
    def ex6():
        v = float(input('Informe a velocidade:\n'))
        resposta = "Multado" if v > 70 else ""
        return print(resposta)
    
    # Criar um algoritmo que leia uma velocidade, caso o valor lido for maior que 70 apresentar na tela a mensagem Multado, caso contrário apresentar na tela a mensagem Não Multado.
    def ex7():
        v = float(input('Informe a velocidade:\n'))
        resposta = "Multado" if v > 70 else "Não multado"
        return print(resposta)

    # Uma empresa decide dar aumento de 15% aos funcionários cujo salário é inferior a 500 reais. Criar um algoritmo que leia o salário de um funcionário e apresente na tela o valor do salário reajustado ou o valor do salário informado caso ele não tenho direito ao reajuste.
    def ex8():
        salario = float(input('Informe o salario:\n'))
        if salario < 500:
            salario = salario + (salario * 0.15)
            print(f'Salario reajustado R$ {salario:.2f}')
        else:
            print(f'Salario R$ {salario:.2f}')
    
    # Criar um algoritmo que leia o valor de uma conta de luz e, caso o valor seja maior que R$ 50,00 e menor que R$ 500,00 apresente na tela a mensagem Você está gastando muito. Caso contrário não exiba mensagem nenhuma.
    def ex9():
        v = float(input('Informe o valor da conta de luz:\n'))
        if v > 50 and v < 500:
            print('Voce estã gastando muito.')
    
    # Criar um algoritmo que leia o valor total de vendas do mês de um determinado vendedor e o seu nome, e apresente na tela o nome do vendedor quando o valor da venda estiver entre R$ 1.000,00 e R$ 5.000,00.
    def ex10():
        nome = input('Informe o nome do vendedor:\n')
        valorV = float(input('Informe o valor total das vendas:\n'))
        if valorV >= 1000 and valorV <= 5000:
            print(f'Vendedor: {nome}\nValor vendas: R$ {valorV:.2f}')

    # Criar um algoritmo que leia um valor numérico inteiro positivo ou negativo e apresentar o valor lido como sendo um valor positivo, ou seja, se o valor lido for menor que zero, ele deve ser multiplicado por -1.
    def ex11():
        num = int(input('Informe um numero:\n'))
        if num < 0:
            num*=-1
            print(num)
        else:
            print(num)
    
    # Criar um algoritmo que leia um número inteiro e apresente na tela o número lido caso ele seja divisível por 4 mas não por 5.
    def ex12():
        num = int(input('Informe um numero:\n'))
        if num % 5 == 0:
            print(num)

    # Criar um algoritmo que leia duas variáveis do tipo lógico, caso ambas sejam verdadeiras apresentar na tela Tem Desconto
    def ex13():
        b1 = bool(input("True ou False?\n"))
        b2 = bool(input('True ou False?\n'))
        if b1 == True and b2 == True:
            print("Tem desconto!")
    
    # Criar um algoritmo que leia um número inteiro e apresente na tela o número lido caso ele seja divisível por 2 e 3. 
    def ex14():
        num = int(input('Informe um numero:\n'))
        if num % 2 == 0 and num % 3 == 0:
            print(num) 

    # Criar um algoritmo que leia um número inteiro e apresente na tela o número lido caso ele seja divisível por 4 ou 5.
    def ex15():
        num = int(input('Informe um numero:\n'))
        if num % 4 == 0 or num % 5 == 0:
            print(num) 

    # Criar um algoritmo que leia dois números inteiros e apresente uma mensagem indicando se o primeiro número é múltiplo do segundo.
    def ex16():
        num1 = int(input('Informe um numero:\n'))
        num2 = int(input('Informe outro numero:\n'))
        if num1 % num2 == 0:
            print(f'{num1} é multiplo de {num2}')

    # As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Criar um algoritmo que leia o número de maçãs compradas, calcule e apresente na tela o custo total da compra.
    def ex17():
        quant = int(input('Informe a quantidade de maçãs compradas:\n'))
        if quant < 12:
            total = quant* 1.30
            print(f'Total R$ {total:.2f}')
        else:
            total = quant* 1.00
            print(f'Total R$ {total:.2f}')
    
    # Criar um algoritmo que leia dois valores inteiros (considere que não serão lidos valores iguais) e apresente-os em ordem crescente.
    def ex18():
        num1 = int(input('Informe um numero:\n'))
        num2 = int(input('Informe outro numero:\n'))
        if num1 < num2:
            print(f'{num1}, {num2}')
        else:
            print(f'{num2}, {num1}')
    
    # Criar um algoritmo que leia a idade de uma pessoa e apresente na tela uma mensagem de maioridade ou não.
    def ex19():
        idade = int(input('Informe sua idade:\n'))
        if idade >= 18:
            print('Você é maior de idade!')

    # Criar um algoritmo que leia o salário de um funcionário, calcule e apresente o salário reajustado, de acordo com a seguinte regra: 
    # salários até R$ 300, reajuste de 15%; 
    # salários maiores que R$ 300, reajuste de 7,5%.
    def ex20():
        s = float(input('Informe o salário:\n'))
        if s <= 300:
            s = s + (s*0.15)
            print(f'Salarario: R$ {s:.2f}')
        else:
            s = s + (s*0.075)
            print(f'Salarario: R$ {s:.2f}')

    # Criar um algoritmo que leia o ano atual e o ano de nascimento de uma pessoa. Apresentar na tela uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).
    def ex21():
        anoA = int(input('Informe o ano atual:\n'))
        anoN= int(input('Informe o ano de nascimento:\n'))
        idade = anoA - anoN
        if idade >= 18:
            print('Você pode votar!')
        else:
            print('Você não pode votar!')
    
    # Uma livraria esta fazendo uma promoção para pagamento à vista em que o comprador pode escolher entre dois critérios de desconto: 
    # Critério A: R$ 0,25 por livro + R$ 7,50 fixo;
    # Critério B: R$ 0,50 por livro + R$ 2,50 fixo.
    # Criar um algoritmo em que o usuário informe a quantidade de livros que deseja comprar e o programa diz qual é a melhor opção de desconto.
    def ex22():
        quant = int(input('Informe a quantidade de livros:\n'))
        critA = (quant * 0.25) + 7.50
        critB = (quant * 0.50) + 2.50
        if critA < critB:
            print('Critério A vale mais a pena!')
        else:
            print('Critério B vale mais a pena!')

    # Criar um algoritmo que leia a altura e o sexo de uma pessoa (M ou F) e apresente o seu peso ideal, utilizando a seguinte fórmula:
    # para homens: (72.7 * altura) - 58
    # para mulheres: (62.1 * altura) - 44.7
    def ex23():
        sexo = input('Informe o sexo (M ou F):\n')
        altura = float(input('Informe a altura:\n'))
        if sexo.upper() == 'M':
            peso = (72.7 * altura) - 58
            print(f'Peso ideal: {peso:.2f} Kg')
        else:
            peso = (72.7 * altura) - 58
            print(f'Peso ideal: {peso:.2f} Kg')
        
    # Criar um algoritmo que leia a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas inteiras, sem os minutos), calcule e apresente na tela a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.
    def ex24():

        start = int(input('Informe a hora do inicio da partida:\n'))
        end = int(input('Informe a hora do fim da partida:\n'))
        total = end - start
        if total < 24:
            print(f"A duaração da partida foi de  {total} {'horas' if total > 1 else 'hora'}")

    # Criar um algoritmo que efetue o cálculo do reajuste de salário de um funcionário. Considere que o funcionário deve receber um reajuste de 15% caso seu salário seja menor que R$ 500,00. Se o salário for maior ou igual a R$ 500,00 mas menor ou igual a R$ 1.000,00, seu reajuste será de 10%; caso seja ainda maior que R$ 1.000,00, o reajuste deverá ser de 5%.
    def ex25():
        salario = float(input('Informe o salario do funcionário:\n'))
        if salario < 500:
            salario = salario + (salario*0.15)
            print(f'Salario: R$ {salario:.2f}')
        elif salario >= 500 and salario <= 1000:
            salario = salario + (salario*0.10)
            print(f'Salario: R$ {salario:.2f}')
        else:
            salario = salario + (salario*0.05)
            print(f'Salario: R$ {salario:.2f}')
    
    # Criar um algoritmo que leia o peso e a altura de uma pessoa, calcule o seu IMC (Índice de Massa Corporal), e apresente na tela uma mensagem informando se a pessoa está ou não no seu peso ideal, de acordo com a tabela abaixo. A fórmula para calcular o IMC é: 
    def ex26():
        peso = float(input('Informe o seu peso:\n'))
        altura = float(input('Informe a sua altura:\n'))
        imc = peso / pow(altura,2)
        if imc < 20:
            print(f'IMC: {imc:.2f}\nAbaixo do peso!')
        elif imc <= 20 and imc < 25:
            print(f'IMC: {imc:.2f}\nPeso ideal!')
        else:
            print(f'IMC: {imc:.2f}\nAcima do peso!')

    # Criar um algoritmo que leia o código de origem de um produto e apresente na tela a sua procedência. A procedência obedece a seguinte tabela:
    def ex27():
        cod = int(input('Informe o codigo de origem:\n'))
        if cod in (5,6):
            print(f'Cod: {cod} -> Nordeste')
        elif cod in range(7,10):
            print(f'Cod: {cod} -> Sudeste')
        elif cod in range(10,21):
            print(f'Cod: {cod} -> Centro-Oeste')
        elif cod in range(21,31):
            print(f'Cod: {cod} -> Nordeste')
        else:
            print('Codigo invalido.')

    # Criar um algoritmo que leia o salário de um funcionário e calcule o imposto de renda (IR) a ser pago a partir do salário do funcionário. Se o salário for menor que R$ 1.257,12 está isento do imposto. Se o salário for entre R$ 1.257,12 e R$ 2.510,00 (inclusive), a alíquota do imposto é 17%. Se o salário for superior a R$ 2.510,00, a alíquota do imposto é 28%. Apresentar na tela o salário bruto, o salário líquido e o valor do imposto.
    def ex28():
        salario = float(input('Informe o salario:\n'))
        if salario < 1257.12:
            print(f'Salario: R$ {salario:.2f}\nLivre de imposto')
        elif salario >= 1257.12 and salario <= 2510:
            salario = salario - (salario * 0.17)
            print(f'Salario: R$ {salario:.2f}\nImposto de 17%')
        else:
            salario = salario - (salario * 0.28)
            print(f'Salario: R$ {salario:.2f}\nImposto de 28%')

    # Criar um algoritmo que leia o valor de três notas escolares de um aluno. Calcular a média aritmética e apresentar na tela a mensagem Aprovado se a média obtida for maior ou igual a 7; caso contrário, o algoritmo deve solicitar a nota de exame do aluno e calcular uma nova média aritmética entre a nota do exame e a primeira média aritmética. Se o valor da nova média for maior ou igual a 5, apresentar na tela a mensagem Aprovado em exame'; caso contrário, apresentar a mensagem Reprovado. Informar junto com cada mensagem o valor da média obtida.
    def ex29():
        n1 = float(input('Informe a primeira nota:\n'))
        n2 = float(input('Informe a segunda nota:\n'))
        n3 = float(input('Informe a terceira nota:\n'))
        media = (n1+n2+n3) / 3
        if media >=7:
            print(f'Media: {media:.2f}\nAprovado!')
        else:
            print(f'Media: {media:.2f}\nEm recuperação!')
            nx= float(input('Informe a nota do exame:\n'))
            media = (media+nx) / 2
            if media >= 5:
                 print(f'Media: {media:.2f}\nAprovado em exame!')
            else:
                 print(f'Media: {media:.2f}\nReprovado!')
    
    # Criar um algoritmo que leia dois números inteiros e apresente na tela uma mensagem indicando se são iguais ou diferentes. Se os números são diferentes, apresentar na tela o maior e o menor número (nesta sequência).
    def ex30():
        num1 = int(input('Informe o primeiro número:\n'))
        num2 = int(input('Informe o segundo número:\n'))
        if num1 == num2:
            print('Os números são iguais.')
        elif num1 < num2:
            print(f'{num1}, {num2}')
        else:
            print(f'{num2}, {num1}')

    # Criar um algoritmo que leia dois números inteiro positivos (A e B). Caso A seja igual a B, apresentar na tela a soma dos dois números. Caso contrário, apresentar na tela a diferença do maior pelo menor número.
    def ex31():
        a = int(input('Informe o primeiro número:\n'))
        b = int(input('Informe o segundo número:\n'))
        if a == b:
            soma = a + b
            print(f'{soma}')
        else:
            if a < b:
                dif = a - b
                print(f'{dif}')
            else:
                dif = b - a
                print(f'{dif}')

    # Criar um algoritmo que represente uma calculadora de quatro operações. O algoritmo deve ler o valor de dois operandos e um operador (+, -, * ou /), efetuar o cálculo desejado e apresentar na tela o resultado.
    def ex32():
        num1 = float(input('Informe o primeiro numero:\n'))
        num2 = float(input('Informe o segundo numero:\n'))
        op =input('Informe a operação:\n+ --> SOMA\n- --> SUBTRAÇÃO\n/ --> DIVISÃO\n* --> MULTIPLICAÇÃO\n')
        match(op):
            case '+':
                soma = num1 + num2
                print(f'{num1} + {num2} = {soma:.2f}')
            case '-':
                sub = num1 - num2
                print(f'{num1} - {num2} = {sub:.2f}')
            case '/':
                div = num1 / num2
                print(f'{num1} / {num2} = {div:.2f}')
            case '*':
                mult = num1 * num2
                print(f'{num1} * {num2} = {mult:.2f}')
            case _:
                print(f'Opção invalida')
    
    # Criar um algoritmo que leia 3 notas de um aluno, calcule a sua média e apresente na tela a sua menção, de acordo com as regras abaixo:
    def ex33():
        n1 = float(input('Informe a primeira nota:\n'))
        n2 = float(input('Informe a segunda nota:\n'))
        n3 = float(input('Informe a terceira nota:\n'))
        media = (n1+n2+n3) / 3
        if media >= 9:
            print("Menção MB")
        elif media <= 7 and media < 9:
            print("Menção B")
        elif media <= 5  and media < 7:
            print("Menção R")
        else:
            print('Menção I')
        
    # Criar um algoritmo que leia a idade de um nadador e apresenta na tela a sua categoria seguindo as regras:
    def ex34():
        idade = int(input('Informe sua idade:\n'))
        if idade in range(5,8):
            print("Ifantil A")   
        elif idade in range(8,11):
            print("Ifantil B")
        elif idade in range(11,14):
            print("Juvenil A")
        elif idade in range(14,18):
            print("Juvenil B")
        else:
            print('Sênior')

    # Criar um algoritmo que leia o código de um livro e apresente na tela a categoria do livro, conforme a tabela abaixo:
    def ex35():
        cod = input('Informe o código do livro(A, B, C):\n')
        match(cod.upper()):
            case 'A':
                print("Ficção")
            case 'B':
                print('Não-Ficção')
            case 'C':
                print('Auto-Ajuda')
            case _:
                print("Inválido")


            