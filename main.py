import os

def contar_lineas_codigo(archivo):

    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = f.readlines()

    loc = 0
    for linea in lineas:
        linea = linea.strip()
        if linea != '' and not linea.startswith('#'):
            loc += 1

    return loc

def calcular_loc_en_directorio(directorio):
    
    total_loc = 0
    informe = []

    for root, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith('.py'):
                path_archivo = os.path.join(root, archivo)
                loc_archivo = contar_lineas_codigo(path_archivo)
                total_loc += loc_archivo
                informe.append((path_archivo, loc_archivo))

    return total_loc, informe

if __name__ == "__main__":
    # Directorio que deseamos analizar
    directorio_a_analizar = '/ruta/a/tu/directorio'

    # Calcular métricas LOC
    total_loc, informe = calcular_loc_en_directorio(directorio_a_analizar)

    # Presentar informe detallado
    print(f"Informe detallado de las métricas LOC en el directorio: {directorio_a_analizar}\n")
    print(f"Total de líneas de código (LOC) encontradas: {total_loc}\n")
    print("Detalles por archivo:\n")
    for archivo, loc in informe:
        print(f"Archivo: {archivo}")
        print(f"Líneas de código (LOC): {loc}\n")

    print("Fin del informe.")
