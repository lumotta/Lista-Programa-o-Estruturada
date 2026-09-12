# Exer 1
# Escreva um programa em Python para ler um valor do teclado e 
# escrever (na tela) o seu antecessor e sucessor.

x = int(input("Digite um valor: "))

suc = x + 1
ant = x - 1

print(f"O valor: {x} tem antecessor = {ant} e tem sucessor = {suc}")


# Exer 2
# Escreva um programa em Python para ler as dimensões de um retângulo
# (base e altura), calcular e escrever a área do retângulo.

b = float(input("Digite a base: "))
h = float(input("Digite a altura: "))

area = b * h

print(f"A sua área é: {area} u²")

# Exer 3
# Escreva um programa em Python que leia a idade de uma pessoa 
# expressa em anos, meses e dias e escreva a idade dessa pessoa 
# expressa apenas em dias. Considerar ano com 365 dias e
# mês com 30 dias.

idade = int(input("Digite sua idade: "))

mes = idade * 12
dia = idade * 365

print(f"Sua idade em dias: {dia} dias")

# Exer 4
#Escreva um programa em Python para ler o salário mensal atual 
# de um funcionário e o percentual de reajuste. 
# Calcular e escrever o novo salário.

salario = float(input("Digite seu salário para o reajuste: "))
taxaReaj = float(input("Digite em porcentegem a taxa de reajuste: "))

reajuste = salario * ((taxaReaj/100) + 1)

print(f"O reajuste foi de R${salario} para R${reajuste}")

# Exer 5
# Escreva um programa em Python que leia três notas de um aluno, 
# calcule e escreva a média final deste aluno. Considerar que a 
# média é ponderada e que o peso das notas é 2, 3 e 5.
# Fórmula para cálculo da média final é:
# MediaFinal = (n1*2 + n2*3 + n3 *5)/10

n1 = float(input("Digite nota 1: "))
n2 = float(input("Digite nota 2: "))
n3 = float(input("Digite nota 3: "))

mf = (n1*2 + n2*3 + n3 *5)/10

print(f"A média poderada é: {mf}")

# Exer 6
# Escreva um programa em Python que receba um valor em segundos 
# e transforem este valor, no valor correspondente em HH:MM:SS

seg = int(input("Digite um valor em segundos: "))

mi = seg // 60
h = mi // 60
mi = mi % 60
seg = seg % 60

print(f"{h:02d}:{mi:02d}:{seg:02d}")


# Exer 7
# Escreva um programa em Python que leia um valor e escreva a mensagem 
# É MAIOR QUE 10! Se o valor lido for maior que 10, caso 
# contrário escrever NÃO É MAIOR QUE 10!

num = float(input("Digite um valor para ver se é maior que 10: "))

if (num > 10):
    print("É MAIOR QUE 10!")
else:
    print("NÃO É MAIOR QUE 10!")
    


# Exer 8
# 8) Escreva um programa em Python que leia um valro e escreva 
# se é positivo ou negativo, considere o valor zero como positivo.

valor = float(input("Digite um valor para verificar se é positivo ou negativo: "))

if (valor >= 0):
    print("Positivo!")
else:
    print("Negativo!")
    


# Exer 9
# Escreva um programa em Python que leia o ano atual e o ano de 
# nascimento de uma pessoa. Escreva uma mensagem que diga se 
# ela poderá ou não votar este ano (não é necessário considerar o mês).

anoAtual = 2026
anoUser = int(input("Digite seu ano de nascimento: "))

poVoto = anoAtual - anoUser

if (poVoto >= 16 and poVoto < 18):
    print("Seu voto é opcional")
elif (poVoto > 18):
    print("Seu voto é obrigatório")
else:
    print("Você não pode votar")
    


# Exer 10
# Escreva um programa em Python para ler: quantidade atual em 
# estoque, quantidade máxima em estoque e quantidade mínima em 
# estoque de um produto. Calcular e escrever a quantidade média 
# (quantidade média = (quantidade máxima + quantidade mínima)/2). 
# Se a quantidade em estoque for maior ou igual a quantidade média 
# escrever a mensagem 'Não efetuar compra', senão escrever a 
# mensagem 'Efetuar compra'.

estoqueAtual = int(input("Digite a quantidade atual em estoque: "))
estoqueMax = int(input("Digite a quantidade máxima em estoque: "))
estoqueMin = int(input("Digite a quantidade mínima em estoque: "))

estoqueMedia = (estoqueMax + estoqueMin)/2

if (estoqueAtual >= estoqueMedia):
    print("Não Efetuar Compra!")
else:
    print("Efetuar Comprar!")
    


