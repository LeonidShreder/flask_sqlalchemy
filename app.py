from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy



from models import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postrges://password:test123@localhost/flaskmovie'
app.config.from_object((Configuration))

app.register_blueprint(post, url_prefix='/blog')
db = SQLAlchemy(app)

@app.route('/')
def index():
    return '<h1> hello flask</h1>'


if __name__ == '__main__':
    app.run()
