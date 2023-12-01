import pandas as pd
import requests 
from typing import Set


def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    df = pd.read_csv('demografic_data.csv', encoding='utf-8', sep=';')
    return df


def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
        
    datos = []

    for i, city in enumerate(ciudades):
        if i >= 9:
            break 
        api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
        response = requests.get(api_url, headers={"X-Api-Key" : "zNnV/PhmkThpmn1DSe2QZg==wWK4V8NvyWgszii3"})
        if response.status_code == 200:
            data = response.json()
            print(response.text)
            dict_datos = {'city': city}
            for key, entry in data.items():
                if isinstance(entry, dict):
                    concentracion = entry.get('concentration', 'concentracion no disponible')
                    dict_datos[key] = concentracion
            datos.append(dict_datos) 
    df = pd.DataFrame(datos)
    df.sort_values(by=['city'], inplace= True)
    df.to_csv('ciudades.csv', index= False)
    dict_resultado = df.to_dict()


    return dict_resultado


df_demografic = ej_1_cargar_datos_demograficos()
if not df_demografic.empty:
    columnas_a_limpiar = ['Race', 'Count', 'Number of Veterans']
    for columna in columnas_a_limpiar:
        if columna in df_demografic.columns:
            df_demografic.drop(columns=[columna], inplace= True)
    df_demografic.drop_duplicates(inplace= True)

    ciudades1 = set(df_demografic['City'])
    df_calidad_aire = ej_2_cargar_calidad_aire(ciudades1)
           





