# Exer 1
# Escreva um programa em python que imprima a mensagem: 
# “É PRECISO FAZER TODOS OS ALGORITMOS PARA APRENDER”.

print("É PRECISO FAZER TODOS OS ALGORITMOS PARA APRENDER.")



#Exer 2
# Escreva um programa em python que leia um tempo em segundos 
# e imprima quantas horas, minutos e segundos há neste tempo.

s = float(input("Digite um valor em segundos: "))

m = s / 60
h = m / 60

print(f"{h} h | {m} min | {s} s")



# Exer 3
# 3) Escreva um programa em python que leia um comprimento 
# em centímetros e imprima quantos metros, decímetros e 
# centímetros há neste comprimento.

cm = float(input("Digite um valor em centímetros: "))

dm = cm / 10
m = dm / 10

print(f"{m} m | {dm} dm | {cm} cm")



# Exer 4
# 4) Escreva um programa em python que leia a idade de 
# uma pessoa expressa em anos, meses e dias e escreva a i
# dade dessa pessoa expressa apenas em dias. Considerar ano
# com 365 dias e mês com 30 dias.

idade = int(input("Digite sua idade em anos: "))

mes = idade * 12
dia = idade * 365

print(f"Sua idade em dias: {dia} dias") 



# Exer 5
# Escreva um programa em python que entre com dois números 
# reais e imprima a média aritmética com a mensagem “média” antes 
# do resultado.

x = float(input("Digite primeiro número real: "))
y = float(input("Digite segundo número real: "))

media = (x + y)/2

print(f"Média: {media}")

# Exer 6
# Escreva um programa em python que possa entrar com o saldo 
# de uma aplicação e imprimir o novo saldo, considerando o 
# reajuste de 1%.

saldo = float(input("Digite seu saldo para o reajuste de 1%: "))

reaj = saldo * 1.01

print(f"Seu reajuste foi R${reaj}")

# Exer 7
# Escreva um programa em python que leia número no formato CDU 
# e imprimir invertido: UDC (Exemplo: 123,saíra 321).

digito = int(input("Digite um numero para inverter: "))

unidade = digito % 10
resto = digito // 10

dezena = resto % 10
resto = resto // 10

centena = resto % 10
resto = resto // 10

total = (unidade * 100) +(dezena * 10) + centena

print(f"Seu número invertido é: {total}")



# Exer 8
# Escreva um programa em python que entre com a base e altura 
# de um retângulo e imprimir a seguinte saída:
# perímetro:
# área:
# diagonal:

h = float(input("Digite a altura do retângulo:"))
b = float(input("Digite a base do retângulo: "))

perimetro = (b*2)+(h*2)
area = b * h
diagonal = ((b)**2 + (h)**2)**(1/2)

print(f"perimetro: {perimetro} | área: {area} u² | diagonal: {diagonal} u")



# Exer 9
# Escreva um programa em python que calcule e imprima a área 
# de um triângulo

hTr = float(input("Digite a altura do triângulo:"))
bTr = float(input("Digite a base do triângulo: "))

areaTr = (bTr * hTr)/2

print(f"Sua área é {areaTr} u²")