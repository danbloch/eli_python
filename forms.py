from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    username=StringField('Benutzername (e-mail)', validators=[DataRequired(), Email()])
    password=PasswordField('Passwort', validators=[DataRequired()])
    submit=SubmitField('Login')
