import media
import fresh_tomatoes
import requests

data_string = """https://api.themoviedb.org/3/search/movie?api_key=
                 0bf21ff60196bf22bce9136c1db1da7c&query="""
movies = []


def create_movie_object(movie):
    search_params = ''
    # create search params to feed to api call
    for word in movie.split():
        search_params += word+'+'
    search_movie = data_string + search_params

    # call movie api for requested movie
    r = requests.get(search_movie)

    # create dictionary of results
    resp = r.json()['results'][0]

    # create poster url
    poster_link = 'http://image.tmdb.org/t/p/w185/' + resp['poster_path']

    # use movie ID to request the trailer and construct youtube url
    movie_url = "http://api.themoviedb.org/3/movie/"
    video_url = "/videos?api_key=0bf21ff60196bf22bce9136c1db1da7c"
    trailer = requests.get(movie_url + str(resp['id']) + video_url)
    youtube_link_start = "https://www.youtube.com/watch?v="
    youtube_link = youtube_link_start + trailer.json()['results'][0]['key']

    # add new movie object to list of movies
    movies.append(media.Movie(resp['original_title'],
    	          resp['overview'], poster_link, youtube_link))

if __name__ == '__main__':
    create_movie_object("School of Rock")
    create_movie_object("Toy Story")
    create_movie_object("Ratatouille")
    create_movie_object("Midnight In Paris")
    create_movie_object("Hunger Games")

    fresh_tomatoes.open_movies_page(movies)
