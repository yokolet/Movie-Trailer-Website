import json
import movie
import fresh_tomatoes

def run():
    """ Reads data from json file and creates html file."""
    with open('data/movies.json') as data_file:
        data = json.load(data_file)

    movies = []
    for d in data:
        movies.append(movie.Movie(d['title'], d['image'], d['url']))

    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    run()
