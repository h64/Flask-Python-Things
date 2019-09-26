from flask import Blueprint, redirect, render_template, request
from datetime import datetime

character_blueprint = Blueprint('characters', __name__, url_prefix='/characters')

@character_blueprint.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('characters/index.html')
    elif request.method == 'POST':
        name = request.form['name']
        # print('You typed the name:', name)
        formatted_langs = [x.strip() for x in request.form['languages'].split(',')]
        # print('You typed the languages:', formatted_langs)
        if request.form['birthday']:
            formatted_date = datetime.strptime(request.form['birthday'], '%Y-%m-%d')
            # print(formatted_date)
        else:
            formatted_date = None
        return redirect('/characters')