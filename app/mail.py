from flask import(
    Blueprint, render_template
)

bp = Blueprint('mail', __name__, url_prefix="/") #el url_prefix es para poner una ruta antes de la ruta que se quiere llegar ejemplo, https:hola/modulo, el hola/, seria el url_prefix se mostrara en todas las url

@bp.route('/', methods=['GET'])
def index():
    return render_template('mails/index.html')
