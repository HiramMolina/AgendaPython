
# Agregar contacto
def agregarCont():
    nombre = input("Ingrese nombre de contacto: ")
    numero = input("Ingrese numero de contacto: ")
    archivo = open('agenda.txt' , 'a')
    archivo.write('\n' + nombre + ',' + numero)
    archivo.close()

def buscarCont():
    nombre = input("Nombre del contacto por buscar: ")
    archivo = open('agenda.txt', 'r')

    # Empieza siendo falso porque no hemos buscado aún.
    encontrado = False
    # Vamos a recorrer cada línea del archivo con un ciclo. Cada línea será guardada en la variable "linea".
    for linea in archivo:
        # Aquí verificamos si lo que escribió el usuario (nombre) está dentro de esta línea.
        # Hacemos todo minúsculas con .lower() para ignorar mayúsculas/minúsculas
        if nombre.lower() in linea.lower(): 
        # Si encontramos el nombre en la línea, imprimimos el contenido de esa línea (el contacto completo: nombre y número)
            print(f"Contacto encontrado: {linea.strip()}")
            # Marcamos que ya lo encontramos, poniendo la variable "encontrado" en True
            encontrado = True
            # Como ya encontramos el contacto, nos salimos del ciclo con "break". No seguimos buscando.
            break
    # Después del ciclo, si no encontramos nada (es decir, "encontrado" sigue siendo False):
    if not encontrado:
        # Imprimimos un mensaje que dice que no hay contacto con ese nombre.
        print(f"No se encontró ningún contacto con el nombre '{nombre}'.")
    # Cerramos el archivo porque ya no lo necesitamos. Esto es muy importante.
    archivo.close()
# Mostrar todos los contactos
def mostrarCont():
    archivo = open('agenda.txt' , 'r')
    registros = archivo.read()
    print("""
          
    * Contactos *
          
          """)
    print(registros)
    print("""
          
    * Fin de la lista. *
          
          """)

def eliminarCont():
    mostrarCont()
    nombre = input("Nombre del contacto por eliminar: ")
    with open("agenda.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontrado = False
    nuevas_lineas =  []

    for linea in lineas:
        if nombre.lower() in linea.lower():
            print("Contacto encontrado")
            encontrado = True
        else: 
            nuevas_lineas.append(linea)
            print("Entra else")
        
        if encontrado:
            with open ("agenda.txt" , "w") as archivo:
                archivo.writelines(nuevas_lineas)
                # print(f"El contacto '{nombre}' ha sido eliminado.")
    else:
            print(f"No se encontró nigun contacto con el nombre '{nombre}'.")

def menu():
    print("""
            Bienvenido a mi agenda en Python.
            """)
    print("\nSeleccione una opción:\n")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar todos los contactos")
    print("4. Eliminar contacto")
    print("5. Salir\n")

#############################

print("""
        Bienvenido a mi agenda en Python.
        """)
print("\nSeleccione una opción:\n")
print("1. Agregar contacto")
print("2. Buscar contacto")
print("3. Mostrar todos los contactos")
print("4. Eliminar contacto")
print("5. Salir\n")

eleccion = 0

diccionario = {
    1: agregarCont,
    2: buscarCont,
    3: mostrarCont,
    4: eliminarCont
}

while True:
    
    try:
        # menu()
        eleccion = int(input("Ingresar a opción: "))
        if eleccion < 1 or eleccion > 5:
            print("Ingrese un numero valido.")
        else:
            eleccion = diccionario[eleccion]()
            print("Listo!\n")
    except ValueError:
        print ("No sea estupido, ingrese un valor numerico del 1 al 4.")
        



