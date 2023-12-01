# Analisis-calidad-aire
Parte 1 
Importa las bibliotecas: pandas para el manejo de datos, requests para hacer solicitudes HTTP
parte 2
Define la función ej_1_cargar_datos_demograficos(): la siguiente función carga un archivo CSV llamado ‘demografic_data.csv’ en un DataFrame de pandas y lo devuelve.
parte 3
Define la función ej_2_cargar_calidad_aire : la  función toma un conjunto de nombres de ciudades y realiza las siguientes operaciones:

Para cada ciudad en el conjunto , hasta un máximo de 9 ciudades, hace una solicitud GET a la API de calidad del aire de api-ninjas.com.
Si la respuesta de la API es exitosa, código de estado HTTP 200, procesa los datos de la respuesta y los carga a una lista de diccionarios.
Crea un DataFrame de pandas a partir de la lista de diccionarios, lo ordena por nombre de ciudad y lo guarda en un archivo CSV llamado ‘ciudades.csv’.
Finalmente, convierte el DataFrame en un diccionario y lo devuelve.
parte 4
Carga los datos demográficos: Utiliza la función ej_1_cargar_datos_demograficos() para cargar los datos demográficos en un DataFrame.
parte 5
Limpia el DataFrame de datos demográficos: Si el DataFrame no está vacío, elimina las columnas ‘Race’, ‘Count’ y ‘Number of Veterans’ (si existen) y elimina las filas duplicadas.
parte 6
Obtiene los datos de calidad del aire: Crea un conjunto de nombres de ciudades a partir de la columna ‘City’ del DataFrame de datos demográficos y utiliza la función ej_2_cargar_calidad_aire(ciudades1) para obtener los datos de calidad del aire para esas ciudades.
