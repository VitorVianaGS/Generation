def somarMultiplos(*num):
    return print(sum(num))

def multiplicarVarios(*num):
    resultado = 1
    for n in num:
        resultado *= n
    return print(resultado)

def ehPar(num):
    if num % 2 == 0:
        return "É par"
    return "É ímpar"

def ehInteiro(num):
    return print(num == int(num))

somarMultiplos(5,10,15)
somarMultiplos(0.5,-4,2)
multiplicarVarios(2,5)
multiplicarVarios(-1,3,2.5)
ehPar(8)
ehPar(5)
ehPar(2.5)
ehInteiro(10)
ehInteiro(-6)
ehInteiro(4.2)