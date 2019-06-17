from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='dan'

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

@app.route("/login")
def index():
    return render_template('index.html', loginData=loginData, title='Startseite')

@app.route("/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login succesful for {form.username.data}!', 'success')
        return redirect(url_for('search'))
    return render_template('login.html', title='login', form=form)

@app.route("/search")
def search():
    return render_template('search.html', title='search')

@app.route("/result")
def result():
    return render_template('result.html', title='result')

if __name__ == '__main__':
    app.run(debug=True)
