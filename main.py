import csv

# --- MÓDULOS DEL SISTEMA ---

def agregar_pais(lista_paises):
    print("\n--- AGREGAR NUEVO PAÍS ---")
    
    while True:
        # Ingreso de datos (.strip() para eliminar espacios en blanco y .capitalize() para devolver una versión en Mayúscula y cuidar el formato impreso)
        nombre = input("Ingrese el nombre del país: ").strip().lower()
        poblacion_str = input("Ingrese la población: ").strip()
        superficie_str = input("Ingrese la superficie en km2: ").strip()
        continente = input("Ingrese el continente: ").strip().lower()

        # Primera Validación: ¿Campos vacíos?
        if not nombre or not poblacion_str or not superficie_str or not continente:
            print("Error: Ningún campo puede estar vacío. Intente de nuevo.\n")
            continue

        # Segunda Validación: ¿Población y Superficie son valores numéricos?
        try:
            poblacion = int(poblacion_str)
            superficie = int(superficie_str)
        except ValueError:
            print("Error: La población y la superficie deben ser números enteros válidos. Intente de nuevo.\n")
            continue  

        # Crear registro y guardar en la estructura de datos
        nuevo_pais = {
            'nombre': nombre,
            'poblacion': poblacion,
            'superficie': superficie,
            'continente': continente
        }
        lista_paises.append(nuevo_pais)
        guardar_datos('paises.csv', lista_paises)
        
        # Confirmación y fin
        print(f"¡Éxito! '{nombre}' ha sido agregado correctamente al sistema.")
        break  

def actualizar_datos(lista_paises):
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    nombre_buscar = input("Ingrese el nombre exacto del país a actualizar: ").strip()
    
    # Búsqueda del país
    pais_encontrado = None
    for pais in lista_paises:
        # Se usa .lower() para que sea indistinto si el usuario ingresa mayúsculas o minúsculas
        if pais['nombre'] == nombre_buscar.lower():
            pais_encontrado = pais
            break
            
    # Si el país no existe, se muestar el error y se vuelve al menú 
    if not pais_encontrado:
        print(f"Error: No se encontró el país '{nombre_buscar}' en la base de datos.")
        return

    # Si el país existe, se pide y valida a los nuevos datos
    print(f"País encontrado: {pais_encontrado['nombre'].capitalize()} (Población actual: {pais_encontrado['poblacion']}, Superficie actual: {pais_encontrado['superficie']})")
    
    while True:
        nueva_pob_str = input("Ingrese la NUEVA población: ").strip()
        nueva_sup_str = input("Ingrese la NUEVA superficie en km2: ").strip()
        
        if not nueva_pob_str or not nueva_sup_str:
            print("Error: Los campos no pueden estar vacíos. Intente de nuevo.\n")
            continue
            
        try:
            nueva_poblacion = int(nueva_pob_str)
            nueva_superficie = int(nueva_sup_str)
        except ValueError:
            print("Error: Debe ingresar números enteros válidos. Intente de nuevo.\n")
            continue
            
        # Sobrescribir los datos en el diccionario
        pais_encontrado['poblacion'] = nueva_poblacion
        pais_encontrado['superficie'] = nueva_superficie
        
        # Guardar los cambios en el archivo CSV
        guardar_datos('paises.csv', lista_paises)
        
        print(f"¡Éxito! Los datos de '{pais_encontrado['nombre']}' han sido actualizados.")
        break

def buscar_pais(lista_paises):
    print("\n--- BUSCAR PAÍS ---")
    termino = input("Ingrese el nombre o fragmento a buscar: ").strip().lower()
    
    # Validación básica por si el usuario presiona Enter sin escribir nada
    if not termino:
        print("Error: El término de búsqueda no puede estar vacío.")
        return

    # Recorrer la estructura de datos y guardar las coincidencias
    resultados = []
    for pais in lista_paises:
        # Se evlua si el fragmento ingresado está en el nombre del país
        if termino in pais['nombre'].lower():
            resultados.append(pais)
            
    # Evaluar si hubo resultados y mostrarlos
    if len(resultados) == 0:
        print(f"No se encontraron países que contengan '{termino}'.")
    else:
        print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
        print("-" * 40)
        for p in resultados:
            print(f"Nombre: {p['nombre'].capitalize()}") # Se usa .capitalize() para curar el formato de impresión
            print(f"Población: {p['poblacion']}")
            print(f"Superficie: {p['superficie']} km2")
            print(f"Continente: {p['continente'].capitalize()}")
            print("-" * 40)

