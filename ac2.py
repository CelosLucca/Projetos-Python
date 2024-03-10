"""
Lucca Barcelos Cravo
matricula: 202402630775
turma: 8002

"""


#exercicio 1.1


def eq_seg_grau(a, b, c):
    delta = b**2 - 4 * a * c
    raiz1 = (-b + delta**0.5)/ 2 * a
    raiz2 = (- b - delta ** 0.5)/ 2 * a
    return (raiz1, raiz2)

print(eq_seg_grau(1, -5, 6))


#exercicio 1.2


def bissexto(ano):
    ano = ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0
    return ano

print(bissexto(2024))



#exercicio 2

def calcula_salario(valor_hora, num_horas, ifpr):
    salario_liquido = (valor_hora * num_horas) * ifpr
    return salario_liquido

print(calcula_salario(20, 160, 0.275))




