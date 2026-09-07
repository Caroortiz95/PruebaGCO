from flask import Flask
from dotenv import load_dotenv
import os
from config.database import db
from routes import bp
from Models import crear_modelos

load_dotenv()

databaseURL = os.getenv("DATABASE_URL")

app = Flask(__name__)
app.register_blueprint(bp)

app.config["SQLALCHEMY_DATABASE_URI"] = databaseURL

db.init_app(app)

with app.app_context():
    crear_modelos()

if __name__ == '__main__':
    app.run(debug=True)