# Lucas Gusmão Valduga
# Exercício 1
# Implementação da função e^x

from math import factorial

sum = 0
terms = int(input("Insira o numero de termos da série (valor de i): "))
x = float(input('insira o valor de x: '))

for i in range(terms):
    sum += (x**i)/float(factorial(i))
    
print(f'e^{int(x)} = {sum}')