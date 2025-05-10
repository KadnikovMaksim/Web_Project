from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    login = StringField('Имя пользователя', validators=[DataRequired()])

    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')

class LoginForm(FlaskForm):
    password = PasswordField('Пароль', validators=[DataRequired()])
    login = StringField('Имя пользователя', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
