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

