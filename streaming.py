import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
api_key = os.getenv("tmdb_key")

def streamingservice(movi_id):
    url = f"https://api.themoviedb.org/3/movie/{movi_id}/watch/providers"
    params ={
        'api_key': api_key
    }
    response = requests.get(url,params=params)
    data = response.json()
    india = data['results'].get('IN', {})
    flatrate = india.get('flatrate',[])
    names = []
    for i in flatrate:
        names.append(i['provider_name'])
    
    return names

