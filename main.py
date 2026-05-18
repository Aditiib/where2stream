import time
from letterboxd import load_wl
from streaming import streamingservice
from tmdb import moviesearch

watchlist = load_wl('watchlist.csv')

platform = input("Which platform? (e.g. Netflix, JioHotstar, Amazon Prime Video): ").strip()

for movie in watchlist:
    print(f"checking {movie['name']}...")
    movie_id = moviesearch(movie['name'])
    if movie_id:
        platforms = streamingservice(movie_id)
        if platform.lower() in [p.lower() for p in platforms]:
            print(f"✓ {movie['name']} ({movie['year']})")
    time.sleep(0.25)
