from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CreateForm(FlaskForm):
    topic = StringField('Тема', validators=[DataRequired()])
    subject = StringField('Тема', validators=[DataRequired()])
    question = StringField("Вопрос", validators=[DataRequired()])
    answer = StringField('Ответ', validators=[DataRequired()])
    submit = SubmitField('Создать')

class ChangeForm(FlaskForm):
    topic = StringField('Тема', validators=[DataRequired()])
    subject = SelectField('Предмет', choices=[('Математика', 'Математика'), ('Биология', 'Биология'),
                                              ('Химия', 'Химия'), ('История', 'История'), ('Русский язык', 'Русский язык'),
                                              ('Физика', 'Физика')], validators=[DataRequired()])
    question = StringField("Вопрос", validators=[DataRequired()])
    answer = StringField('Ответ', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
