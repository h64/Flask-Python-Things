from flask import Blueprint, render_template, request

character_blueprint = Blueprint('characters', __name__, url_prefix='/characters')

@character_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('characters/index.html')
    elif request.method == 'POST':
        return 'POST REACHED'