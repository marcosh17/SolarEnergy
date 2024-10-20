# archivo: pvgis_api.py

import requests

def get_irradiance_data(latitude, longitude):
    """
    Obtiene los datos de irradiancia de la API de PVGIS para una ubicación específica.

    :param latitude: Latitud de la ubicación.
    :param longitude: Longitud de la ubicación.
    :return: Un diccionario con los datos de irradiancia.
    :raises Exception: Si la solicitud a la API falla.
    """
    url = f"https://re.jrc.ec.europa.eu/api/v5_2/seriescalc?lat={latitude}&lon={longitude}&outputformat=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception("Error al obtener datos de la API de PVGIS")
