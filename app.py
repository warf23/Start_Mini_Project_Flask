from flask import Flask , render_template  , url_for
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


# Create the application instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    content = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Integer , default=0)
    date_created = db.Column(db.DateTime , default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# Create a URL route in our application for "/"
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True )