from flask import Flask, render_template, url_for
from forms import LoginForm

app = Flask(__name__)

#app.config['SECRET_KEY']=''

loginData = [
    {
        'User': 'dan.bloch@europace.de',
        'Password': 'supersafe'
    },
    {
        'User': 'olaf.hausmann@europace.de',
        'Password': 'supersafe'
    }
]

@app.route("/")
def login():
    return render_template('index.html', loginData=loginData, title='login')

@app.route("/login")
def login2():
    form = LoginForm()

@app.route("/search")
def search():
    return render_template('search.html', title='search')

@app.route("/result")
def result():
    return render_template('result.html', title='result')

if __name__ == '__main__':
    app.run(debug=True)
