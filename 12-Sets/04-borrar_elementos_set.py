mi_set = {1,2,3,4,5}
mi_set.discard(3)
print(mi_set)

# BORRAR LOS NUMEROS IMPARES DE UN SET
mi_set = {1,2,3,4,5}
mi_set = {x for x in mi_set if x % 2 == 1}
print(mi_set)