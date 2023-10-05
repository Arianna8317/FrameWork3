from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, EqualTo

#Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться".
class RegistrationForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    second_name = StringField('Фамилия', validators=[DataRequired()]) 
    e_mail = StringField('e-Mail', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    confirmation_password = StringField(
    'Password again',     validators=[DataRequired(), EqualTo('password')]
  )

