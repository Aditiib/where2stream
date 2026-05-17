from letterboxd import load_wl

watchlist = load_wl('watchlist.csv')
for movie in watchlist:
    print(f"{movie['name']} ({movie['year']})")
