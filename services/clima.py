from config.config import api_key, base_url
from datetime import datetime, time
import requests

def coordenadas(cidade, api_key, base_url): # coordenadas

    params = { # parâmetros da requisição
        "q": cidade,
        "limit": 1,
        "appid": api_key
    }

    response = requests.get(base_url, params=params) # requisição das coordenadas

    if response.status_code == 200: # funcionou
        data = response.json() 
        
        if data: 
            lat = data[0]["lat"] # latitude
            lon = data[0]["lon"] # longitude
            return lat, lon
        
        else: # se a cidade não for encontrada, mostrar erro.
            print("Cidade não encontrada.") 
            return None
        
    else: # se a requisição falhar, mostrar erro.
        print("Erro na requisição:", response.status_code)
        return None
    
def previsao_tempo(api_key, lat, lon): # previsão do tempo

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br"

    response = requests.get(weather_url) # requisição da previsão do tempo

    if response.status_code == 200: # funcionou
        data = response.json()
        return data

    else: # se a requisição falhar, mostrar erro.
        print("Erro na requisição:", response.status_code)
        return None

def estimativa_chuva(api_key, lat, lon): # estimativa de chuva

    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=pt_br"

    response = requests.get(forecast_url) # requisição da estimativa de chuva

    if response.status_code == 200: # funcionou
        data = response.json()
        return data
    
    else: # se a requisição falhar, mostrar erro.
        print("Erro na requisição:", response.status_code)
        return None
