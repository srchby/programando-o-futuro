from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

db = SQLAlchemy()

class Client(db.Model):
    email = db.Column(db.String(254), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(14))
    
    orders = db.relationship('Order', back_populates='client', cascade='all, delete-orphan')
    
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, default=date.today)
    price = db.Column(db.Float, nullable=False)
    
    client_email = db.Column(db.String(254), db.ForeignKey('client.email'), nullable=False)
    client=db.relationship('Client', back_populates='orders')
    