# Programa para identificar la longitud de una palabra ingresada por el usuario.

    #Ciclo while para validar que se escriba algo.
while True:
    palabra = input("Por favor ingresa una palabra: ")
    # Uso de la función "len" para contar la longitud de la cadena
    if len(palabra) == 0:
        print("¿Qué pasó papi? No tecleaste algo.")
    else:
        #Uso de la sentencia "break" para romper el ciclo while
        break
    #Ciclo while para validar que la palabra contenga entre 4 y 8 letras.
while True:
    if len(palabra) < 4:
        if len(palabra) == 1:
            print(f"Hacen falta letras. Sólo tiene una letra. (Eso no es una palabra xD)")
        else:
            print(f"Hacen falta letras. Sólo tiene {len(palabra)} letras.")
    elif len(palabra) > 8:
        print(f"Oye, Tranquilo viejo, sobran letras. Tiene {len(palabra)} letras.")
    else:
        print("Palabra correcta.")
        break
    palabra = input("Ingresa nuevamente una palabra: ")

#######################################################################################################

# PROGRAMA PARA ENCONTRAR EL CUADRANTE CON LOS DATOS INTRODUCIDOS POR EL USUARIO
# Lista de cuadrantes
cuadrantes = ["I", "II", "III", "IV"]

abscisa = int(input("Ingresa el valor de X: "))
ordenada = int(input("Ingresa el valor de Y: "))

coordenada = [abscisa, ordenada]
# Condicionales
if coordenada[0] == 0:
    if coordenada[1] == 0:
        cuadrante = "en el origen"
    elif coordenada[1] < 0:
        cuadrante = "entre el cuadrante " + cuadrantes[2] + " y el cuadrante " + cuadrantes[3]
    elif coordenada[1] > 0:
        cuadrante = "entre el cuadrante " + cuadrantes[0] + " y el cuadrante " + cuadrantes[1]
elif coordenada[1] == 0:
    if coordenada[0] < 0:
        cuadrante = "entre el cuadrante " + cuadrantes[1] + " y el cuadrante " + cuadrantes[2]
    elif coordenada[0] > 0:
        cuadrante = "entre el cuadrante " + cuadrantes[0] + " y el cuadrante " + cuadrantes[3]
elif coordenada[0] > 0:
    if coordenada[1] > 0:
        cuadrante = "en el cuadrante " + cuadrantes[0]
    elif coordenada[1] < 0:
        cuadrante = "en el cuadrante " + cuadrantes[3]
elif coordenada[0] < 0:
    if coordenada[1] > 0:
        cuadrante = "en el cuadrante " + cuadrantes[1]
    elif coordenada[1] < 0:
        cuadrante = "en el cuadrante " + cuadrantes[2]
print(f"El punto se encentra {cuadrante}.")



