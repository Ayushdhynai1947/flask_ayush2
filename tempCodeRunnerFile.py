# app.py
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    # return "Hello, World!"

@app.route('/products')
def products():
    return 'this is porduct page'

if __name__ == '__main__':
    app.run(debug=True)

