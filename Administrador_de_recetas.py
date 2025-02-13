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

print(f"\nLa cantidad de recetas almancenadas (entre todas las categorías) es de: {total_de_recetas}")

