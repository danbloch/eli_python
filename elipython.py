from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dan")
def hello():
    return "Hello Dan"

if __name__ == '--main--':
    app.run(debug=True)
