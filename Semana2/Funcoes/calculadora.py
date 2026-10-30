def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num1 != 0 or num2 != 0:
        return num1 / num2

operador = ""

while operador != "+ - * /":

    num1 = float(input("Primeiro número: "))
    num2 = float(input("Segundo número: "))
    operador = input("Operador(+ - * /): ")

    if operador == "+":
        print(somar(num1, num2))
    elif operador == "-":
        print(subtrair(num1, num2))
    elif operador == "*":
        print(multiplicar(num1, num2))
    elif operador == "/":
        if num1 != 0 and num2 != 0:
            print(dividir(num1, num2))
        else:
            print("Não é possivel dividir por 0")
    else:
        print("Operador inválido")

###############################################

# Calculadora Aprimorada

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