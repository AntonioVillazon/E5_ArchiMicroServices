import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
movies = [
    {'id': 0,
     'title': 'Coming 2 America Trailer',
     'url': 'https://www.youtube.com/watch?v=acxUWBg_7CM&ab_channel=MovieclipsTrailers',
     'synopsis': 'Prince Akeem returns to America to search for his long-lost son.',
     'genre': 'comedy',
     'type': 'movie',
     'date': '2021',
     'notation': '5'},
    {'id': 1,
     'title': 'Dune',
     'url': 'https://www.youtube.com/watch?v=4t7utI9yrsA&ab_channel=ONEMedia',
     'synopsis': 'La planete la plus importante de l\'univers, Arrakis, est egalement appelée "Dune". Une gigantesque lutte pour le pouvoir commence autour de celle-ci, aboutissant a une guerre interstellaire.',
     'genre': 'sci-fi',
     'type': 'movie',
     'date': '2020',
     'notation': '4'},
    {'id': 2,
     'title': 'The White Tiger',
     'url': 'https://www.youtube.com/watch?v=ZMuDvgtuiBI&ab_channel=MovieclipsTrailers',
     'synopsis': 'The epic journey of a poor Indian driver who must use his wit and cunning to break free from servitude to his rich masters and rise to the top of the heap.',
     'genre': 'drama',
     'type': 'movie',
     'date': '2021',
     'notation': '3'}
]


#other functions
################
def string_equal(string_1, string_2):
    if (string_1 == string_2) or (string_1+'s' == string_2) or (string_1 == string_2+'s'):
        return True
################

    
#api functions

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Web API for films search test</h1>
<p>This web api is a test to check if we can access the films by
searching by id, title, genre, type, release_data, notation, ...</p>'''

#get all
@app.route('/api/v1/resources/movies/all', methods=['GET'])
def api_all_movies():
    return jsonify(movies)

#get film by id
@app.route('/api/v1/resources/movies/film_by_id', methods=['GET'])
def api_movie_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided or exceeding the number of films on the website."

    movies_links = []
    
    for movie in movies:
        if movie['id'] == id:
            movies_links.append({'id' : movie['id'], 'title' : movie['title'], 'synopsis' : movie['synopsis'], 'url' : movie['url']})

    return jsonify(movies_links)


#get film by title
@app.route('/api/v1/resources/movies/film_by_title', methods=['GET'])
def api_movies_by_title():

    title = request.args['title']

    movies_links = []
    cpt=0
    
    for movie in movies:
        if title.lower() in movie['title'].lower():
            movies_links.append({'title' : movie['title'], 'synopsis' : movie['synopsis'], 'url' : movie['url']})
            cpt+=1
            
    if cpt == 0:
        return "Error: The movie you are trying to find doesn't exist on this website."    
    return jsonify(movies_links)


#get film by genre
@app.route('/api/v1/resources/movies/film_by_genre', methods=['GET'])
def api_movies_by_genre():

    genre = request.args['genre']

    movies_links = []
    cpt=0
    
    for movie in movies:
        if string_equal(genre.lower(), movie['genre'].lower()):
            movies_links.append({'genre' : movie['genre'], 'title' : movie['title'], 'synopsis' : movie['synopsis'], 'url' : movie['url']})
            cpt+=1
            
    if cpt == 0:
        return "Error: No "+genre+" movies are available on this website."
    return jsonify(movies_links)



#get film by type
@app.route('/api/v1/resources/movies/film_by_type', methods=['GET'])
def api_movies_by_type():

    type_movie = request.args['type']

    movies_links = []
    cpt=0
    
    for movie in movies:
        if string_equal(type_movie.lower(), movie['type'].lower()):
            movies_links.append({'type' : movie['type'], 'title' : movie['title'], 'synopsis' : movie['synopsis'], 'url' : movie['url']})
            cpt+=1
            
    if cpt == 0:
        return "Error: No "+type_movie+" are available on this website."    
    return jsonify(movies_links)



@app.route('/api/v1/resources/movies/film_by_date', methods=['GET'])
def api_movies_by_release_date():

    release_data = request.args['date']

    movies_links = []
    cpt=0
    
    for movie in movies:
        if int(release_data) == int(movie['date']):
            movies_links.append({'date' : movie['date'], 'title' : movie['title'], 'synopsis' : movie['synopsis'], 'url' : movie['url']})
            cpt+=1
            
    if cpt == 0:
        return "Error: No film on this website has been released in "+release_data+"."    
    return jsonify(movies_links)


#get film by notation
@app.route('/api/v1/resources/movies/film_by_notation', methods=['GET'])
def api_movie_by_notation():
    notation = float(request.args['notation'])

    movies_links = []
    
    for movie in movies:
        if float(movie['notation']) >= notation:
            movies_links.append({'notation' : movie['notation'], 'title' : movie['title'], 'synopsis' : movie['synopsis'], 'url' : movie['url']})

    return jsonify(movies_links)


app.run()
