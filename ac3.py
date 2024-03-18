"""
Lucca Barcelos Cravo
matricula: 202402630775
turma: 8002

"""

# Exercício 1: triângulos

def determina_tipo_triangulo(l1, l2, l3):
    if l1 + l2 < l3 or l1 + l3 < l2 or l2 + l3 < l1:
        print("Não é um triângulo")
    elif  l1 == l2 == l3:
        print("Equilátero")
    elif l1 != l2 != l3:
        print("Escaleno")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Isóceles")
    
    return determina_tipo_triangulo


print(determina_tipo_triangulo(4, 4, 4))
print(determina_tipo_triangulo(2, 4, 4))
print(determina_tipo_triangulo(3, 4, 5)) 
print(determina_tipo_triangulo(1, 1, 4)) 


# Exercício 2: dia da semana

def dia_semana(num):
    if num == 1:
        return "Domingo"
    elif num == 2:
        return "Segunda-Feira"
    elif num == 3:
        return "Terça-Feira"
    elif num == 4:
        return "Quarta-Feira"
    elif num == 5:
        return "Quinta-Feira"
    elif num == 6:
        return "Sexta-Feira"
    elif num == 7:
        return "Sábado"
    else:
        return ""
    

    
# Exercício 3: calculadora simples
        
print(dia_semana(2))
print(dia_semana(6)) 
print(dia_semana(7)) 
print(dia_semana(9))


def soma(n1,n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1 / n2

def calculadora():
    n1 = float(input("Informe um número: "))
    n2 = float(input("Informe outro número: "))
    operacao = input("Informe a operação: ")
    if operacao == "soma":
        print(soma(n1, n2))
    elif operacao == "subtração":
        print(subtracao(n1, n2))
    elif operacao == "multiplicação":
        print(multiplicacao(n1, n2))
    elif operacao == "divisão":
        print(divisao(n1,n2))
    else:
        print ("operação inválida")

calculadora()





        
     

                           
    

    

    







