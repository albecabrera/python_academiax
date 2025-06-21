persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid"
}

valor = persona.setdefault("ciudad")
valor = persona.setdefault("municipio", "El Pinar")
print(valor)