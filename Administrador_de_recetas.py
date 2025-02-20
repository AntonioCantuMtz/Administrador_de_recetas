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
            system("cls")
            mostrar_categorias(carpeta_base1)
            categoria_ingresada = input("Ingresa el nombre de la categoría: ")
            nueva_ruta = mostrar_recetas(carpeta_base1, categoria_ingresada)
            receta = input("Ingresa la receta que deseas ver (sin la extensión del archivo): ")
            receta_seleccionada = receta + ".txt"
            leer_receta(nueva_ruta, receta_seleccionada)

        elif opcion_ingresada == 2:
            system("cls")
            mostrar_categorias(carpeta_base1)
            categoria_ingresada = input("Ingresa el nombre de la categoría a la que pertenecerá la nueva receta: ")
            crear_receta(carpeta_base1, categoria_ingresada)

        elif opcion_ingresada == 3:
            system("cls")
            mostrar_categorias(carpeta_base1)
            crear_categoria(carpeta_base1)

        elif opcion_ingresada == 4:
            mostrar_categorias(carpeta_base1)
            categoria_ingresada = input("Ingresa el nombre de la categoría: ")
            system("cls")
            mostrar_recetas(carpeta_base1, categoria_ingresada)
            eliminar_receta(carpeta_base1, categoria_ingresada)

        elif opcion_ingresada == 5:
            mostrar_categorias(carpeta_base1)
            categoria_ingresada = input("Ingresa el nombre de la categoría: ")
            system("cls")
            eliminar_categoria(carpeta_base1, categoria_ingresada)

        elif opcion_ingresada == 6:
            return print("Programa finalizado...")
        else:
            print("Esa opcion no existe. Favor de ingresar una opción valida.\n")
            system("cls")

def mostrar_categorias(carpeta_base1):
    print("Todas las categorías:")

    #La funcion iterdir() imprime todas las carpetas hijo de la ruta principal <3
    for hijo in carpeta_base1.iterdir():
        print(hijo)

    print("\n")

def mostrar_recetas(carpeta_base1, categoria_ingresada):
    nueva_ruta = Path(carpeta_base1, categoria_ingresada)

    for archivo in nueva_ruta.glob("*.txt"):
        print(archivo)

    return nueva_ruta

def leer_receta(nueva_ruta, receta):
    mostrar_receta = Path(nueva_ruta, receta)
    print(mostrar_receta.read_text())

    salir = "n"

    while salir != "s":
        salir = input("Favor de ingresar la letra 's' para volver al menú: ")

    system("cls")

#Con esta funcion no solo creamos el archivo sino que tambien le agregamos su contenido
def crear_receta(carpeta_base1, categoria_ingresada):
    nombre_receta = input("Ingresa el nombre de la receta: ")

    receta_nueva = nombre_receta + ".txt"

    nueva_ruta = Path(carpeta_base1, categoria_ingresada) / receta_nueva

    #Con el metodo touch() creamos un nuevo archivo (en caso de que este no exista)
    nueva_ruta.touch()

    contenido_receta = input("Ingresa el contenido de la receta: ")

    #Con el metodo write_text() le agreamos el contenido al archivo de texto
    nueva_ruta.write_text(contenido_receta)

def crear_categoria(carpeta_base1):
    nombre_categoria = input("Ingresa el nombre de la nueva categoría: ")

    nueva_categoria = Path(carpeta_base1) / nombre_categoria

    #Con el metodo mkdir() creamos un nuevo directorio (o una nueva carpeta)
    nueva_categoria.mkdir()

    system("cls")

def eliminar_receta(carpeta_base1, categoria_ingresada):
    receta = input("Ingresa el nombre de la receta que deseas eliminar: ")

    extension_receta = receta + ".txt"

    receta_a_eliminar = Path(carpeta_base1, categoria_ingresada) / extension_receta

    #Con el metodo unlink() eliminamos un archivo
    receta_a_eliminar.unlink()

    print("Receta eliminada con éxito.")

def eliminar_categoria(carpeta_base1, categoria_ingresada):
    categoria_a_eliminar = Path(carpeta_base1, categoria_ingresada)

    confirmar = ""

    while confirmar != "s" or confirmar != "n":

        confirmar = input("Estas seguro(a) que deseas borrar la categoría? (Presiona 's' para confirmar o 'n' para cancelar)\n"
                          "NOTA: También se borrarán las recetas almacenadas en dicha categoría.\n")

        if confirmar == "s":
            #La funcion rmdir() elimina una carpeta (o directorio)
            categoria_a_eliminar.rmdir()
            return print("Categoría eliminada con éxito.")
        elif confirmar == "n":
            return print("Operación cancelada.")

        system("cls")
        print("Por favor ingresa una opción válida.")

#Aqui se mandan a llamar las funciones
menu_principal(carpeta_base)






