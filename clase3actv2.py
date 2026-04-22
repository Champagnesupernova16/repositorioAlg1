#Declaro la variable global
estudiantes = []

#Funcion leer consola
def leer_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre

#Funcion validar nombre
def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False

#Funcion persistir
def persistir_nombre(nombre):
    estudiantes.append(nombre)
    return True

#Funcion principal
def main():
    print("Bienvenida ...")
    nombre = leer_nombre()
    valid_nombre = validar_nombre(nombre)
    if valid_nombre:
        #Persisto
        persistir_nombre(nombre)
        print("Nombre guardado")
        print(estudiantes)
    else:
        print("Nombre invalido")
main()