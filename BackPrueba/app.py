from flask import Flask
from dotenv import load_dotenv
import os
from config.database import db

load_dotenv()

databaseURL = os.getenv("DATABASE_URL")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = databaseURL

db.init_app(app)
