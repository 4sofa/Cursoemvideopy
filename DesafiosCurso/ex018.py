import math

angulo = float(input('Digite o ângulo: '))

# Convertendo de graus para radianos

angulo_radiano = math.radians(angulo)

# Calculando
cos = (math.cos(angulo_radiano))
seno = (math.sin(angulo_radiano))
tan = (math.tan(angulo_radiano))
print('O valor do cosseno é: {:.2f}\nO valor do seno é: {:.2f}\nO valor da tangente é: {:.2f}'.format(cos, seno,
                                                                                                      tan))
