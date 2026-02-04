from flask import Flask

app = Flask(__name__)

@app.route('/')

def HelloWorld():
    return '<h1>Y hệt HTML !</h1>'

@app.route('/user/<name>')

def HelloUser(name):
    return f'<h2>Chào {name} ! </h2>'


if __name__ =='__main__':
    app.run(debug = True)
