from flask import Flask, render_template, url_for
app = Flask(__name__)

loginData = [
    {
        'User': 'Dan',
        'Password': 'supersafe'
    },
    {
        'User': 'Olaf',
        'Password': 'supersafe'
    }
]

@app.route("/")
def login():
    return render_template('index.html', loginData=loginData, title='login')

@app.route("/search")
def search():
    return render_template('search.html', title='search')

@app.route("/result")
def result():
    return render_template('result.html', title='result')

if __name__ == '__main__':
    app.run(debug=True)
