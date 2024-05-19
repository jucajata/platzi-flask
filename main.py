from flask import Flask, request, make_response, redirect, render_template, session
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

load_dotenv()

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar café', 'Enviar solicitud de compra', 'Entregar vídeo al productor']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def internal_server_error(error):
  return render_template('500.html', error=error)
    

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@app.route('/server_error')
def server_error():
    raise(Exception('500 error'))
    

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    login_form =LoginForm()
    context = {
        'user_ip':user_ip, 
        'todos':todos,
        'login_form': login_form
    }
    return render_template('hello.html', **context)