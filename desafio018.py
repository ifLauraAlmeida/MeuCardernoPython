import math as mt

angulo = float(input("Digite o ângulo: "))
angulo_rad = mt.radians(angulo)
seno = mt.sin(angulo_rad)
cosseno = mt.cos(angulo_rad)
tangente = mt.tan(angulo_rad)

print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, seno))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, cosseno))
print("O ângulo de {} tem a TANGENTE de {:.2f}".format(angulo, tangente))