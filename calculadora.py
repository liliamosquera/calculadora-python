def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def obtener_numero(mensaje):
    try:
        return float(input(mensaje))
    except ValueError:
        raise ValueError("Debes ingresar un número válido")


def calculadora():
    try:
        print("=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. salir")

        opcion = input("Elegí una opción: ")

        a = obtener_numero("Ingresá el primer número: ")
        b = obtener_numero("Ingresá el segundo número: ")

        if opcion == "1":
            resultado = sumar(a, b)
        elif opcion == "2":
            resultado = restar(a, b)
        elif opcion == "3":
            resultado = multiplicar(a, b)
        elif opcion == "4":
            resultado = dividir(a, b)
        else:  

         print("Opción inválida")
    
        return

        print(f"Resultado: {resultado}")

    except ValueError as e:
        print(f"Error: {e}")


calculadora()
