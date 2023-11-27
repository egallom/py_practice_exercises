import math

# Ejercicio 1
# Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos es múltiplo del otro.

def es_multiplo(num1, num2):
    num1 = int(input("Ingresa un número entero, por favor: "))
    num2 = int(input("Ingresa otro número entero, por favor: "))

    if num1 == 0 or num2 == 0:
        print("Cero es múltiplo de todos los números.")
    elif num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    elif num2 % num1 == 0:
        print(f"{num2} es múltiplo de {num1}.")
    else:
        print(f"{num1} NO es múltiplo de {num2} y viceversa.")

# es_multiplo(num1, num2)


# Ejercicio 2
# Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.

def calc_temp(temp_max, temp_min):
    temp_prom = (temp_max + temp_min)/2
    return temp_prom

# result = calc_temp(20, 10)
# print(f"La temperatura promedio es: {result}")


# Ejercicio 3
# Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. 
# El programa pedirá el número de días que se van a introducir.

def main():
    num_dias = int(input("Ingrese el número de días: "))

    for dia in range(1, num_dias + 1):
        temp_max = float(input(f"Ingrese la temperatura máxima del día {dia}: "))
        temp_min = float(input(f"Ingrese la temperatura mínima del día {dia}: "))

        resultado = calc_temp(temp_max, temp_min)
        print(f"La temparatura promedio del día {dia} fue de: {resultado}.")

# main()


# Ejercicio 4
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo.

def calcular_max_min(lista):
    if not lista:
        return "La lista está vacía"
    
    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if (numero > maximo):
            maximo = numero
        elif (numero < minimo):
            minimo = numero
    
    return (f"El número máximo es: {maximo}.\nEl número mínimo es: {minimo}.")
    
# resultado = calcular_max_min([2, 3, 1, 4, 5])
# print(resultado)


# Ejercicio 5
# Diseñar una función que calcule el área y el perímetro de una círculo.

def calcular_circulo(radio):
    pi = math.pi
    area_circulo = round(pi*radio*radio, 2)
    perimetro_circulo = round(2*pi*radio, 2)

    return(f"El área del círculo es: {area_circulo}.\nEl perímetro del círculo es: {perimetro_circulo}.")

# resultado = calcular_circulo(5)
# print(resultado)


# Ejercicio 6
# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.

def login(usuario, contrasena):
    return usuario == "usuario1" and contrasena == "asdasd"

# resultado = login("usuario1", "asdasd")
# print(resultado)


# Ejercicio 7
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

intentos_maximos = 3
intento_numero = 0

# for intento in range(intentos_maximos):
#     usuario = input("Ingrese el nombre de usuario: ")
#     contrasena = input("Ingrese la contraseña: ")

#     if login(usuario, contrasena):
#         print("¡Inicio de sesión exitoso!")
#         break
#     else:
#         intento_numero += 1
#         print(f"Inicio de sesión fallido. Dispone de {intentos_maximos - intento_numero} intentos más.")
# else:
#     print("Su usuario bloqueado ha sido bloqueado.")


# Ejercicio 8
# Crear una función que permita calcular el factorial de un número

def calcular_factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = 5
resultado_factorial = calcular_factorial(numero)
# print(f"El factorial de {numero} es: {resultado_factorial}")
