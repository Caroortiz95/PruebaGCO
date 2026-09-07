from flask import Flask
from config.database import db
from routes import bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(bp)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)