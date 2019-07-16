from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username=StringField('Benutzername (e-mail)', validators=[Email(), DataRequired()])
    password=PasswordField('Passwort', validators=[DataRequired()])
    submit=SubmitField('Login')

# Für Bootcamp
class Taschenrechner(FlaskForm):
    wert1=DecimalField('Erster Wert', validators=[DataRequired()])
    wert2=DecimalField('Zweiter Wert', validators=[DataRequired()])
    meinoperator=SelectField('Operation', choices=[('+', '+'), ('-', '-'), ('x', '*'), ('/', '/')])
    submit=SubmitField('Rechnen')
