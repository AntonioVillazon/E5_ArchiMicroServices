import os
import flask
from flask import Flask, request, jsonify
import sqlite3

#app = flask.Flask(__name__)
#app.config["DEBUG"] = True
app = Flask(__name__)

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
    return '''<h1>Profils Management</h1>
<p>This API will help us to manage the profils database with actions like add a profil, remove a profil, update the informations of a profil.</p>'''


@app.route('/profils/all', methods=['GET'])
def api_all():
    '''fucntion to display all the movies objects from the database'''
    conn = sqlite3.connect('profilsDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_movies = cur.execute('SELECT login, name FROM PROFILS;').fetchall()

    return jsonify(all_movies)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

###############################
#           append            #
###############################

def create_profil(conn, profil):
    sql = ''' INSERT INTO PROFILS(login,name,password)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, profil)
    conn.commit()
    return cur.lastrowid


@app.route('/profils/append', methods=['POST'])
def api_append_profil():
    '''
function to append a profil as a json object with the POST method
exemple (if you can use a softwore like POSTMAN) :
    {
    "login": "new_profil", 
    "name": "new_name", 
    "password": "new_pwd"
    }
    '''
    profil = request.json
    #query = ''' INSERT INTO PROFILS (login, name, password) VALUES (?, ?, ?) '''
    to_append = (profil['login'], profil['name'], profil['password'])


    conn = sqlite3.connect('profilsDB.db')
    create_profil(conn, to_append)


    conn = sqlite3.connect('profilsDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_profils = cur.execute('SELECT login, name FROM PROFILS;').fetchall()
    
    return jsonify(all_profils)

###############################
#           remove            #
###############################

@app.route('/profils/delete', methods=['GET'])
def api_delete():
    '''
function to delete one or multiples profils from the database by using his login or his name
exemple :
    http://127.0.0.1:5000/profils/delete?login=profil_login
    http://127.0.0.1:5000/profils/delete?name=profil_name
    '''
    query_parameters = request.args

    name = query_parameters.get('name')
    login = query_parameters.get('login')

    query = "DELETE FROM PROFILS WHERE"
    to_filter = []

    if name:
        print(name)
        query += ' name = ? AND'
        to_filter.append(name+"%")
    if login:
        print(login)
        query += ' login = ? AND'
        to_filter.append(login)
    if not (name or login):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('profilsDB.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    cur.execute(query, to_filter).fetchall()
    conn.commit()
    print('One profil has been removed from the website')


    conn2 = sqlite3.connect('profilsDB.db')
    conn2.row_factory = dict_factory
    cur = conn2.cursor()
    all_profils = cur.execute('SELECT login, name FROM PROFILS;').fetchall()

    return jsonify(all_profils)


###############################
#           update            #
###############################
def update_profil_password(conn, profil_elts):
    sql = ''' UPDATE PROFILS
              SET password = ?
              WHERE login = ?'''
    cur = conn.cursor()
    cur.execute(sql, profil_elts)
    conn.commit()

@app.route('/profils/update_password', methods=['GET'])
def api_update_password():
    '''
function to update the notation of a movie from the database by using his movie_notation and his movie_name
exemple :
    http://127.0.0.1:5000/profils/update_password?password=profil_password&login=profil_login
    ou
    http://127.0.0.1:5000/profils/update_password?login=profil_login&password=profil_password
    '''
    query_parameters = request.args
    password = query_parameters.get('password')
    login = query_parameters.get('login')

    to_update = (password, login)
    
    conn = sqlite3.connect('profilsDB.db')
    update_profil_password(conn, to_update)
    
    return """<p> The password has been updated for """+login+"""</p>"""



#app.run()
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5005)

#port=os.getenv('PORT')
