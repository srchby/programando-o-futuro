from flask import Flask, render_template, request
app = Flask(__name__)
products = []

@app.route('/', methods=['GET','POST'])
def manage_products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        products.append({'name': name, 'price': price, 'description': description  })
        
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)