from data.users import Users
from data.questions import Questions
import sozdanie_BD
from flask import Flask, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import sqlalchemy
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired
from flask import render_template
from flask import redirect
from forms.user import LoginForm, RegisterForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = sozdanie_BD.db_session.create_session()
    return db_sess.query(Users).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = sozdanie_BD.db_session.create_session()
        if db_sess.query(Users).filter(Users.login == form.login.data).first():
            return render_template('registration.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = Users()
        user.login = form.login.data
        user.about = form.about.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('registration.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('f')
    if form.validate_on_submit():
        db_sess = sozdanie_BD.db_session.create_session()
        user = db_sess.query(Users).filter(Users.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me)
            return redirect("/home")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/home', methods=['GET', 'POST'])
@login_required
def main():
    if request.method == 'POST':
        topic = request.form.get('topic')
        question = request.form.get('question')
        subject = request.form.get('subject')

    db_sess = sozdanie_BD.db_session.create_session()
    quests = db_sess.query(Questions).filter(Questions.user_id == current_user.id)
    return render_template('home.html', title='', quests=quests)


@app.route('/')
def a():
    return render_template('base.html', title='Аунтефикация')


app.run()
