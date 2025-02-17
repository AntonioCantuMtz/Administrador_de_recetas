#Proyecto 'administrador de recetas'
from pathlib import Path

total_de_recetas = 0

print("Bienvenido al administrador de recetas\n")

#Todas las carpetas y archivos que vayamos creando se almacenan en esta ruta
carpeta_base = Path(Path.home(), "Recetas")

print("Todas las categorías y recetas que vayas creando se almacenan en la siguiente ruta: ", carpeta_base)

#Con este for recorremos todas las sub carpetas de la carpeta base y buscamos todos los archivos txt hay
for txt in Path(carpeta_base).glob("**/*.txt"):
    total_de_recetas = total_de_recetas + 1

print(f"\nLa cantidad de recetas almancenadas (entre todas las categorías) es de: {total_de_recetas}\n")

#Esta funcion es el menu principal del programa y realiza una tarea determinada
#dependiendo de la opcion ingresada por el usuario
def menu_principal(carpeta_base1):

    opcion_del_menu = 0

    while opcion_del_menu != 6:
        print("Opciones del menú\n"
              "1. Leer recetas\n"
              "2. Crear receta\n"
              "3. Crear categoría\n"
              "4. Eliminar receta\n"
              "5. Eliminar categoría\n"
              "6. Finalizar programa\n")

        #Aqui evaluamos si lo que ingresa el usuario es un numero o no
        try:
            opcion_ingresada = int(input("Elige la opción que desees: "))
        except:
            print("Has ingresado un valor no valido. Favor de ingresar una opción valida.\n")
            opcion_ingresada = 0

        #Mediante los siguientes IFs iramos accediendo a las distintas opciones del menú
        if opcion_ingresada == 1:
            mostrar_categorias(carpeta_base1)
        elif opcion_ingresada == 2:
            print("Lo sentimos esa opcion aun no esta disponible :(")
        elif opcion_ingresada == 3:
            print("Lo sentimos esa opcion aun no esta disponible :(")
        elif opcion_ingresada == 4:
            print("Lo sentimos esa opcion aun no esta disponible :(")
        elif opcion_ingresada == 5:
            print("Lo sentimos esa opcion aun no esta disponible :(")
        elif opcion_ingresada == 6:
            return "Programa finalizado..."
        else:
            print("Esa opcion no existe. Favor de ingresar una opción valida.\n")



def mostrar_categorias(carpeta_base2):
    print("Todas las categorías:")

    #La funcion iterdir() imprime todas las carpetas hijo de la ruta principal <3
    for hijo in carpeta_base2.iterdir():
        print(hijo)


#Aqui se mandan a llamar las funciones
menu_principal(carpeta_base)






