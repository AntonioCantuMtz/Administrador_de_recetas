#Proyecto 'administrador de recetas'
from pathlib import Path
from os import system

total_de_recetas = 0

print("Bienvenido al administrador de recetas")

#Todas las carpetas y archivos que vayamos creando se almacenan en esta ruta
carpeta_base = Path(Path.home(), "Recetas")

print("\nTodas las categorías y recetas que vayas creando se almacenan en la siguiente ruta: ", carpeta_base, "\n")

#Con este for recorremos todas las sub carpetas de la carpeta base y buscamos todos los archivos txt hay
for txt in Path(carpeta_base).glob("**/*.txt"):
    total_de_recetas = total_de_recetas + 1

print(f"\nLa cantidad de recetas almancenadas (entre todas las categorías) es de: {total_de_recetas}\n")

#Esta funcion es el menu principal del programa y realiza una tarea determinada
#dependiendo de la opcion ingresada por el usuario
def menu_principal(carpeta_base1):

    opcion_del_menu = 0
    categoria_ingresada = ""

    while opcion_del_menu != 6:
        print("Opciones del menú:\n"
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
            system("cls")
            print("Has ingresado un valor no valido. Favor de ingresar una opción valida.\n")
            opcion_ingresada = 0

        #Mediante los siguientes IFs iremos accediendo a las distintas opciones del menú
        if opcion_ingresada == 1:
            mostrar_categorias(carpeta_base1)
            categoria_ingresada = input("Ingresa el nombre de la categoría: ")
            nueva_ruta2 = mostrar_recetas(carpeta_base1, categoria_ingresada)
            receta = input("Ingresa la receta que deseas ver (sin la extensión del archivo): ")
            receta_seleccionada = receta + ".txt"
            mostrar_receta_seleccionada(nueva_ruta2, receta_seleccionada)
        elif opcion_ingresada == 2:
            print("Lo sentimos esa opcion aun no esta disponible :(")
            system("cls")
        elif opcion_ingresada == 3:
            print("Lo sentimos esa opcion aun no esta disponible :(")
            system("cls")
        elif opcion_ingresada == 4:
            print("Lo sentimos esa opcion aun no esta disponible :(")
            system("cls")
        elif opcion_ingresada == 5:
            print("Lo sentimos esa opcion aun no esta disponible :(")
            system("cls")
        elif opcion_ingresada == 6:
            return "Programa finalizado..."
        else:
            print("Esa opcion no existe. Favor de ingresar una opción valida.\n")
            system("cls")



def mostrar_categorias(carpeta_base2):
    print("Todas las categorías:")

    #La funcion iterdir() imprime todas las carpetas hijo de la ruta principal <3
    for hijo in carpeta_base2.iterdir():
        print(hijo)

    print("\n")

def mostrar_recetas(carpeta_base3, categoria_ingresada):
    nueva_ruta = Path(carpeta_base3, categoria_ingresada)

    for archivo in nueva_ruta.glob("*.txt"):
        print(archivo)

    return nueva_ruta

def mostrar_receta_seleccionada(nueva_ruta3, receta):
    mostrar_receta = Path(nueva_ruta3, receta)
    print(mostrar_receta.read_text())

    salir = "n"

    while salir != "s":
        salir = input("Favor de ingresar la letra 's' para volver al menú: ")

    system("cls")


#Aqui se mandan a llamar las funciones
menu_principal(carpeta_base)






