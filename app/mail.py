from flask import(
    Blueprint, render_template
)
from .db import get_db
bp = Blueprint('mail', __name__, url_prefix="/") #el url_prefix es para poner una ruta antes de la ruta que se quiere llegar ejemplo, https:hola/modulo, el hola/, seria el url_prefix se mostrara en todas las url

@bp.route('/', methods=['GET'])
def index():
    db, c = get_db()
    c.execute("SELECT * FROM email")
    mails = c.fetchall()
    return render_template('mails/index.html', mails = mails)
