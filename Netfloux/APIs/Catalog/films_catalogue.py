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
    all_books = cur.execute('SELECT * FROM MOVIES;').fetchall()

    return jsonify(all_books)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


#app.run()
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5001)

#port=os.getenv('PORT'))
