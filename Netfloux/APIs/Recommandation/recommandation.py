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
    return '''<h1>Movies recommanded Display</h1>
<p>This API will only display all the movies contained in our database that we want to recommand to the customers.
</p>'''

@app.route('/movies/recommanded', methods=['GET'])
def api_recommanded_films():
    conn = sqlite3.connect('moviesDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    recommanded_movies = cur.execute('SELECT * FROM MOVIES WHERE movie_notation >= 3.5;').fetchall()

    return jsonify(recommanded_movies)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


#app.run()
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5002)

#port=os.getenv('PORT'))
