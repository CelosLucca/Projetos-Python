"""
Lucca Barcelos Cravo
matricula: 202402630775
turma: 8002

"""
def exercicio1(): 
    # exercicio 1: resolva uma equação do segundo grau

    a = int(input("digite o valor do coeficiente a: "))
    b = int(input("digite o valor do coeficiente b: "))
    c = int(input("digite o valor do coeficiente c: "))

    delta = b**2 - 4*a*c
    print("o valor de delta é: ", delta)

    raiz1 = (-b - delta**0.5) / (2*a)
    raiz2 = (-b + delta**0.5) / (2*a)
    print("o valor da raiz1 é: ", raiz1)
    print("o valor de raiz2 é: ", raiz2)



def exercicio2() :
    # exercicio 2: anos bissextos

    ano = int(input("informe o ano: "))
    print((ano%4 == 0) and((ano%400 == 0) or (ano%100 != 0)))


exercicio1()
exercicio2()
    
