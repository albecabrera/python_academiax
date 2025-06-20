# ARGUMENTOS ARBITRATIOS
def saludar(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}")
    
saludar("Alberto", "Juan", "Maria")