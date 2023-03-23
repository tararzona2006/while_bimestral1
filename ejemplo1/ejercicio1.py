# Bucle while

import math

numero = int(input("digite un número: "))

while numero < 0:
    print("error -> debería ser un número positivo")
    numero = int(input("digite un número: "))

print(f"/su raíz cuadrada de, numero, es: {(math.sqrt(numero)):.2f} ")





