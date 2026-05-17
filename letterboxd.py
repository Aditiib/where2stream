import csv
def load_wl(filename):
    movies = []
    with open(filename, newline = "", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append({
                'name': row['Name'],
                'year' : row['Year'],
                'url' : row['Letterboxd URI']
            })
    return movies
