# https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

from flask import Flask, render_template, request, redirect
from models import db, Client

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        phone = request.form['phone']
        
        db.session.add(Client(email=email, name=name, phone=phone))
        db.session.commit()
        return redirect('/')
    return render_template('forms.html')

@app.route('/')
def index():
    clients = Client.query.all()
    return render_template('index.html', clients=clients)

if __name__ == '__main__':
    app.run(debug=True)
