from flask import Flask, render_template, request, make_response, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from models import db, User
from logging import getLogger as Logger
from registration_form import RegistrationForm


app = Flask(__name__)
logger = Logger(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///register.db'
db.init_app(app)
#csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
  db.create_all()
  print('OK')


@app.get('/')
def home():
    context = {'users': User.query.all()}
    return render_template('home.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'POST' and form.validate():
        first_name=form.first_name.data,
        second_name=form.second_name.data,
        e_mail=form.e_mail.data,
        password=form.password.data
        user = User(
          first_name,   second_name,
          e_mail,
          password
        )
        user.set_password()
        db.session.add(user)
        db.session.commit()

        response = make_response(redirect(url_for('home')))
        flash('You have been successfully registered!', 'success')
        return response
    else:
        return render_template('register.html', form=form)




if __name__ == "__main__":
    app.run(debug=True)