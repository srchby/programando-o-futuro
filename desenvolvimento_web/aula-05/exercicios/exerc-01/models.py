from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Client(db.Model):
    email = db.Column(db.String(254), primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
