# Gestión de de países

Este repositorio contiene el Trabajo Práctico Integrador (TPI) para la materia **Programación 1** de la Tecnicatura Universitaria en Programación a Distancia (UTN). 

El objetivo del proyecto es desarrollar una aplicación de consola en Python que permita gestionar información sobre países, aplicando estructuras de datos (listas y diccionarios), modularización con funciones, persistencia en archivos CSV y la generación de estadísticas y filtros.

## Características del Sistema

El programa ofrece un menú interactivo que permite realizar las siguientes operaciones:
* **Agregar:** Ingresar un nuevo país validando sus datos y guardándolo en el archivo `.csv`.
* **Actualizar:** Modificar la población y superficie de un país existente mediante.
* **Buscar:** Encontrar países por coincidencia exacta o parcial de su nombre.
* **Filtrar:** Obtener listados según el Continente, o por rangos numéricos de población y superficie.
* **Ordenar:** Visualizar los datos ordenados por nombre, población o superficie (de manera ascendente o descendente).
* **Estadísticas:** Calcular indicadores como países con mayor/menor población, promedios globales y cantidad de países por continente.

## Instrucciones de Uso

1. Clonar este repositorio en tu máquina local:
   ```bash
   git clone [UTN-TUPaD-Programacion1-TPI](https://github.com/fdmuinos/UTN-TUPaD-Programacion1-TPI.git)
2. Tener instalado Python 3.x.
3. Navegar a la carpeta del proyecto y ejecutar el archivo principal desde la terminal:
   ```bash
   python main.py
4. Interactuar con el menú principal ingresando el número de la opción deseada (1-7).

## Ejemplos de Entradas y Salidas

### Ejemplo de Búsqueda Parcial (Opción 3)
- Entrada del usuario: arg
- Salida del sistema:
   ```plaintext
   Se encontraron 1 coincidencia(s):
   ----------------------------------------
   Nombre: Argentina
   Población: 45376763
   Superficie: 2780400 km2
   Continente: América
   ----------------------------------------

### Ejemplo de Estadísticas (Opción 6)
- Salida del sistema:
    ```plaintext
    • País con MAYOR población: Brasil (213.993.437 hab.)
   • País con MENOR población: Australia (26.000.000 hab.)
   • Promedio de población global: 66.885.566,67 hab.
   • Promedio de superficie global: 3.489.432,22 km2

## Equipo de Trabajo
- Fernando Muiños.

## Enlaces
- Video Demostración: 

