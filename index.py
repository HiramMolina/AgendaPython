def suma():
            print("SUMA:")
            print("Ingrese 2 numeros para sumarlos.")
            while True:
                try:
                    n1 = int(input("Numero 1: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")
            while True:
                try:
                    n2 = int(input("Numero 2: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")

            res = n1+n2
            return res

def sumaTuneada():
    print("SUMA:")
    print("Ingrese numeros para sumarlos, para confirmar, deje en blanco.")
    total = 0 #El total inicia en 0 para poder sumarle valor despues

    while True: #MIENTRAS no se salga del bucle, será TRUE
        entrada = input("Ingrese un numero: ") #Se solicita un input, el cual se asignará a "ENTRADA". Ej: 1
        if entrada == "": #Si la entrada se queda en blanco...
             break        #... Se rompe el if
        try:              #Mientras no se rompa el if, intenta la siguiente operación.
             numero = int(entrada) # Se convierte en INT la "ENTRADA", para asignarlo a la variable "NUMERO"
             total += numero       # El total, el cual era 0, va a sumarse a si mismo el valor de NUMERO, por cada iteración.
                                    # ES DECIR, cada que el if no se quede en blanco, se va a ingresar el nuevo valor de numero en esa iteración.
                                    # Suponiendo que ingresa 1, 2 y 5, se suma primero 0 = 0 + 1 lo que resulta en numero = 1, 
                                    # despues 1 = 1 + 2 da igual a 3, y despues 3 = 3 + 5, hasta que el if se quede en  blanco y entre el BREAK que ignora el if.

        except ValueError: # Si el valor ingresado no es int, va a brincar el print de excepción.
             print("Ingrese un numero o deje un espacio en blanco.")

    return total #El return de sumaTuneada es lo que en la función termina con el nombre "Total" cosa que no interfiere con el codigo posteriormente, ya que es local.

def resta():
            print("RESTA:")
            print("Ingrese 2 numeros para restarlos:")
            while True:
                try:
                    n1 = int(input("Numero 1: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")
            while True:
                try:
                    n2 = int(input("Numero 2: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")

            res = n1-n2
            return res

def mutliplicacion():
            print("MULTIPLICACIÓN:")
            print("Ingrese 2 numeros para multiplicarlos.")
            while True:
                try:
                    n1 = int(input("Numero 1: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")
            while True:
                try:
                    n2 = int(input("Numero 2: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")

            res = n1*n2
            return res

def division():
            print("DIVISION:")
            print("Ingrese 2 numeros para dividirlos.")
            while True:
                try:
                    n1 = int(input("Dividir: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")
            while True:
                try:
                    n2 = int(input("Entre: "))
                    break
                except ValueError:
                    print ("Ingrese un valor valido (Numero)")

            res = n1/n2
            return res

eleccion = 0

diccionario = {
     1: sumaTuneada,
     2: resta,
     3: mutliplicacion,
     4: division
}

print ( """***********************************
       Calculadora:
        Sumar = 1
        Restar = 2
        Multiplicar = 3
        Dividir = 4
        ***************************""")
while True:
    try:
        eleccion = int(input("Opción: "))
        if  eleccion < 1 or eleccion > 4:
            print("Ingrese un valor del 1 al 4 segun corresponda")
        else:
            #Llama la función correspondiente
            resultado = diccionario[eleccion]()
            print("El resultado de la operación es = ", resultado)
    except ValueError:
        print ("No sea estupido, ingrese un valor numerico del 1 al 4.")
        # print("ERROR!")
        # print("Ingrese un valor del 1 al 4 segun corresponda")

# if eleccion == 1:
#     resultado = suma()
#     print("El resultado de la opcion es = ", resultado)
    
# else:
#      print("Nadota")


    









