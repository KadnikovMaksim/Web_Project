from flask import Flask, render_template, redirect
from flask_login import (LoginManager, login_user, login_required,
                         logout_user)

from data import db_session

from data.users import User
# from data.jobs import Jobs
from data.registration import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def Load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
        return render_template('registration.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('registration.html', title='Авторизация', form=form)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    # jobs = db_sess.query(Jobs).all()
    users = db_sess.query(User).all()
    names = {name.id: (name.surname, name.name) for name in users}
    return render_template('index.html', jobs=jobs,
                           names=names, title='Загловок')


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/mars_explorer.sqlite")
    app.run()


if __name__ == '__main__':
    main()
