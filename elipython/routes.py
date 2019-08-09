from flask import render_template, url_for, flash, redirect, request
from elipython import app
from elipython.forms import LoginForm, Taschenrechner

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
    return render_template('index.html', loginData=loginData, title='Startseite')

@app.route("/search")
def search():
    return render_template('search.html', title='search')
