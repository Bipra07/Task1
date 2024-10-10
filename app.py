# Flask app with automatic dummy data insertion
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(80), nullable=False)

# Create tables and insert dummy data
@app.before_first_request
def create_tables_and_insert_data():
    db.create_all()
    if Property.query.first() is None:
        properties = [
            Property(price=100000, location="Downtown", type="sale"),
            Property(price=2000, location="Uptown", type="rent"),
            Property(price=500000, location="Suburbs", type="sale"),
            Property(price=1500, location="City Center", type="rent")
        ]
        db.session.bulk_save_objects(properties)
        db.session.commit()

# Routes (Signup, Login, Get Properties)
# [...]

if __name__ == '__main__':
    app.run(debug=True)
