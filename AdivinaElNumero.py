 # Este es el juego de adivinar el número.

import random
import os
import time

def adivina(x):
  numero_a = random.randint(1, x)
  numero_b = 0
  while numero_a != numero_b:
    #os.system ("clear") 
    numero_b = int(input(f'Adivina un número entre 1 y {x}: '))
    if numero_b < numero_a:
      print("Inténtalo de nuevo, tu número es muy pequeño")
    elif numero_b > numero_a:
      print("Intenta de nuevo, tu número es muy grande")
    #time.sleep(5.0)
  print("Excelente, encontraste el número.")

adivina(100)