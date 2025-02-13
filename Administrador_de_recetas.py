#Proyecto 'administrador de recetas'
from pathlib import Path

total_de_recetas = 0
opciones_del_menu = 0

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
def menu_principal(opcion_ingresada):
    while opcion_ingresada != 6:
        print("Opciones del menú\n"
              "1. Leer recetas\n"
              "2. Crear receta\n"
              "3. Crear categoría\n"
              "4. Eliminar receta\n"
              "5. Eliminar categoría\n"
              "6. Finalizar programa\n")

        try:
            opcion_ingresada = int(input("Elige la opción que desees: "))
        except:
            print("Has ingresado un valor no valido. Favor de ingresar una opción valida.\n")
            opcion_ingresada = 0

    return "Programa finalizado..."


menu_principal(opciones_del_menu)