# Exer 11
#Escreva um programa em Python que leia o valor de um ano e i
# nforma se este ano é bissexto ou não. Obs: Um ano é bissexto 
# se ele for divisível por 400 ou se ele for divisível por 4 e não por 100.

ano = int(input("Digite um ano para verificar se é um ano bissexto: "))

if (ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")



# Exer 12
# Ler um valor e escrever se é positivo, negativo ou zero.

aNum = float(input("Digite um valor para verificar se é positivo, negativo ou zero: "))

if (aNum > 0):
    print("Positivo!")
elif (aNum < 0):
    print("Negativo!")
else:
    print("É Zero!")
    
    
    
# Exer 13
# Escreva um programa em Python que leia 3 valores (considere 
# que não serão informados valores iguais) e escrever o maior deles.

i = float(input("Digite 1° valor: "))
j = float(input("Digite 2° valor: "))
k = float(input("Digite 3° valor: "))

if (i > j and i > k and j > k):
    print(f"{i} > {j} > {k}")
elif (i > j and i > k and k > j):
    print(f"{i} > {k} > {j}")
elif (j > i and j > k and i > k):
    print(f"{j} > {i} > {k}")
elif (j > k and j > i and k > i):
    print(f"{j} > {k} > {i}")
elif (k > i and k > j and i > j):
    print(f"{k} > {i} > {j}")
elif (k > j and k > j and j > i):
    print(f"{k} > {j} > {i}")
else:
    print("Valor inválido")


# Exer 14
#  Escreva um programa em Python que leia 3 valores (considere 
# que não serão informados valores iguais) e escrever a soma dos 2 maiores.

i = float(input("Digite 1° valor: "))
j = float(input("Digite 2° valor: "))
k = float(input("Digite 3° valor: "))

if (i > j and i > k and j > k):
    print(f"{i} > {j} > {k}")
    print(f"{i} + {j} = {i + j}")
elif (i > j and i > k and k > j):
    print(f"{i} > {k} > {j}")
    print(f"{i} + {k} = {i + k}")
elif (j > i and j > k and i > k):
    print(f"{j} > {i} > {k}")
    print(f"{j} + {i} = {j + i}")
elif (j > k and j > i and k > i):
    print(f"{j} > {k} > {i}")
    print(f"{j} + {k} = {j + k}")
elif (k > i and k > j and i > j):
    print(f"{k} > {i} > {j}")
    print(f"{k} + {i} = {k + i}")
elif (k > j and k > i and j > i):
    print(f"{k} > {j} > {i}")
    print(f"{k} + {j} = {k + j}")
else:
    print("Valor inválido")



# Exer 15
# 15) Escreva um programa em Python que leia 3 valores (A, B e C) 
# representando as medidas dos lados de um triângulo e escrever se 
# formam ou não um triângulo. OBS: para formar um triângulo, o valor 
# de cada lado deve ser menor que a soma dos outros 2 lados.

_a = float(input("Digite lado A: "))
_b = float(input("Digite lado B: "))
_c = float(input("Digite lado C: "))

if (
    _a + _b > _c
    and _a + _c > _b
    and _b + _c > _a
):
    print("Formam um Triângulo")
else:
    print("Ñ Formam um Triângulo")


# Exer 16
# Escreva um algoritmo que leia as idades de 2 homens e de 2 mulheres 
# (considere que as idades dos homens serão sempre diferentes entre si, 
# bem como as das mulheres). Calcule e escreva a soma das idades do homem 
# mais velho com a mulher mais nova, e o produto das idades do homem mais 
# novo com a mulher mais velha

h1 = int(input("Digite a Idade do homem 1: "))
h2 = int(input("Digite a Idade do homem 2: "))
m1 = int(input("Digite a Idade do mulher 1: "))
m2 = int(input("Digite a Idade do mulher 2:"))


if h1 > h2:
    if m1 > m2:
        print(f"A soma das idades do homem mais velho com a mulher mais nova: {h1 + m2}")
        print(f"O produto das idades do homem mais novo com a mulher mais velha: {h2 * m1}")
    else:
        print(f"A soma das idades do homem mais velho com a mulher mais nova: {h1 + m1}")
        print(f"O produto das idades do homem mais novo com a mulher mais velha: {h2 * m2}")

else:
    if m1 > m2:
        print(f"A soma das idades do homem mais velho com a mulher mais nova: {h2 + m2}")
        print(f"O produto das idades do homem mais novo com a mulher mais velha: {h1 * m1}")
    else:
        print(f"A soma das idades do homem mais velho com a mulher mais nova: {h2 + m1}")
        print(f"O produto das idades do homem mais novo com a mulher mais velha: {h1 * m2}")