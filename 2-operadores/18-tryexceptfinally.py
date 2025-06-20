try:
    x = 5 / 0
except ZeroDivisionError:
    print("No se puede dividir un número por cero")
finally:
    print("Se ejecutará siempre")
    