#Crie um porgrama que leia  3 valores e mostre qual é o maior e o menor 

valores = []

num1 = int(input("Digite o primeiro numero "))
num2 = int(input("Digite o segundo numero "))
num3 = int(input("Digite o terceiro numero "))

valores.append (num1)
valores.append (num2)
valores.append (num3)

maior = max(valores)
menor = min(valores)

valores.remove(maior)
meio = max(valores)

print (f"Numero maior = {maior}| O do meio é = {meio}| o menor = {menor}")