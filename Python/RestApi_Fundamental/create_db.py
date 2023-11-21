from application import db
from application import Drink
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))



with app.app_context():
    db.create_all()

    if Drink.query.first():
        # Delete all existing drinks
        Drink.query.delete()
        db.session.commit()

    drink1=Drink(name="Grape Soda", description="Tastes like soda")
    db.session.add(drink1)
    drink2=Drink(name="Cherry",description="Tastes like that one ice cream")
    db.session.add(drink2)
    db.session.commit()


# Additional code for creating tables or performing other operations




