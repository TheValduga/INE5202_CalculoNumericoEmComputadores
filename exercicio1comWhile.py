# Lucas Gusmão Valduga
# Exercício 1 com while
# Implementação da função e^x

from math import factorial  

sum = 0
x = float(input('insira o valor de x: '))
err = 0.0
i = 0
real = 7.389056098930649

while err > 0.000000000000001 and err != 0: 
    sum += (x**i)/float(factorial(i))
    i += 1
    err = real - sum
    
print(f'e^{int(x)} = {sum}')
    