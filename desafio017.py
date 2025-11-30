# A soma do quadrado dos catetos é igual ao quadrado da hipotenusa.
import math as mt
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = mt.hypot(co, ca)

print("A hipotenusa vai medir {:.2f}".format(hi))

hi = (co**2 + ca**2) ** (1/2)
print("A hipotenusa vai medir {:.2f}".format(hi))

hi = mt.sqrt(co**2 + ca**2)
print("A hipotenusa vai medir {:.2f}".format(hi))

hi = mt.pow(co,2) + mt.pow(ca,2)
hi = mt.sqrt(hi)
print("A hipotenusa vai medir {:.2f}".format(hi))
