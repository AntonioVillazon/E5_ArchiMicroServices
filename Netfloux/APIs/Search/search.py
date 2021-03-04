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

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Movies Display</h1>
<p>This API will only display all the movies contained in our database and that will be display as a catalogue in our website.</p>'''



@app.route('/movies/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT * FROM MOVIES;').fetchall()

    return jsonify(all_movies)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/movies', methods=['GET'])
def api_filter():
    query_parameters = request.args

    movie_id = query_parameters.get('movie_id')
    movie_genre = query_parameters.get('movie_genre')
    movie_date = query_parameters.get('movie_date')
    movie_name = query_parameters.get('movie_name')
    movie_notation = query_parameters.get('movie_notation')

    query = "SELECT * FROM MOVIES WHERE"
    to_filter = []

    if movie_id:
        print(movie_id)
        query += ' movie_id=? AND'
        to_filter.append(movie_id)
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
        query += ' movie_notation >= ? AND'
        to_filter.append(movie_notation)
    if not (movie_id or movie_name or movie_genre or movie_date or movie_notation):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)





#app.run()
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5003)

#port=os.getenv('PORT'))
