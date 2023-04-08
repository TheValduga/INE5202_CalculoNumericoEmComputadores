# Método da Secante
# Lucas Gusmão Valduga 21103505

from math import exp, cos


def calc_f(x):
    return exp(x)-2*cos(x)

 # [0,2] intervalo que possui a raiz
erro = 10**-8  # precisão
i = 0  # número de iterações
x0 = 0  # estimativa inicial (setada no inicio do intervalo)
x1 = 2 # estimativa inicial (setada no fim do intervalo)
fx0 = calc_f(x0)
fx1 = calc_f(x1)

while (abs(fx1) > erro):
    i += 1
    xk = x1 - ((x1-x0)*fx1/(fx1-fx0))
    x0 = x1
    x1 = xk
    fx0 = fx1
    fx1 = calc_f(x1)

print(f"Aproximação da raiz: {xk}")
print(f"Precisão: {fx1}")
print(f"numero de iterações: {i}")
