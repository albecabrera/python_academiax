numeros = [1, 2, 3 ,4, 5]

for numero in numeros:
    if numero % 2 == 0:
        print(f"El número {numero} es par")
        break
    else: 
        print("No se encontró ningún par")
        