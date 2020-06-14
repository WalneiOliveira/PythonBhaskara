#Fórmula de Bhaskara
# entrada:
a = float(input('digite o valor para a diferente de zero: '))
b = float(input('digite o valor de b: '))
c = float(input('digite o valor de c: '))

#Cálculo do Delta:
import math
delta = b**2 - (4 * a * c)


#Condições das raízes:
if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print('a raiz desta equação é', raiz1)
if delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print('as raízes da equação são', raiz2, 'e', raiz1)
if delta < 0:
    print('esta equação não possui raízes reais')





