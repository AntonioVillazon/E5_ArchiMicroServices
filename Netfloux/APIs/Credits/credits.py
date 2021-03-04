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
 	  		 	       	 	  		 	      

@app.route('/', methods=['GET'])
def home():
    return '''
<!DOCTYPE html>	 	 	  		 	      
<html lang="en">
 <style>	 	 	  		 	      
body {	 	 	  		 	      
    background-color: #F9FFD8;
    text-align: center;
    color : black
}
</style>

<body>
    <h1>Credits</h1>
    <h2>Created by Yassine GOUMBARK, Antonio VILLAZON and Yonnel NYOKAS</h2>
    <br>
    <p>Python version : <b style="color:red;"><i>3.7.3</i></b></p>
    <br>
    <p>PostgreSQL version : <b style="color:red;"><i>JDBC 42.2.18</i></b></p>
    <br>
    <p>Angular version : <b style="color:red;"><i>11</i></b></p>
    <br>
    <p>Java version : <b style="color:red;"><i>1.8</i></b></p>
    <br>
    <p>PGAdmin version : <b style="color:red;"><i>4</i></b></p>
</body>
'''

#app.run()


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5006)

#port=os.getenv('PORT'))
