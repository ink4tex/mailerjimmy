
from re import sub
from flask import(
    Blueprint, render_template, request, flash, redirect,url_for, current_app
)
from .db import get_db
import sendgrid
bp = Blueprint('mail', __name__, url_prefix="/") #el url_prefix es para poner una ruta antes de la ruta que se quiere llegar ejemplo, https:hola/modulo, el hola/, seria el url_prefix se mostrara en todas las url

@bp.route('/', methods=['GET'])
def index():
    search = request.args.get('search')
    db, c = get_db()
    if search is None:
        c.execute("SELECT * FROM email")
    else:
        c.execute("SELECT * FROM email WHERE content like %s",('%' + search + '%', ))
    
    
    mails = c.fetchall()
    return render_template('mails/index.html', mails = mails)

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        email = request.form.get('email')
        subject = request.form.get('subject')
        content = request.form.get('content')
        errors = []

        if not email:
            errors.append('El Email es Obligatorio')
        elif "@" not in email:
            errors.append('El Email es Invalido')
        else:
            pass
        if not subject:
            errors.append('El Asunto es Obligatorio')        
        if not content:
            errors.append('El Contenito es Obligatorio')

        if len(errors) == 0:
            db, c = get_db()
            c.execute("INSERT INTO email(emial, subject, content) VALUES (%s, %s, %s)", (email, subject, content))
            db.commit()

            return redirect(url_for('mail.index'))
        else:
            for error in errors:
                flash(error)
    return render_template('mails/create.html')

def send(to, subject, content):
    sg = sendgrid.SendGridAPIClient(api_key=current_app.config['SENDGRID_KEY'])