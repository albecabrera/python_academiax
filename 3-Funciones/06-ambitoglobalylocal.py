# AMBITO LOCAL Y GLOBAL
x = "global"

def foo():
    x ="local" # imprime local pues está dentro de la función
    print(x)
    
foo()
print(x) # Imprime global pues está fuera del alcance (scope)