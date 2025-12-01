#Criar um prorgrama que pense em um numero de 1 a 5 e você adivinhe qual é
import random
from random import randint
import time

numero_aleatorio = randint(1 , 5)

tentativa = int(input("Digite o Número de 1 a 5: "))
print('HUMMM SERÁ QUE VOCÊ ACERTOU??....\n')
time.sleep(3)

if tentativa == numero_aleatorio:
    print ("Você acertou")
else:
    print ("Você errou, tente novamnte")

print (f"O número sorteado era {numero_aleatorio}")