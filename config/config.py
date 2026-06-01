import os
from dotenv import load_dotenv

load_dotenv() # Carregar variáveis de ambiente do arquivo .env

api_key = os.getenv("api_key") # Pegar a chave da API do ambiente
base_url = f"https://api.openweathermap.org/geo/1.0/direct?q={{cidade}}&limit=5&appid={api_key}" # URL base para obter coordenadas
custo_kwh = 0.75
custo_visita = 80