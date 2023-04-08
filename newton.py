# Método de Newton
# Lucas Gusmão Valduga 21103505

from math import exp, cos, sin


def calc_f(x):
    return exp(x)-2*cos(x)


def calc_df(x):
    return exp(x)+2*sin(x)


 # [0,2] intervalo que possui a raiz
erro = 10**-8  # precisão
i = 0  # número de iterações
x0 = 2  # estimativa inicial (setada em algum valor do intervalo)
fx0 = calc_f(x0)

while (abs(fx0) > erro):
    i += 1
    xk = x0 - (fx0/calc_df(x0))
    x0 = xk
    fx0 = calc_f(x0)

print(f"Aproximação da raiz: {xk}")
print(f"Precisão: {fx0}")
print(f"numero de iterações: {i}")
