# Método da bisseção
# Lucas Gusmão Valduga 21103505

from math import exp,cos

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

erro = 10**-15 # precisão
fxm = 1 # função calculada no x médio
k = 0 # número de iterações

while (abs(fxm) > erro):
    k += 1
    xm = (a+b)/2
    fxm = calc_f(xm)
    
    if (fa * fxm < 0):
        b = xm
        fb = fxm
    else:
        a = xm
        fa = fxm
    
print(f"Aproximação da raiz: {xm}")
print(f"Precisão: {fxm}")
print(f"numero de iterações: {k}")