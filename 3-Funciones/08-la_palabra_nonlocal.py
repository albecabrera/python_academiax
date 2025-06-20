x = 5

def funcion_externa():
    x = 10
    
    def funcion_interna():
        nonlocal x
        x = 1
        print("Función interna:", x)
        
    funcion_interna()
    print("Función externa", x)
funcion_externa()
print("Global:", x)
