from flask import render_template, url_for, flash, redirect, request, session
from elipython import app
from elipython.forms import LoginForm, Taschenrechner
import api_client

@app.route("/", methods=["GET","POST"])
def bootcamp():
    form=Taschenrechner()
    form.validate_on_submit()
    return render_template('bootcamp.html', title='bootcamp', name='Dan', form=form)

@app.route("/result", methods=["GET","POST"])
def result():
    form=Taschenrechner()
    if form.validate_on_submit():
        wert1=request.form['wert1']
        wert2=request.form['wert2']
        meinoperator=request.form['meinoperator']
        ergebnis=eval(wert1+meinoperator+wert2)
        return render_template('result.html', title='result', ergebnis=ergebnis)
    return render_template('result.html', title='result', ergebnis="Fehler")

@app.route("/meiner", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "dan.bloch@europace.de" and form.password.data == "supersafe":
            flash(f'Login succesful for {form.username.data}!', 'success')
            return redirect(url_for('search'))
        else:
            flash(f'Login unsuccesful!', 'danger')
    return render_template('login.html', title='login', form=form)


@app.route("/login")
def index():
    return render_template('loginform.html', title='Startseite')

@app.route("/search")
def search():
    return render_template('search.html', title='search')

@app.route("/angebote")
def angebote():
    if session.get('token') is None:
        return redirect(url_for('index'))
    return render_template('angebote.html', title='search')

@app.route("/resultlogin", methods=["GET","POST"])
def resultlogin():
    user=request.form['username']
    password=request.form['password']
    token, loginSuccessful=api_client.getToken(user, password)
    if loginSuccessful:
        session['token']=token
        return render_template('resultlogin.html', title='Login Result')
    else:
        return render_template('loginform.html', title='Startseite')
