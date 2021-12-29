import os

from flask import Flask
from flaskext.mysql import MySQL
from flask_cors import CORS, cross_origin

app = Flask(__name__, instance_relative_config=True)
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'e0doeq3m0o50of4t'
app.config['MYSQL_DATABASE_PASSWORD'] = 'g9xjd28zj9ys0nip'
app.config['MYSQL_DATABASE_DB'] = 'm69uprljet8vajzk'
app.config['MYSQL_DATABASE_HOST'] = 'j5zntocs2dn6c3fj.chr7pe7iynqr.eu-west-1.rds.amazonaws.com'
#app.config['MYSQL_DATABASE_USER'] = 'root'
#app.config['MYSQL_DATABASE_DB'] = 'w3school_tutorial'
#app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

try:
    os.makedirs(app.instance_path)
except OSError:
    pass