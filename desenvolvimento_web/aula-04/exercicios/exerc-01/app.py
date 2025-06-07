from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
products = []

@app.route('/', methods=['GET','POST'])
def manage_products():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        price = request.form.get('price', '').strip()
        price = int(price)
        description = request.form.get('description', '').strip()
        if name and price and description:
            products.append({'name': name, 'price': price, 'description': description})
        return redirect(url_for('manage_products')) 
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)