from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
print(app.config.from_object(Config))
db = SQLAlchemy(app)

from models import User  # Import your models here

@app.route('/')
def home():
    return "Hello, Flask with SQLAlchemy and MySQL!"

if __name__ == '__main__':
    app.run(debug=True)
