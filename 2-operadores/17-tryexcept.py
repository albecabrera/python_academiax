try: 
    numero = input(("Ingresa un número: "))
    print(f'El número es {numero}')
except ValueError:
    print('Debes ingresar un número válido')
    
# En caso que se haga una división por cero pasa lo siguiente:

try:
    x = 5 / 0
except ZeroDivisionError:
    print("No se puede dividir un número por cero")