from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dan")
def hello2():
    return "gucki"

@app.route("/dan2")
def hello3():
    return "gucki5"

if __name__ == '--main--':
    app.run(debug=True)
