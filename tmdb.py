import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
api_key = os.getenv("tmdb_key")

def moviesearch(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': api_key,
        'query': title
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['results'][0]['id']
print(moviesearch("Interstellar"))