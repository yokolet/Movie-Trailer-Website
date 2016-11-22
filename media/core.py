import movie
import fresh_tomatoes

def run():
    toy_story = movie.Movie("Toy Story",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youTube.com/watch?v=vwyZH85NQC4")

    avatar = movie.Movie("Avatar",
                         "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                         "http://www.youtube.com/watch?v=-9ceBgWV8io")

    school_of_rock = movie.Movie("School of Rock",
                                 "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                 "https://www.youtube.com/watch?v=3PsUJFEBC74")

    ratatouille = movie.Movie("Ratatouille",
                              "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                              "https://www.youtube.com/watch?v=c3sBBRxDAqk")

    midnight_in_paris = movie.Movie("Midnight in Paris",
                                    "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                    "https://www.youtube.com/watch?v=atLg2wQQxvU")

    hunger_games = movie.Movie("Hunger Games",
                               "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                               "https://www.youtube.com/watch?v=PbA63a7H0bo")

    movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    run()
