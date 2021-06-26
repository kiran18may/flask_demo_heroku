from flask import Flask
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def index():
    return "<h1> THis is a flask application </h1>"

if __name__ == "__main__":
    app.run()