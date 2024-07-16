from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import environment

app = Flask(__name__)

app.config.from_object(environment[getenv('ENVIRONMENT')])


api = Api(
    app,
    title='Template Login',
    version='0.1',
    description='Endpoints',
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
