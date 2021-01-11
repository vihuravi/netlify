from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manytone.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgres+psycopg2://voqhaatngxcffq:c30decc3cc73e1d0ce0e52000fc370530d701061800fcfb040d5a1946b8c98f0@ec2-52-72-34-184.compute-1.amazonaws.com/d98o1tg078te5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = '1238sadh1234390823kjhdJKA*(@E$^$'
