import requests

     
def obtenir_meteo_ville(nom_ville, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={nom_ville}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        print(f"\n--- Météo à {nom_ville} ---")
        print(f"Température: {data['main']['temp']}°C")
        print(f"Description: {data['weather'][0]['description']}")
        print("-----------------------------")
    else:
        print("\nErreur: Impossible d'obtenir la météo. Veuillez vérifier le nom de la ville ou l'API Key.")