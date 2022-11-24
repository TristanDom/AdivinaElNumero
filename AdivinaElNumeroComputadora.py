 # Este es el juego de adivinar el número.

import random
#import os
#import time

def adivina(x):
  min = 1
  max = x
  retroA = ''
  adivina = 0
  print("Instrucciones digita 'b' si el número es menor, 'a' mayor o 'c' si he adivinado el número que estás pensando:")
  while retroA != 'c':
    if min != max:
      adivina = random.randint(min, max)
    else:
      adivina = min
    retroA = input(f"""Estás pensando en el número {adivina}?: """)
    if retroA == "a":
      print(f"El número el cual estás pensando es mayor a {adivina}")
      max = adivina - 1
    elif retroA == "b":
      print(f"El número el cual estás pensando es menor a {adivina}")
      min = adivina + 1


  print(f"El número el cual estabas pensando es {adivina} ¿cierto? B)")
      

adivina(100)