def filtrar_paises(lista_paises):
    print("\n--- FILTRAR PAÍSES ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    
    opcion = input("Elija un filtro (1-3): ").strip()
    resultados = []

    # A: Filtro por Continente
    if opcion == '1':
        continente_buscado = input("Ingrese el continente: ").strip().lower()
        for pais in lista_paises:
            # Se usa .lower() para evitar problemas con mayúsculas/minúsculas
            if pais['continente'].lower() == continente_buscado:
                resultados.append(pais)
                
    # B: Filtro por Población
    elif opcion == '2':
        try:
            min_pob = int(input("Ingrese la población mínima: ").strip())
            max_pob = int(input("Ingrese la población máxima: ").strip())
            for pais in lista_paises:
                if min_pob <= pais['poblacion'] <= max_pob:
                    resultados.append(pais)
        except ValueError:
            print("Error: Los rangos deben ser números enteros válidos.")
            return # Se retorna al menú principal si hay error
            
    # C: Filtro por Superficie
    elif opcion == '3':
        try:
            min_sup = int(input("Ingrese la superficie mínima en km2: ").strip())
            max_sup = int(input("Ingrese la superficie máxima en km2: ").strip())
            for pais in lista_paises:
                if min_sup <= pais['superficie'] <= max_sup:
                    resultados.append(pais)
        except ValueError:
            print("Error: Los rangos deben ser números enteros válidos.")
            return # Se retorna al menú principal si hay error
            
    else:
        print("Error: Opción de filtro no válida.")
        return # Se sale si no elige 1, 2 o 3

    # Se muestran los resultados almacenados
    if len(resultados) == 0:
        print("\nNo se encontraron países que cumplan con los criterios de filtrado.")
    else:
        print(f"\nSe encontraron {len(resultados)} país(es):")
        print("-" * 40)
        for p in resultados:
            print(f"Nombre: {p['nombre'].capitalize()}")
            print(f"Población: {p['poblacion']}")
            print(f"Superficie: {p['superficie']} km2")
            print(f"Continente: {p['continente'.capitalize()]}")
            print("-" * 40)

def ordenar_paises(lista_paises):
    print("\n--- ORDENAR PAÍSES ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    
    opcion_criterio = input("Elija un criterio (1-3): ").strip()
    
    # Se mapea la opción del usuario a la key del diccionario
    if opcion_criterio == '1':
        clave = 'nombre'
    elif opcion_criterio == '2':
        clave = 'poblacion'
    elif opcion_criterio == '3':
        clave = 'superficie'
    else:
        print("Error: Criterio no válido.")
        return

    print("\nDirección de ordenamiento:")
    print("1. Ascendente (Menor a Mayor / A-Z)")
    print("2. Descendente (Mayor a Menor / Z-A)")
    
    opcion_dir = input("Elija la dirección (1-2): ").strip()
    
    # Configurar la dirección 
    if opcion_dir == '1':
        es_descendente = False
    elif opcion_dir == '2':
        es_descendente = True
    else:
        print("Error: Dirección de ordenamiento no válida.")
        return

    # Se aplica el ordenamiento
    paises_ordenados = sorted(lista_paises, key=lambda x: x[clave], reverse=es_descendente)

    # Mostrar los resultados
    print("\n--- RESULTADOS ORDENADOS ---")
    for p in paises_ordenados:
        print(f"Nombre: {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km2")

def mostrar_estadisticas(lista_paises):
    print("\n--- ESTADÍSTICAS DE LOS PAÍSES ---")
    
    # Validación de seguridad: evitar que el programa falle si la lista está vacía
    if not lista_paises:
        print("Error: No hay datos suficientes para calcular estadísticas.")
        return

    # País con mayor y menor población
    pais_max = max(lista_paises, key=lambda x: x['poblacion'])
    pais_min = min(lista_paises, key=lambda x: x['poblacion'])

    # Promedios de Población y Superficie
    total_pob = sum(p['poblacion'] for p in lista_paises)
    total_sup = sum(p['superficie'] for p in lista_paises)
    cantidad = len(lista_paises)
    
    promedio_pob = total_pob / cantidad
    promedio_sup = total_sup / cantidad

    # Cantidad de países por continente
    conteo_continentes = {}
    for p in lista_paises:
        # Se usa .capitalize() para normalizar 
        continente = p['continente'].title()
        if continente in conteo_continentes:
            conteo_continentes[continente] += 1
        else:
            conteo_continentes[continente] = 1

    # --- IMPRESIÓN DE RESULTADOS ---
    print(f"• País con MAYOR población: {pais_max['nombre']} ({pais_max['poblacion']:,} hab.)")
    print(f"• País con MENOR población: {pais_min['nombre']} ({pais_min['poblacion']:,} hab.)")
    
    # Usamos :.2f para mostrar los promedios solo con 2 decimales
    print(f"• Promedio de población global: {int(promedio_pob):,} hab.")
    print(f"• Promedio de superficie global: {promedio_sup:,.2f} km2")
    
    print("\n• Cantidad de países por continente:")
    for cont, cant in conteo_continentes.items():
        print(f"  - {cont}: {cant} país(es)")

# --- FUNCIÓN DE LECTURA DE DATOS ---

def cargar_datos(ruta_archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    """
    paises = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            # Se usa DictReader para que cada fila sea un diccionario
            lector_csv = csv.DictReader(archivo, skipinitialspace=True)
            for fila in lector_csv:
                # Se convierte "Población" y "Superficie" a int 
                fila['poblacion'] = int(fila['poblacion'])
                fila['superficie'] = int(fila['superficie'])
                paises.append(fila)
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}.")
    except ValueError:
        print("Error de formato en el CSV: Población y Superficie deben ser numéricos.")
    
    return paises

def guardar_datos(ruta_archivo, lista_paises):
    try: 
        with open(ruta_archivo, mode='w', encoding='utf-8', newline='') as archivo:
            # Nombres de las columnas de la base de datos
            encabezados = ['nombre', 'poblacion', 'superficie', 'continente']
            
            # Configuración del escritor
            escritor_csv = csv.DictWriter(archivo, fieldnames=encabezados)
            
            # Escritura de los encabezados
            escritor_csv.writeheader()
            
            # Escritura de los registros
            escritor_csv.writerows(lista_paises)
            
    except Exception as e:
        print(f"Error al intentar guardar el archivo: {e}")

# --- BUCLE PRINCIPAL ---

def main():
    # Cargar el dataset en una lista de diccionarios
    archivo_csv = 'paises.csv'
    dataset_paises = cargar_datos(archivo_csv)

    # Bucle del Menú Principal
    while True:
        print("\n--- GESTIÓN DE DATOS DE PAÍSES ---")
        print("1. Agregar un país")
        print("2. Actualizar datos de un país")
        print("3. Buscar un país")
        print("4. Filtrar países")
        print("5. Ordenar países")
        print("6. Mostrar estadísticas")
        print("7. Salir")

        opcion = input("Ingrese una opción (1-7): ")

        # Selector de opciones 
        if opcion == '1':
            agregar_pais(dataset_paises)
        elif opcion == '2':
            actualizar_datos(dataset_paises)
        elif opcion == '3':
            buscar_pais(dataset_paises)
        elif opcion == '4':
            filtrar_paises(dataset_paises)
        elif opcion == '5':
            ordenar_paises(dataset_paises)
        elif opcion == '6':
            mostrar_estadisticas(dataset_paises)
        elif opcion == '7':
            print("Finalizando el programa. ¡Hasta la próxima!")
            break
        else:
            print("Error: Opción no válida. Por favor ingrese un número del 1 al 7.")

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    main()