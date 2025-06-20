lenguaje = input("¿Qué lenguaje de programación deseas aprender?")

match lenguaje:
    case "JS":
        print("Te puedes convertir en desarrollador web.")
    case "Python":
        print("Te puedes convertir en científico de datos.")
    case "PHP":
        print("Te puedes convertir en desarrollador backend")
    case "Java":
        print("Te puedes convertir en maestro de informática")
    case _:
        print("El lenguaje no importa. Tuú puedees hacerlo!")
        