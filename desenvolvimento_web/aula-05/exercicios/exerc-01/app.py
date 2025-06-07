# https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

from flask import Flask, render_template, request, redirect
from models import db, Client, Order
from datetime import date, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client.db'
db.init_app(app)


with app.app_context():
    db.create_all()
    test_clients = [
        Client(email='abc@abc.com', name='abc'),
        Client(email='bbc@abc.com', name='bbc'),
    ]
    test_orders = [
        Order(id=1, date="12032025", price=2.00, client_email='abc@abc.com'),
        Order(id=2, date="21052025", price=2.00, client_email='abc@abc.com'),
        Order(id=3, date="21052025", price=2.00, client_email='bbc@abc.com')
    ]

    if not Client.query.first():
        db.session.add_all(test_clients)
        db.session.add_all(test_orders)
        
    db.session.commit()
    
    print(Order.query.all())
    print(Client.query.all())

@app.route('/delete', methods=['POST'])
def delete():
    email = request.form.get('email')
    client = Client.query.filter_by(email=email).first()
    if client:
        db.session.delete(client)
        db.session.commit()
    return redirect('/')

@app.route("/update", methods=["POST"])
def update():
    oldemail = request.form.get("oldemail")
    newemail = request.form.get("newemail")
    newname = request.form.get("newname")
    newphone = request.form.get("newphone")
    client = Client.query.filter_by(email=oldemail).first()
    if client:
        client.email = newemail
        client.name = newname
        client.phone = newphone
        db.session.commit()
    return redirect("/")

@app.route('/orders', methods=['GET'])
def orders():
    orders = Order.query.all()
    clients = Client.query.all()
    return render_template('orders.html', orders=orders, clients=clients)

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
