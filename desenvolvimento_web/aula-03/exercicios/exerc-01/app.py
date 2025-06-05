from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('idade.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    idade = request.form['idade']
    idade = int(idade)
    return render_template('resultado.html', idade=idade)

if __name__ == '__main__':
    app.run(debug=True)