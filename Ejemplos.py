# 1 if.py
# Verifica si un número es positivo

numero = 10

if numero > 0:
    print("El número es positivo")


# 2 if_else.py
# Verifica si un número es positivo o negativo

numero = -5

if numero >= 0:
    print("El número es positivo o cero")
else:
    print("El número es negativo")


# 3 ternario.py
# Forma corta de escribir un if-else

edad = 18
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"

print(mensaje)


# 4 if_multiple.py
# Determina la calificación de un estudiante

nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy buena")
elif nota >= 70:
    print("Buena")
else:
    print("Reprobado")


# 5 switch.py
# Simulación de switch usando match-case (Python 3.10 o superior)

opcion = 2

match opcion:
    case 1:
        print("Elegiste la opción 1")
    case 2:
        print("Elegiste la opción 2")
    case 3:
        print("Elegiste la opción 3")
    case _:
        print("Opción no válida")


# 6 while.py
# Cuenta del 1 al 5

contador = 1

while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1


# 7 do_while.py
# Simulación de do-while

contador = 1

while True:
    print(f"Contador: {contador}")
    contador += 1
    if contador > 5:
        break  # Rompe el ciclo cuando la condición se cumple


# 8 for.py
# Recorre una lista

frutas = ["manzana", "banana", "pera"]

for fruta in frutas:
    print("Me gusta la", fruta)
