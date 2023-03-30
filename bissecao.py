from math import exp,sin

def calc_f(x):
    return exp(x)*sin(x)-1

while True:
    a = float(input("\nInsira o valor de A no intervalo: "))
    b = float(input("\nInsira o valor de B no intervalo: "))
    
    fa = calc_f(a)
    fb = calc_f(b)
    
    if (fa * fb < 0):
        print()
        break
    else:
        print("Não há raiz dentro do intervalo (a,b), insira os valores novamente\n")

erro = 10**-16 # precisão
xm = (a+b)/2 # x médio de (a,b)
fxm = calc_f(xm) # função calculada no x médio
k = 0 # número de iterações

while (abs(fxm) > erro):
    if (fa * fxm < 0):
        b = xm
        fb = fxm
    else:
        a = xm
        fa = fxm
        
    k += 1
    xm = (a+b)/2
    fxm = calc_f(xm)
    
print(f"Aproximação da raiz: {xm}")
print(f"Precisão: {fxm}")
print(f"numero de iterações: {k}")