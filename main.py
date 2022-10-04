import numpy as np

#função que vaai nos ajudar com a entrade de dados
def entrada_dados():
    coeficiente = quantidade = eval(input("Digite o valor do coeficiente: "))
    return coeficiente

#função que vai definir o delta
def calc_delta(a,b,c):
    delta = b*b-4*a*c
    return delta

#função que de fato calcula as raízes e retorna as mensagens pro usuário
def calcular_raizes(a,b,c,delta):
    if(delta < 0):
        resultado = 'A equação não possui raízes nos números reais'
    elif(delta == 0):
        x = -b / (2 * a)
        resultado = f'A equação só possui uma raiz:{x}'
    else:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        resultado = f'A equação possui as raízes: {x1}, {x2}'
    return resultado

a = entrada_dados()
b = entrada_dados()
c = entrada_dados()

delta = calc_delta(a,b,c)

resultado = calcular_raizes(a,b,c,delta)
print(resultado)


