from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/databasename'
db = SQLAlchemy(app)

from app.models import user, building, bathroom, review
from app.routes import user_routes, building_routes, bathroom_routes, review_routes
