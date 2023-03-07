import random
class Vetores:
    def __init__(self) -> None:
        pass


    # Criar um programa que leia 8 elementos inteiros em um vetor A. Construir um vetor B do mesmo tipo e tamanho com os elementos do vetor A multiplicados por 3. O elemento B[0] recebe o elemento A[0] * 3, o elemento B[1] recebe o elemento A[1] * 3 e assim por diante, até a posição 7 do vetor. Apresentar os elementos do vetor B.
    def ex1():

        a = []
        b = []

        for i in range(8):
            num = int(input(f'Informe o {i+1}° numero:\n'))
            a.append(num)

        for j in range(8):
            b.append(a[j] * 3)
            print(f'{a[j]} x 3 = {b[j]}')

# Criar um programa que leia um vetor de 7 posições de valores inteiros, conte quantos valores estão na faixa [10,20] e substitua os valores que estão nesta faixa pelo número 0 (zero). Apresentar na tela a quantidade de valores modificados e o vetor modificado.

    def ex2():
        a = []

        for i in range(8):
            num = int(input(f'Informe o {i+1}° numero:\n'))
            a.append(num)
            if a[i] >= 10 or a[i-1] <= 20 :
                a[i] = 0
        print(a)
    
    # Criar um programa que leia um vetor de 10 posições de valores inteiros e em seguida leia dois valores inteiros X e Y quaisquer correspondentes a duas posições no vetor. Ao final apresentar na tela a soma dos valores encontrados nas posições X e Y.
    def ex3():
        a = []
        for i in range(10):
            pos = i
            num = int(input(f'Informe o {pos+1}° numero:\n'))
            a.append(num)
        x = a[random.randint(0,10)]
        y = a[random.randint(0,10)]
        print(f'{x} + {y} = {x+ y}')

        
    # Criar um programa que leia um vetor de 12 posições de valores inteiros e em seguida leia um valor inteiro X qualquer. Fazer uma busca do valor de X no vetor lido e informar a posição em que foi encontrado ou se não foi encontrado. 
    def ex4():
        a = []
        for i in range(12):
            pos = i
            num = int(input(f'Informe o {pos+1}° numero:\n'))
            a.append(num)
        x = int(input('Informe um numero para verificar a posição:\n'))
        if x in a:
            print(f'{x} esta na posição: {a.index(x)}')
        else:
            print(f'{x} não foi encontrado')
    
    # Criar uma função que copie o conteúdo de um vetor em um segundo vetor. A função deve retornar o vetor copiado. 
    def ex5():
        a = [44,2,90,42,20,26]
        b = a
        print(f'Lista original: {a}')
        print(f'Lista copiada: {b}')

    # Criar uma função que some o conteúdo de dois vetores e armazene o resultado em um terceiro vetor. A função deve retornar o terceiro vetor. 
    def ex6():
        a = [44,2,90,42,20,26]
        b = [32,43,108,57,78,20]
        c = []
        for i in range(6):
            c.append(a[i] + b[i])
        print(f'Soma dos valores de a e b: {c}')

    # Criar uma função para unir dois vetores de mesmo tamanho e mesmo tipo em um terceiro vetor com dobro do tamanho. A função deve retornar o terceiro vetor.
    def ex7():
        a = [44,2,90,42,20,26]
        b = [32,43,108,57,78,20]
        c = a + b
        print(c)

    # Criar um programa que leia um vetor de 10 elementos de inteiro e apresente a soma dos valores que estão nos índices pares do vetor.
    def ex8():
        a = []
        soma = 0
        for i in range(10):
            pos = i+1
            num = int(input(f'Informe o {pos}° numero:\n'))
            a.append(num)
            if i % 2 == 0:
                soma+=num
        print(f'A soma dos valores nas posições pares é: {soma}')

    # Criar um programa que leia um vetor de 16 posições de valores inteiros e troque os 8 primeiros valores pelos 8 últimos valores e vice-versa. Ao final apresentar na tela os dados do vetor obtido.
    def ex9():
        a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        print(f'Antes da alteração:{a}')
        for i in range(8):
            x = a[i+8]
            a[i+8] = a[i]
            a[i] = x 
        print(f'Depois da alteração: {a}')

    # Criar um programa que leia dois vetores de 4 posições de valores inteiros. Criar outro vetor preenchendo-o nas posições pares com os valores do primeiro vetor e nas posições ímpares com os valores do segundo vetor. Apresentar na tela os dados do vetor criado.
    def ex10():
        v1 = []
        v2 = []
        v3 = []
        for i in range(4):
            n = int(input(f'Informe o {i + 1}° valor do vetor 1:'))
            v1.append(n)
        for i in range(4):
            n = int(input(f'Informe o {i + 1}° valor do vetor 2:'))
            v2.append(n)

        for i in range(8):
            if i % 2 == 0:
                v3.append(v1[i//2])
            else:
                v3.append(v2[i//2])

        for i in range(len(v3)): print(i)

    #  Criar um programa que leia uma determinada quantia a ser retirada em um caixa eletrônico e apresente a quantidade mínima de cédulas equivalente. As cédulas são de 50, 20 e 10. Utilizar sempre que possível cédulas de maior valor. O valor da quantia a ser retirada deve ser múltiplo de 10. Guardar em um vetor a quantidade de cada cédula. Apresentar os dados do vetor de cédulas na tela.
    def ex11():
        v = int(input('Qual valor deseja retirar: R$\n'))

        if v % 10 != 0:
            print('Valor invalido')
        else:
            notas = [0,0,0]
        
        for i in range(len(notas)):
            notas[i] = v // (50 if i == 0 else 20 if i == 1 else 10)
            v %= (50 if i == 0 else 20 if i == 1 else 10)
        
        print(f'Notas de R$ 50 --> {notas[0]}\nNotas de R$ 20 --> {notas[1]}\nNotas de R$ 10 --> {notas[2]}')

    








    