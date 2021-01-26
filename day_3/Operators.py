import math

# Day 3: 30 Days of python programming

# A
age            = int(27)
height         = 1.80
complex_number = 10j
print('age', type(age), age)
print('height', type(height), height)
print('complex_number', type(complex_number), complex_number)

# B
print('Calcular area de um triangulo:')
base   = float(input('Informe a base: '))
height = float(input('Informe a altura: '))
area   = 0.5 * base * height
print('A area do triangulo é:', area)

# C
print('Calcular o perimetro de um triangulo:')
side_a = float(input('Lado A: '))
side_b = float(input('Lado B: '))
side_c = float(input('Lado C: '))
perimeter = side_a + side_b + side_c
print('O perimetro do pedido é:', perimeter)

# D
print('Calcular a area de um retangulo')
length = float(input('Insira a comprimento: '))
width  = float(input('Insira a largura: '))
area   = length * width
print('Area do retangulo:', area)
perimeter = length + width
print('Perimetro do retangulo:', perimeter)

# E
print('Calcular a area de um circulo')
radius = float(input('Insira o raio: '))
area   = math.pi * (radius ** 2)
print('Area do ciruclo:', area)
circumference = 2 * math.pi * radius
print('Circunferencia do circulo:', circumference)

# F
print(not len('python') == len('jargon'))
print('on' in 'python')
print('on' in 'jargon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'dragon' and 'on' not in 'python')
print(str(float(len('python'))))

# G
number = int(input('Insira o valor: '))
print((number % 2) == 0)

# H
print('10' is 10)
print(int(float('9.8')) is 10)

# I
hours = int(input('Insira quantas horas vc trabalha por dia: '))
rate  = float(input('Insira quanto ganha por hora: R$'))
earn  = hours * rate
print(f'Voce ganha R${earn} por dia')

# J
life_length = 60 * 60 * 24 * 365 * 100
age = int(input('Sua idade: '))
age_in_seconds = 60 * 60 * 24 * 365 * age
remain = life_length - age_in_seconds
print(f'vc ainda tem {remain} segundos de vida')

print(
'''
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
'''
)