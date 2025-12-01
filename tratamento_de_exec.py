# [Padrão] Imports [01] <tratamento com TRy e except>

try:
    valor1 = int(input("Digite o valor número 1: "))
    valor2 = int(input("Digite o valor número 2: "))

    soma = valor1 + valor2

    if soma >= 50:
        print (f"Valor maior que 50 ou igual a 50, o valor é {soma}")
    else:
        print(f"Valor menor que 50, o valor é {soma}")

except ValueError:
    print("Você digitou LETRAS BOBÃO")

finally:
    print("Código finalizado.")
    

