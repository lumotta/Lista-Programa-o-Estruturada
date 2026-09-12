# Exer 1
# Faça um programa que receba dois números e mostre qual deles é o maior

a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))

if (a > b):
    print(f"{a} > {b}")
else:
    print(f"{b} > {a}")

# Exer 2
# Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.

num = int(input("Digite para verificar se ele é par ou impar: "))

if (num % 2 == 0):
    print(f"{num} é par")
else:
    print(f"{num} é impar")

# Exer 3
# Escreva um programa que, dado dois números inteiros, mostre na tela o maior deles, 
# assim como a diferença existente entre ambos.

numA = int(input("Digite o valor A: "))
numB = int(input("Digite o valor B: "))

if (numA > numB):
    print(f"{numA} > {numB}")
    print(f"{numA} - {numB} = {numA -numB}")
else:
    print(f"{numA} > {numB}")
    print(f"{numB} - {numA} = {numB -numA}")

# Exer 4
# Faça um programa que receba dois números e mostre o maior. Se por acaso, os 
# dois números forem iguais, imprima a mensagem de “Números iguais”.

f = float(input("Digite o valor I: "))
g = float(input("Digite o valor J: "))

if (f > g):
    print(f"{f} > {g}")
elif (g > f):
    print(f"{g} > {f}")
else:
    print(f"{f} = {g}")

# Exer 5
# Faça um programa que leia duas notas de um aluno, verifique se as notas são válidas 
# e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, 
# um valor entre 0.0 e 10.0. Caso a nota não seja um valor válido, deve ser informado 
# ao usuário, e o programa deve ser encerrado.

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

if (
    n1 <= 10 
    and n1 >= 0
    and n2 <= 10
    and n2 >= 0
):
    media = (n1 + n2) / 2
    print(f"A média é {media}")
else:
    print("Valor da nota inválido")

# Exer 6
# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a 
# prestação for maior que 20% do salário, imprima: “Empréstimo não concedido”, 
# caso contrário, imprima: “Empréstimo concedido”.

salario = float(input("Digite salário do Trabalhador: "))
v_prstacao = float(input("Digite o valor da prestação: "))

if (v_prstacao > salario * 0.2):
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido")

# Exer 7
# Faça um programa que calcule a média ponderada das notas e três avaliações. 
# A primeira e a segunda avaliação têm peso 1 e a terceira tem peso 2. Ao final da 
# execução do cálculo da média, imprimir a média do aluno e indicar se o aluno foi 
# aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

mediaP = ((nota1 + nota2) + nota3) / 4

if (mediaP >= 60):
    print(f"Aluno a média foi {mediaP} e está aprovado!")
else:
    print(f"Aluno a média foi {mediaP} e está reprovado!")


# Exer 8
# Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas 
# (as básicas, por exemplo). O usuário escolherá uma das opções e o programa então 
# pedirá dois valores numéricos e realizará a operação, mostrando o resultado e finalizando o programa.

num1 = float(input("Digite o primeiro valor: "))
op = input("Digite o sinal da operação(+, -, *, /): ")
num2 = float(input("Digite o segundo valor: "))

match (op):
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if (num2 != 0):
            print(num1 / num2)
        else:
            print("Ñ existe divisão por 0")
    case _:
        print("Valor inválido")

# Exer 9
# Faça um programa que receba três números e os imprima em ordem crescente.

i = float(input("Digite 1° valor: "))
j = float(input("Digite 2° valor: "))
k = float(input("Digite 3° valor: "))

if (i > j and i > k and j > k):
    print(f"{k} < {j} < {i}")
elif (i > j and i > k and k > j):
    print(f"{j} < {k} < {i}")
elif (j > i and j > k and i > k):
    print(f"{k} < {i} < {j}")
elif (j > k and j > i and k > i):
    print(f"{i} < {k} < {j}")
elif (k > i and k > j and i > j):
    print(f"{j} < {i} < {k}")
elif (k > j and k > i and j > i):
    print(f"{i} < {j} < {k}")
else:
    print("Valores iguais ou inválidos")

# Exer 10
# Faça um programa que leia o código do produto escolhido do cardápio de uma 
# lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. 
# Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete 
# segue o padrão abaixo:
# Especificação Código Preço
# Cachorro Quente 100 R$ 1,20
# Bauru Simples 101 R$ 1,30
# Bauru com Ovo 102 R$ 1,50
# Humburguer 103 R$ 1,20
# Cheeseburguee 104 R$ 1,70
# Suco 105 R$2,20
# Refri 106 R$1,00

cardapio = [
    (100, "Cachorro Quente", 1.20),
    (101, "Bauru Simples", 1.30),
    (102, "Bauru com Ovo", 1.50),
    (103, "Hambúrguer", 1.20),
    (104, "Cheeseburger", 1.70),
    (105, "Suco", 2.20),
    (106, "Refri", 1.00)
]

for codigo, especificacao, preco in cardapio:
    print(f"{codigo:<8} | {especificacao:<20} | R$ {preco:>5.2f}")

cd = int(input("Digite o codigo do produto: "))
qntPro = int(input("Digite o quantidade do produto: "))

match (cd):
    case 100:
        print(f"O valor pago foi de R${qntPro * 1.2}")
    case 101:
        print(f"O valor pago foi de R${qntPro * 1.3}")
    case 102:
        print(f"O valor pago foi de R${qntPro * 1.5}")
    case 103:
        print(f"O valor pago foi de R${qntPro * 1.2}")
    case 104:
        print(f"O valor pago foi de R${qntPro * 1.7}")
    case 105:
        print(f"O valor pago foi de R${qntPro * 2.2}")
    case 106:
        print(f"O valor pago foi de R${qntPro * 1}")