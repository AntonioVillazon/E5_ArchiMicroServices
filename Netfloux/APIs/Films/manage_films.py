import os
import flask
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
#app = flask.Flask(__name__)
#app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

###############################
#           display           #
###############################

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Movies Management</h1>
<p>This API will help us to manage the movies database with actions like add a movie, remove a movie, update the informations of a movie.</p>'''


@app.route('/movies/all', methods=['GET'])
def api_all():
    '''fucntion to display all the movies objects from the database'''
    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT * FROM MOVIES;').fetchall()

    return jsonify(all_movies)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

###############################
#           append            #
###############################

def create_movies(conn, movie):
    sql = ''' INSERT INTO MOVIES(movie_name,movie_url,movie_synopsis,movie_genre,movie_notation,movie_date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, movie)
    conn.commit()
    return cur.lastrowid

@app.route('/movies/append', methods=['POST'])
def api_append():
    '''
function to append a movie as a json object with the POST method
exemple (if you can use a softwore like POSTMAN) :
    {
    "movie_date": 2020, 
    "movie_genre": "drama", 
    "movie_name": "Tenet", 
    "movie_notation": 4.5, 
    "movie_synopsis": "Armed with only one word, Tenet, and fighting for the survival of the entire world, a Protagonist journeys through a twilight world of international espionage on a mission that will unfold in something beyond real time.", 
    "movie_url": "https://www.youtube.com/watch?v=7SE0z3bGIBc&ab_channel=MovieclipsTrailers"
    }
    '''
    movie = request.json
    #query = ''' INSERT INTO MOVIES (movie_name, movie_url, movie_synopsis, movie_genre, movie_notation, movie_date) VALUES (?, ?, ?, ?, ?, ?) '''
    to_append = (movie['movie_name'], movie['movie_url'], movie['movie_synopsis'], movie['movie_genre'], movie['movie_notation'], movie['movie_date'])


    conn = sqlite3.connect('moviesDB.db')
    create_movies(conn, to_append)


    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT * FROM MOVIES;').fetchall()
    
    print(movie)
    return jsonify(all_movies)


###############################
#           remove            #
###############################

@app.route('/movies/delete', methods=['GET'])
def api_delete():
    '''
function to delete one or multiples movies from the database by using his movie_genre, his movie_date, his movie_name or his movie_notation
exemple :
    http://127.0.0.1:5000/movies/delete?movie_name=film_name
    http://127.0.0.1:5000/movies/delete?movie_date=film_date
    '''
    query_parameters = request.args

    movie_genre = query_parameters.get('movie_genre')
    movie_date = query_parameters.get('movie_date')
    movie_name = query_parameters.get('movie_name')
    movie_notation = query_parameters.get('movie_notation')

    query = "DELETE FROM MOVIES WHERE"
    to_filter = []

    if movie_genre:
        print(movie_genre)
        query += ' movie_genre=? AND'
        to_filter.append(movie_genre)
    if movie_date:
        print(movie_date)
        query += ' movie_date=? AND'
        to_filter.append(movie_date)
    if movie_name:
        print(movie_name)
        query += ' movie_name like ? AND'
        to_filter.append(movie_name+"%")
    if movie_notation:
        print(movie_notation)
        query += ' movie_notation <= ? AND'
        to_filter.append(movie_notation)
    if not (movie_name or movie_genre or movie_date or movie_notation):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute(query, to_filter).fetchall()
    conn.commit()
    print('One movie has been removed from the website')


    conn2 = sqlite3.connect('moviesDB.db')
    conn2.row_factory = dict_factory
    cur = conn2.cursor()
    all_movies = cur.execute('SELECT * FROM MOVIES;').fetchall()

    return jsonify(all_movies)

###############################
#           update            #
###############################
def update_movie_notation(conn, movie_elts):
    sql = ''' UPDATE MOVIES
              SET movie_notation = ?
              WHERE movie_name like ?'''
    cur = conn.cursor()
    cur.execute(sql, movie_elts)
    conn.commit()


@app.route('/movies/update_notation', methods=['GET'])
def api_update():
    '''
function to update the notation of a movie from the database by using his movie_notation and his movie_name
exemple :
    http://127.0.0.1:5000/movies/update_notation?movie_notation=film_notation&movie_name=film_name
    ou
    http://127.0.0.1:5000/movies/update_notation?movie_name=film_name&movie_notation=film_notation
    '''
    query_parameters = request.args
    movie_notation = query_parameters.get('movie_notation')
    movie_name = query_parameters.get('movie_name')

    to_update = (movie_notation, movie_name+"%")
    
    conn = sqlite3.connect('moviesDB.db')
    update_movie_notation(conn, to_update)


    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT * FROM MOVIES;').fetchall()
    
    return jsonify(all_movies)

def update_movie_url(conn, movie_elts):
    sql = ''' UPDATE MOVIES
              SET movie_url = ?
              WHERE movie_name like ?'''
    cur = conn.cursor()
    cur.execute(sql, movie_elts)
    conn.commit()

@app.route('/movies/update_url', methods=['GET'])
def api_update_url():
    '''
function to update the url of a movie from the database by using his movie_notation and his movie_name (only if the url is down)
exemple :
    http://127.0.0.1:5000/movies/update_url?movie_notation=film_notation&movie_name=film_name
    ou
    http://127.0.0.1:5000/movies/update_url?movie_name=film_name&movie_notation=film_notation
    '''
    query_parameters = request.args
    movie_url = query_parameters.get('movie_url')
    movie_name = query_parameters.get('movie_name')

    to_update = (movie_url, movie_name)
    
    conn = sqlite3.connect('moviesDB.db')
    update_movie_url(conn, to_update)


    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT * FROM MOVIES;').fetchall()
    
    return jsonify(all_movies)
    

#app.run()
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5004)


#port=os.getenv('PORT'))
