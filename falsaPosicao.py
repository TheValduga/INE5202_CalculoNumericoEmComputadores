# Método da falsa posição
# Lucas Gusmão Valduga 21103505

from math import exp, cos

def calc_f(x):
    return exp(x)-2*cos(x)

while True:
    a = float(input("\nInsira o valor de A no intervalo: "))
    b = float(input("\nInsira o valor de B no intervalo: "))

    fa = calc_f(a)
    fb = calc_f(b)

    if (fa * fb < 0):
        print()
        break
    else:
        print("\nNão há raiz dentro do intervalo (a,b), insira os valores novamente\n")

erro = 10**-15  # precisão
fxk = 1 # função calculada onde a reta cruza o eixo x
i = 0  # número de iterações

while (abs(fxk) > erro):
    i += 1
    xk = a-((fa*(b-a))/(fb-fa))
    fxk = calc_f(xk)
    
    if (fa * fxk < 0):
        b = xk
        fb = fxk
    else:
        a = xk
        fa = fxk

print(f"Aproximação da raiz: {xk}")
print(f"Precisão: {fxk}")
print(f"numero de iterações: {i}")
